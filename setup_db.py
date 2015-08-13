"""
    setup_db.py

    주의!
        테이블 생성 순서가 엉망이기 때문에, 외래키 제한을 맞추려면 2번 실행해야 함.

    TO-DOs:
        users나 books에서 한 항목을 삭제하면,
        연쇄적으로 하위 테이블이 삭제된다.
        다른 백업 DB로 옮기는 방법을 고안해보자.

        또는 사용자에게 삭제 권한 대신, 비공개 권한만 주는 건 어떨까?
"""

import mysql.connector as conn
from mysql.connector import errorcode
from config_db import *

TABLES = {}

# 책
# stories의 부모 역할
TABLES['books'] = (
    "CREATE TABLE books ("
    " num mediumint UNSIGNED AUTO_INCREMENT,"
    " user_num mediumint UNSIGNED NOT NULL,"
    " title varchar(255) NOT NULL,"
    " pub_date datetime default 0,"
    " mod_date datetime default 0 ON UPDATE CURRENT_TIMESTAMP,"
    " intro text,"
    " PRIMARY KEY(num),"
    " FOREIGN KEY (user_num) REFERENCES users(num) ON DELETE CASCADE"
    ")"
)

# 글
# 글에 대한 메타 데이터 저장
# story_data의 부모
TABLES['stories'] = (
    "CREATE TABLE stories ("
    " num mediumint UNSIGNED AUTO_INCREMENT,"
    " book_num mediumint UNSIGNED NOT NULL,"
    " title varchar(255) NOT NULL,"
    " view_count mediumint UNSIGNED,"
    " like_count mediumint UNSIGNED,"
    " pub_date datetime default 0,"
    " mod_date datetime default 0 ON UPDATE CURRENT_TIMESTAMP,"
    " PRIMARY KEY (num),"
    " FOREIGN KEY (book_num) REFERENCES books(num) ON DELETE CASCADE"
    ")"
)

# 글 내용
# 실제 글의 내용
# num은 stories 테이블을 참조하는 외부 키.
# stories에서 삭제 시, story_data의 해당 항목도 삭제됨.
TABLES['story_data'] = (
    "CREATE TABLE story_data ("
    " num mediumint UNSIGNED NOT NULL,"
    " story mediumtext,"
    " FOREIGN KEY (num) REFERENCES stories(num) ON DELETE CASCADE"
    ")"
)

# 사용자 정보
# password는 일단 보통 텍스트로 저장하고, 나중에 sha256을 적용할 것. (salt도 고려할 것)
# MySQL의 SHA2 함수 참고할 것.
# level 0은 관리자
TABLES['users'] = (
    "CREATE TABLE users ("
    " num mediumint UNSIGNED NOT NULL AUTO_INCREMENT,"
    " id varchar(20) NOT NULL,"
    # " password char(64) NOT NULL,"
    " password varchar(255) NOT NULL,"
    " name varchar(255) NOT NULL,"
    " email varchar(255),"
    " intro text,"
    " point mediumint UNSIGNED,"
    " level tinyint UNSIGNED DEFAULT 1,"
    " reg_date datetime default 0,"
    " log_date datetime default 0,"
    " PRIMARY KEY (num), UNIQUE (id)"
    ")"
)

# 태그 목록
TABLES['tags'] = (
    "CREATE TABLE tags ("
    " num mediumint UNSIGNED AUTO_INCREMENT,"
    " tag varchar(255) NOT NULL,"
    " PRIMARY KEY (num)"
    ")"
)

# 책과 태그를 연결
TABLES['tag_links'] = (
    "CREATE TABLE tag_links ("
    " book_num mediumint UNSIGNED,"
    " tag_num mediumint UNSIGNED,"
    " FOREIGN KEY (book_num) REFERENCES books(num) ON DELETE CASCADE,"
    " FOREIGN KEY (tag_num) REFERENCES tags(num) ON DELETE CASCADE"
    ")"
)


# ----- MAIN ----- #

# DB 접속
try:
    cnx = conn.connect(user=DB_USER, password=DB_PASSWORD,
                       host=DB_HOST, database=DB_NAME, port=DB_PORT)
except conn.Error as e:
    print("DB 접속 실패!: ", e.msg)
    exit()
else:
    cursor = cnx.cursor()

# 테이블 생성
for name, query in TABLES.items():
    try:
        print('테이블 {} 생성 중... '.format(name), end='')
        cursor.execute(query)
    except conn.Error as e:
        if e.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('이미 존재합니다!')
        else:
            print('실패했습니다! ({})'.format(e.msg))
    else:
        print('OK!')

cursor.close()
cnx.close()
