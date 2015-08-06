"""
    book.py
"""

from bottle import Bottle, template


app = Bottle()


@app.route('/')
def book_main():
    pass


@app.route('/<book_num:int>')
def show_book(book_num):
    """ TO-DO: 책 정보 & 챕터 목록 출력  """
    pass


@app.error(404)
def error404(error):
    return 'Nothing Here...'
