"""
    session_control.py

    beaker.middleware와 함께 사용할 것
"""

from bottle import request


def is_logged():
    s = request.environ.get('beaker.session')
    return True if 'user_id' in s else False


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


def data():
    s = request.environ.get('beaker.session')
    return s


def logout():
    s = request.environ.get('beaker.session')
    s.delete()
