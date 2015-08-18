% include('header.tpl', title=title)
      <div id="user-info-update">

        <div class="panel panel-default">
          <div class="panel-heading">
            <h3 class="panel-title">회원 정보 수정</h3>
          </div>
          <div class="panel-body">
            <form id="form-user-info" method="post" action="/u/{{info['id']}}/update_info">
              <div class="form-group form-group-sm">
                <label for="inputId" class="sr-only">아이디</label>
                <input type="text" class="form-control" id="inputId" name="id" placeholder="{{info['id']}}" disabled />
              </div>
              <div class="form-group form-group-sm">
                <label for="inputName" class="sr-only">사용자명</label>
                <input type="text" class="form-control" id="inputName" name="name" value="{{info['name']}}" placeholder="사용자명" />
              </div>
              <div class="form-group form-group-sm">
                <label for="inputEmail" class="sr-only">이메일 주소</label>
                <input type="mail" class="form-control" id="inputEmail" name="email" value="{{info['email']}}" placeholder="이메일 주소" />
              </div>
              <div class="form-group form-group-sm">
                <label for="inputPassword" class="sr-only">로그인 암호</label>
                <input type="password" class="form-control" id="inputPassword" name="password" placeholder="로그인 암호" />
              </div>
              <div class="form-group form-group-sm">
                <label for="inputPassword2" class="sr-only">로그인 암호 확인</label>
                <input type="password" class="form-control" id="inputPassword2" name="password2" placeholder="로그인 암호 확인" />
              </div>
              <div class="form-group form-group-sm">
                <label for="textareaIntro" class="sr-only">사용자 소개</label>
                <textarea class="form-control" rows="4" name="intro" placeholder="사용자 소개">{{info['intro']}}</textarea>
              </div>
              <div class="form-group form-group-sm">
                <button type="submit" class="btn btn-sm btn-primary join-btn">정보 갱신</button>
                <div class="clearfix"></div>
              </div>
            </form>
          </div>  <!-- panel-body -->
        </div>  <!-- panel -->



      </div>
% include('footer.tpl')