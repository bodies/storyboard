"""
    member.py

    클래스 Member: 사용자 관리 DB 작업 처리

    TO-DOs:
        DB 에러(예) 발생 시, 깔끔한 처리 방법?
"""

import mysql.connector as conn
from config_db import *


class Member:

    cnx = None
    cur = None

    def __init__(self):
        try:
            self.cnx = conn.connect(
                user=DB_USER, password=DB_PASSWORD, database=DB_NAME,
                host=DB_HOST, port=DB_PORT, charset='utf8')
            self.cur = self.cnx.cursor()
        except:
            raise

    def __del__(self):
        self.cur.close()
        self.cnx.close()

    def login(self, id, passwd):
        # 정보가 맞으면 사용자 번호, 아이디, 별명, 등급을 리스트로 반환
        # 안 맞으면, 빈 리스트 반환
        try:
            self.cur.execute(
                "SELECT num, id, name, level FROM users \
                WHERE id=%s AND password=%s \
                LIMIT 1", (id, passwd)
            )
            return self.cur.fetchone()
        except Exception as e:
            print('DB ERROR: ', e)
            raise

    def register(self, id, name, email, passwd, admin=False):
        level = 1 if not admin else 0
        print(id, name, email, passwd, level)
        try:
            self.cur.execute(
                "INSERT INTO users (id, name, email, password, level, reg_date) VALUES \
                (%s, %s, %s, %s, %s, NOW())", (id, name, email, passwd, level)
            )
            self.cnx.commit()
        except:
            raise

    def update(self, num, **data):
        # name, email, password 변경
        # TO-DOs: 비번을 확인해야 하나?
        try:
            set_str = []
            for k in ('name', 'email', 'password'):
                if k in data:
                    set_str.append('{}={}'.format(k, data[k]))

            if not set_str:
                raise Exception

            self.cur.execute(
                'UPDATE users SET {} WHERE num={} LIMIT 1'.format(
                    ','.join(set_str), num
                )
            )
        except:
            return False
        else:
            return True

    def remove(self, num):
        # 실수로 인한 삭제를 방지할 방법? (사용자 번호와 아이디 확인 체크?)
        # 사용자가 이미 없을 경우, 삭제를 실패하면
        try:
            self.cur.execute('DELETE FROM users WHERE num=%s LIMIT 1', (num,))
        except:
            raise

    def extra_info(self, id):
        # 세션에 저장된 것 이오의 사용자 정보를 반환
        try:
            self.cur.execute('SELECT email, intro FROM users WHERE id=%s LIMIT 1', (id,))
            result = self.cur.fetchall()
            return result[0]
        except:
            print('ERROR in extra_info')
            raise

    def _is_duplicated(self, col, value):
        # TODO: 예외 발생 시 처리 방법
        query = 'SELECT EXISTS (SELECT 1 FROM users WHERE {}=%s LIMIT 1)'.format(col)
        print(query)
        try:
            self.cur.execute(query, (value,))
            result = self.cur.fetchone()
            return result[0]
        except Exception as e:
            print(e.args[0])
            raise

    def has_id(self, id):
        return self._is_duplicated('id', id)

    def has_email(self, email):
        return self._is_duplicated('email', email)

    def has_name(self, name):
        return self._is_duplicated('name', name)

    def list(self):
        # 테스트 용
        # 사용자 목록 + 사용자 삭제 링크 출력
        try:
            self.cur.execute('SELECT num, id, name, email, reg_date FROM users')
            return self.cur.fetchall()
            # print(self.cur.fetchall())
        except:
            raise
