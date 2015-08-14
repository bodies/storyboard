"""
    admin.py

    '/admin' - 관리자 페이지
"""

from bottle import Bottle, redirect, request, template
import session_control as s
import member

app = Bottle()

m = member.Member()


# ----- ROUTING ----- #

@app.hook('before_request')
def admin_auth():
    # if not s.is_admin():
        # redirect('/login')
    pass


@app.route('/')
def adm_main():
    pass


@app.route('/users')
def show_user_list():
    ls = m.list()
    return template('admin_user_list.tpl', title='사용자 목록', ls=ls)


@app.route('/u/update_user')
def update_user():
    return template('user_info_form.tpl', title='사용자 정보 수정')


@app.route('/delete_user')
def delete_user():
    # TODO: 삭제하는 대신, 정지시키거나 정지된 사용자 테이블로 옮기는 방법을 생각해볼 것.
    user_num = request.query.get('num', None)
    if not user_num:
        redirect('/')
    try:
        m.remove(user_num)
    except Exception as e:
        print(e.args[1])
        return template('error_popup.tpl', err_msg='사용자를 삭제할 수 없습니다.')
