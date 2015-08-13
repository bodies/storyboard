"""
    admin.py

    '/adm' - 관리자 페이지
"""

from bottle import Bottle, redirect, template
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
    str = ['<table>']

    for r in ls:
        str.append('<tr>')
        str.append('<td>{}</td><td>{}</td>'.format(r['num'], r['id']))
        str.append('<td>{}</td><td>{}</td>'.format(r['name'], r['email']))
        str.append('<td>{}</td></tr>'.format(r['reg_date']))

    str.append('</table>')

    return ''.join(str)
