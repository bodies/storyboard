# -*- coding: utf-8 -*-

"""
    Story Board
"""

from bottle import Bottle, redirect, request, run, static_file, template
from bottle import html_escape
from beaker.middleware import SessionMiddleware
import re
from subroutes import admin, book, story, user
import session_control as s
import member


# ----- VARIABLES ----- #

# 사용자 관련 DB 작업용
m = member.Member()

# TO-DOs: 프로세스를 껐다가 켜도 로그인이 유지되게 할 것
session_opts = {
    'sesstion.type': 'memory',
    # 'session.cookie_expires': 3000,
    'session.auto': True
}


# ----- ROUTING ----- #

app = Bottle()

app.mount('/b', book.app)
app.mount('/s', story.app)
app.mount('/u', user.app)
app.mount('/admin', admin.app)

sessioned_app = SessionMiddleware(app, session_opts)


@app.route('/')
def main():
    # 최종적으로는 최근 글, 추천 글등을 보여주는 홈페이지 역할
    return template('main.tpl', title='메인 페이지',
        logged=s.is_logged(), member=s.data())


@app.route('/login')
def login_form():
    if s.is_logged():
        # 이미 로그인했으면 사용자 페이지로
        return template('popup.tpl', msg='이미 로그인 중입니다.')
    return template('login_form.tpl', title='로그인', action='/login')


@app.route('/login', method='post')
def do_login():

    id = html_escape(request.forms.getunicode('id', '').strip())
    passwd = request.forms.getunicode('password', '').strip()
    remember = True if request.forms.getunicode('remember') else False
    dest = request.forms.getunicode('dest', '/u/{}'.format(id)).strip()

    if not id or not passwd:
        # 정보가 안 넘어왔을 경우, 팝업으로 경고 후, 로그인 폼으로..
        redirect('/login')
    try:
        user_info = m.login(id, passwd)
        print('USER_INFO: ', user_info)
        if user_info:
            s.login(user_info[0], user_info[1], user_info[2], user_info[3])
        else:
            return template('popup.tpl', msg='아이디/패스워드가 일치하지 않습니다.')
    except Exception as e:
        print(e)
        return template('popup.tpl', msg='일시적인 장애로 로그인할 수 없습니다')
    else:
        redirect(dest)


@app.route('/logout')
def do_logout():
    s.logout()
    redirect('/')


@app.route('/join')
def join_form():
    # TODO: 템플릿에서 사용자 입력값 1차 확인
    if s.is_logged():
        # 이미 가입한 경우, 팝업 안내 후 첫 화면으로
        redirect('/')
    return template('join_form.tpl', title='회원 가입')


@app.route('/join', method='post')
def do_join():
    # TODO: 오류 발생 시, 오류 메시지를 만들어서 에러 페이지로 리다이렉트

    class JoinError(Exception):
        # 회원가입 실패 시, 발생시킬 예외
        def __init__(self, value):
            self.value = value
        # request.forms.decode('utf-8')

    try:
        id = html_escape(request.forms.getunicode('id', '').strip())
        name = html_escape(request.forms.getunicode('name', '').strip())
        email = html_escape(request.forms.getunicode('email', '').strip())
        passwd = request.forms.getunicode('password', '').strip()
        passwd2 = request.forms.getunicode('password2', '').strip()

        if not id or not name or not email or not passwd or not passwd2:
            raise JoinError('가입 정보가 부족합니다.')

        if passwd != passwd2:
            raise JoinError('암호가 일치하지 않습니다.')

        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            raise JoinError('이메일 주소가 옳바르지 않습니다.')

        if m.has_id(id):
            raise JoinError('이미 존재하는 아이디입니다')

        if m.has_email(email):
            raise JoinError('이미 등록된 이메일입니다.')

        if m.has_name(name):
            raise JoinError('이미 등록된 사용자명입니다.')

        m.register(id, name, email, passwd)

    except JoinError as e:
        return template('popup.tpl', msg=e.value)

    except Exception as e:
        # return template('error_popup.tpl',
                        # err_msg='사용자 등록에 실패했습니다. 잠시 후 다시 시도해주세요.')
        return template('popup.tpl', msg=e.args[1])

    else:
        # 가입 절차 완료
        # TODO: 가입 환영 메시지 출력 + 사용자 페이지로 이동
        # redirect('/u/{}'.format(id))
        redirect('/login')
        print('가입 완료')


@app.route('/static/<filename>')
def serve_static(filename):
    return static_file(filename, root='static')


@app.error(404)
def error404(error):
    # TO-DO: 제대로 된 404 대응 페이지 만들 것!

    return "Nothing Here..."


@app.route('/test')
def test():
    return template('test.tpl', title='테스트 페이지')


@app.route('/test', method='post')
def do_test():
    # request.forms.recode_unicode = False
    print(request.forms.getunicodeunicode('abc'))
    pass


# ----- END OF ROUTING ----- #


# ----- MAIN ----- #

if __name__ == '__main__':
    run(app=sessioned_app, host='127.0.0.1', port=5000, debug=True, reloader=True)
