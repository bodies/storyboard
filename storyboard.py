"""
    Story Board
"""

from bottle import Bottle, redirect, request, static_file, template
from subroutes import book, story, user


# ----- ROUTING ----- #

app = Bottle()

app.mount('/b', book.app)
app.mount('/s', story.app)
app.mount('/u', user.app)


@app.route('/')
def main():
    return ('This is the main page...')


@app.route('/login')
def login_form():
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
    pass


@app.route('/join')
def join_form():
    pass


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
    app.run(host='127.0.0.1', port=5000, debug=True, reloader=True)
