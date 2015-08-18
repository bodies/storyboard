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
    # TODO: 사용자 랭킹 등 보여주기
    logged = s.is_logged()
    session_data = s.data()
    return template('user_main.tpl', title='시용자 페이지', logged=logged,
                    member=session_data)


@app.route('/<user_id>')
def user_page(user_id):
    """
    TO-DOs:
    1. 로그인 여부 확인
    2. 사용자 정보 & 최근 작품 목록 출력
    3. 로그인 중이라면, 정보 수정, 새 작품 쓰기, 작품 수정 등 기능 제공
    """
    try:
        m = member.Member()
        if not m.has_id(user_id):
            raise Exception('사용자 페이지가 존재하지 않습니다.')
        keys = ('id', 'name', 'intro', 'point', 'level', 'reg_date')
        result = m.data(user_id, keys)
        if not result:
            raise Exception('사용자 정보가 존재하지 않습니다.')
        data = dict(zip(keys, result))

        logged = s.is_logged(user_id)
        session_data = s.data()

        return template('user_user_page.tpl',
                        title='{}의 페이지'.format(user_id), data=data,
                        logged=logged, member=session_data)
    except Exception as e:
        print('EXCEPTION in user_page')
        return template('popup.tpl', msg=str(e))


@app.route('/<user_id>/update_info')
def update_info(user_id):
    # 한번 더 암호 묻기
    # TODO: 로그인 여부 확인! (세션 데이터가 없으면 템플릿에서 에러 발생!)
    try:
        if not s.is_logged(user_id):
            raise Exception('사용자 정보를 수정할 권한이 없습니다.')

        info = {}
        session_data = s.data()
        info['num'] = session_data['user_num']
        info['id'] = session_data['user_id']
        info['name'] = session_data['user_name']
        info['level'] = session_data['level']

        m = member.Member()
        etc_data = m.extra_data(session_data['user_num'])
        info['email'] = etc_data[0]
        info['intro'] = etc_data[1]
        if not info['intro']:
            info['intro'] = ''

        return template('user_info_form.tpl', title='사용자 정보 수정', info=info,
                        logged=True, member=session_data)

    except Exception as e:
        print('UPDATE_USER EXCEPTION: ', e)
        return template('popup.tpl', msg=e)


@app.route('/<user_id>/update_info', method='post')
def do_update_info(user_id):
    try:
        if not s.is_logged(user_id):
            raise Exception('사용자 정보를 수정할 권한이 없습니다.')
        home_url = '/u/{}'.format(user_id)
        name = request.forms.getunicode('name', None)
        email = request.forms.getunicode('email', None)
        password = request.forms.getunicode('password', None)
        password2 = request.forms.getunicode('password2', None)
        intro = request.forms.getunicode('intro', None)

        if password != password2:
            raise Exception('비밀번호가 일치하지 않습니다.')

        m = member.Member()
        m.update(user_id, name=name, email=email, password=password, intro=intro)

        return template('popup', msg='{}님의 정보를 갱신했습니다.'.format(user_id), dest=home_url)

    except Exception as e:
        return template('popup.tpl', msg=str(e), dest=home_url)


@app.route('/<user_id>/newbook')
def new_book(user_id):
    """ 새 책 등록: 폼 출력 """
    try:
        if not s.is_logged(user_id):
            raise Exception('새 책을 등록한 권한이 없습니다.')

        print("MAKING NEW BOOK...")

        return template('user_new_book_form.tpl', title='새 책 등록',
                        logged=True, member=s.data())
    except Exception as e:
        return template('popup', msg=str(e))


@app.route('/<user_id>/newbook', method='post')
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
