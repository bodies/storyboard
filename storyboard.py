"""
    Story Board
"""

from bottle import Bottle, redirect, request, run, static_file, template
from beaker.middleware import SessionMiddleware
from subroutes import book, story, user
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

# ----- FUNCS ----- #


def is_logged():
    s = request.environ.get('beaker.session')
    # if 'user_id' in s and 'user_name' in s and 'user_num' in s:
    if 'user_id' in s:
        return True
    else:
        return False


def sess_login(num, id, name):
    s = request.environ.get('beaker.session')
    s['user_id'] = id
    s['user_num'] = num
    s['user_name'] = name


def sess_logout():
    s = request.environ.get('beaker.session')
    s.delete()


# ----- ROUTING ----- #

app = Bottle()
sessioned_app = SessionMiddleware(app, session_opts)

app.mount('/b', book.app)
app.mount('/s', story.app)
app.mount('/u', user.app)


@app.route('/')
def main():
    return ('This is the main page...')


@app.route('/login')
def login_form():
    if is_logged():
        # 이미 로그인했으면 사용자 페이지로
        redirect('/u')
    return template('login_form.tpl', title='로그인')


@app.route('/login', method='post')
def do_login():
    id = request.forms.get('id')
    passwd = request.forms.get('password')
    dest = request.forms.get('dest', '/')

    if not id or not passwd:
        # TO-DOs: 에러 표시 팝업?
        redirect('/login')

    redirect(dest)


@app.route('/logout')
def do_logout():
    sess_logout()
    redirect('/')


@app.route('/join')
def join_form():
    if is_logged():
        redirect('/')
    return template('join_form.tpl', title='회원 가입')


@app.route('/join', method='post')
def do_join():
    pass


@app.route('/static/<filename>')
def serve_static(filename):
    return static_file(filename, root='static')


@app.error(404)
def error404(error):
    # TO-DO: 제대로 된 404 대응 페이지 만들 것!

    return "Nothing Here..."

# ----- END OF ROUTING ----- #


# ----- MAIN ----- #

if __name__ == '__main__':
    run(app=sessioned_app, host='127.0.0.1', port=5000, debug=True, reloader=True)
