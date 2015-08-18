% title = setdefault('title', '')
% logged = setdefault('logged', False)
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="content-type" content="text/html;chatset=utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{{title}}</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <link rel="stylesheet" href="/static/style.css" />
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
    <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <a href="/" class="navbar-brand">스토리보드</a>
        </div>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav navbar-right">
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false"><span class="glyphicon glyphicon-user"></span>
              % if logged:
              {{ member['user_name'] }}
              % else:
              사용자
              % end
                <span class="caret"></span>
              </a>
              <ul class="dropdown-menu">
              % if logged:
                <li><a href="/u/{{ member['user_id'] }}">내 페이지</a></li>
                <li><a href="/u/{{ member['user_id'] }}/update_info">정보 수정</a></li>
                <li><a href="/logout">로그아웃</a></li>
              % else:
                <li><a href="/join">계정 만들기</a></li>
                <li><a href="/login">로그인</a></li>
              % end
              </ul>
          </ul>
        </div>
      </div>
    </nav>
    <div class="container">
