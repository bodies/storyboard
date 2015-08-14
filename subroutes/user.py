"""
user.py

handling requests from '/u'
"""

"""
    TO-DOs:
    1) 로그인 확인
       반복되는 공통 작업을 간단하고 직관적으로!

"""

from bottle import Bottle, redirect, request, template
import session_control as s
import member

app = Bottle()

# ----- ROUTING ----- #


@app.route('/')
def show_user_page():
    print("USER PAGE")
    data = s.data()
    print(data)
    for k, v in data.items():
        print("SESSIONED DATA: ", k, v)


@app.route('/<user_id>')
def user_page(user_id):
    """
    TO-DOs:
    1. 로그인 여부 확인
    2. 사용자 정보 & 최근 작품 목록 출력
    3. 로그인 중이라면, 정보 수정, 새 작품 쓰기, 작품 수정 등 기능 제공
    """

    data = s.data()
    print(data)
    for k, v in data.items():
        print("SESSIONED DATA: ", k, v)

    return '<a href="/u/{}/update_user">사용자 정보 수정</a>'.format(user_id)


@app.route('/<user_id>/update_user')
def update_user(user_id):
    # 한번 더 암호 묻기
    # TODO: 로그인 여부 확인! (세션 데이터가 없으면 템플릿에서 에러 발생!)
    try:
        info = {}
        m = member.Member()
        extra_info = m.extra_info(user_id)
        sessioned_data = s.data()
        for k, v in sessioned_data.items():
            info[k] = v
        info['email'] = extra_info[0]
        info['intro'] = extra_info[1]
        print('INFO: ', info)

        return template('user_info_form.tpl', title='사용자 정보 수정', info=info)
    except Exception as e:
        print(e.args[1])
        return template('error_popup.tpl', err_msg="사용자 정보를 갱신할 수 없습니다.")


@app.route('/<user_id>/update_user', method='post')
def do_update_user(user_id):
    request.forms.get('name', None)
    request.forms.get('email', None)
    request.forms.get('password', None)
    request.forms.get('password2', None)
    request.forms.get('intro', None)
    pass


@app.route('/<user_id>/new')
def new_book(user_id):
    """ 새 책 등록: 폼 출력 """
    return template('user_new_book_form.tpl', title='새 책 등록')
    pass


@app.route('/<user_id>/new', method='post')
def save_new_book(user_id):
    """ 새 책 등록 : 저장 """
    title = request.forms.get('b_title')
    type = request.forms.get('b_type')
    public = request.forms.get('b_public')
    keywords = request.forms.get('b_keywords')
    intro = request.forms.get('b_intro')

    if not title or not type or not public:
        # 잘못된 접근이므로, 사용자 페이지로 돌려보낸다
        pass

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
    title = request.forms.get('s_title')
    text = request.forms.get('s_text')
    public = request.forms.get('s_public')

    if not text:
        # 글 내용이 없므로, 책 페이지로 돌려보낸다
        pass

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
