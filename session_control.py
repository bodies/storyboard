"""
    session_control.py

    beaker.middleware와 함께 사용할 것
"""

from bottle import request


def is_logged(id=None):
    # 로그인 여부 확인
    # id가 넘어오면, 그 id로 로그인 중인 확인
    s = request.environ.get('beaker.session')
    if 'user_id' not in s:
        return False
    elif not id:
        return True
    elif id == s['user_id']:
        return True
    else:
        return False


def is_admin():
    s = request.environ.get('beaker.session')
    if 'user_id' in s and 'level' in s and s['level'] == 0:
        return True
    return False


def login(num, id, name, level):
    s = request.environ.get('beaker.session')
    s['user_id'] = id
    s['user_num'] = num
    s['user_name'] = name
    s['level'] = level
    print('SESSION OK!')


def data(key=None):
    # 세션 데이터 접근용 객체를 반환
    # key값을 지정하면 해당 세션 데이터값만 반환
    s = request.environ.get('beaker.session')
    if not key:
        return s
    elif key in s:
        return s[key]
    else:
        return None


def logout():
    s = request.environ.get('beaker.session')
    s.delete()
