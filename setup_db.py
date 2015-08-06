# user 항목을 삭제하면, 그 아래 모든 book이 삭제되고, 그 아래 모든 story, story_data
# 가 삭제된다. ON DELETE CASCADE

# 책 정보
# story의 부모 역할
TBL_BOOK = (
    "CREATE TABLE book ("
    "num mediumint UNSIGNED AUTO_INCREMENT,"
    "user_num mediumint UNSIGNED NOT NULL,"
    "title varchar(255) NOT NULL,"
    "pub_date datetime default 0,"
    "mod_date datetime default 0 ON UPDATE CURRENT_TIMESTAMP,"
    "intro text,"
    "PRIMARY KEY(num),"
    "FOREIGN KEY (user_num) REFERENCES user(num) ON DELETE CASCADE"
    ")"
)

# 본문 정보
# story_data의 부모 테이블
TBL_STORY = (
    "CREATE TABLE story ("
    "num mediumint UNSIGNED AUTO_INCREMENT,"
    "book_num mediumint UNSIGNED NOT NULL,"
    "title varchar(255) NOT NULL,"
    "view_count mediumint UNSIGNED,"
    "like_count, mediumint UNSIGNED,"
    "pub_date datetime default 0,"
    "mod_date datetime default 0 ON UPDATE CURRENT_TIMESTAMP,"
    "PRIMARY KEY (num),"
    "FOREIGN KEY (book_num) REFERENCES book(num) ON DELETE CASCADE"
    ")"
)

# 본문 내용
# num은 story 테이블을 참조하는 외부 키.
# story에서 삭제 시, story_data 항목도 삭제됨.
TBL_STORY_DATA = (
    "CREATE TABLE story_data ("
    "num mediumint UNSIGNED NOT NULL,"
    "story mediumtext,"
    "FOREIGN KEY (num) REFERENCES story(num) ON DELETE CASCADE"
    ")"
)

# 사용자 정보
# password는 일단 보통 텍스트로 저장하고, 나중에 sha256을 적용할 것. (salt도 고려할 것)
# MySQL의 SHA2 함수 참고할 것.
TBL_USER = (
    "CREATE TABLE user ("
    "num mediumint UNSIGNED NOT NULL AUTO_INCREMENT,"
    "id varchar(20) NOT NULL,"
    # "password char(64) NOT NULL,"
    "password varchar(255) NOT NULL,"
    "name varchar(255) NOT NULL,"
    "email varchar(255),"
    "intro text,"
    "point mediumint UNSIGNED,"
    "level tinyint UNSIGNED DEFAULT 1,"
    "reg_date datetime default 0,"
    "log_date datetime default 0,"
    "PRIMARY KEY (num), UNIQUE (id)"
    ")"
)

# 태그 목록
TBL_TAGS = (
    "CREATE TABLE tags ("
    "num mediumint UNSIGNED AUTO_INCREMENT,"
    "tag varchar(255) NOT NULL,"
    "PRIMARY KEY (num)"
    ")"
)

# 책과 태그를 연결
TBL_TAGLIST = (
    "CREATE TABLE tag_list ("
    "book_num mediumint UNSIGNED,"
    "tag_num mediumint UNSIGNED,"
    "FOREIGN KEY (book_num) REFERENCES book(num) ON DELETE CASCADE,"
    "FOREIGN KEY (tag_num) REFERENCES tags(num) ON DELETE CASCADE"
    ")"
)
