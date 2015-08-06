"""
user.py

handling requests from '/u'
"""

"""
    TO-DOs:
    1) 로그인 확인: 반복되는 공통 작업을 간단하고 직관적으로!

"""

from bottle import Bottle, redirect, template

app = Bottle()


# ----- ROUTING ----- #


@app.route('/')
def show_user_page():
    pass


@app.route('/<user_id>')
def user_page(user_id):
    """
    TO-DOs:
    1. 로그인 여부 확인
    2. 사용자 정보 & 최근 작품 목록 출력
    3. 로그인 중이라면, 정보 수정, 새 작품 쓰기, 작품 수정 등 기능 제공
    """
    pass


@app.route('/<user_id>/new')
def new_book(user_id):
    """ 새 책 등록: 폼 출력 """
    return template('user_new_book_form.tpl', title='새 책 등록')
    pass


@app.route('/<user_id>/new', method='post')
def save_new_book(user_id):
    """ 새 책 등록 : 저장 """
    pass


@app.route('/<user_id>/b')
def user_books(user_id):
    """ 전체 작품 목록  """
    pass


@app.route('/<user_id>/b/<book_num:int>')
def show_book(user_id, book_num):
    """ 책 정보 보기 """
    pass


@app.route('/<user_id>/b/<book_num:int>/mod')
def modify_book(user_id, book_num):
    """ 책 정보 수정: 폼 출력 """
    pass


@app.route('/<user_id>/b/<book_num:int>/mod', method='post')
def save_modified_book(user_id, book_num):
    """ 책 정보 수정: 저장 """
    pass


@app.route('/<user_id>/b/<book_num:int>/new')
def new_story(user_id, book_num):
    """ 새 글 등록: 폼 출력 """
    return template('user_new_story_form.tpl', title='새 글 등록')


@app.route('/<user_id>/b/<book_num:int>/new', method='post')
def save_new_story(user_id, book_num):
    """ 새 글 등록: 저장 """
    pass


@app.route('/<user_id>/s/<story_num:int>')
def show_story(user_id, story_num):
    """ 글 보기 """
    pass


@app.route('/<user_id>/s/<story_num:int>/mod')
def modify_story(user_id, story_num):
    """ 글 수정: 폼 출력 """
    pass


@app.route('/<user_id>/s/<story_num:int>/mod', method='post')
def save_modified_story(user_id, story_num):
    """ 글 수정: 저장 """
    pass


@app.route('/<user_id>/b/<book_num:int>/<number:int>')
def link_story(book_num, number):
    """ 책 속의 회차로 이야기에 직접 접근.
        리디렉트 처리하자.
        eg. /b/1234/15 -> 15회로 연결
    """
    pass


@app.route('/test')
def test_route():
    print('TESTING...')
    redirect('/')


@app.error(404)
def error404(error):
    redirect('/')
