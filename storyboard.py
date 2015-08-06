"""
    Story Board
"""

from bottle import Bottle, static_file
from subroutes import book, story, user


# ----- ROUTING ----- #

app = Bottle()

app.mount('/b', book.app)
app.mount('/v', story.app)
app.mount('/u', user.app)


@app.route('/')
def main():
    return ('This is the main page...')


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
