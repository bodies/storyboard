% include('header.tpl', title=title)
      <div id="join">
        <div class="panel panel-default">
          <div class="panel-heading">
            <h3 class="panel-title">회원 가입</h3>
          </div>
          <div class="panel-body">
            <form id="form-join" method="post" action="/join" accept-charset="utf-8">
              <div class="form-group form-group-sm">
                <label for="inputId" class="sr-only">아이디</label>
                <input type="text" class="form-control" id="inputId" name="id" placeholder="아이디" />
              </div>
              <div class="form-group form-group-sm">
                <label for="inputName" class="sr-only">사용자명</label>
                <input type="text" class="form-control" id="inputName" name="name" placeholder="사용자명" />
              </div>
              <div class="form-group form-group-sm">
                <label for="inputEmail" class="sr-only">이메일 주소</label>
                <input type="mail" class="form-control" id="inputEmail" name="email" placeholder="이메일 주소" />
              </div>
              <div class="form-group form-group-sm">
                <label for="inputPassword" class="sr-only"></label>
                <input type="password" class="form-control" id="inputPassword" name="password" placeholder="로그인 암호" />
              </div>
              <div class="form-group form-group-sm">
                <label for="inputPassword2" class="sr-only"></label>
                <input type="password" class="form-control" id="inputPassword2" name="password2" placeholder="로그인 암호 확인" />
              </div>
              <div class="form-group form-group-sm">
                <button type="submit" class="btn btn-sm btn-primary join-btn">회원 등록</button>
                <div class="clearfix"></div>
              </div>
            </form>
          </div>  <!-- panel-body -->
        </div>  <!-- panel -->
      </div>  <!-- #join -->
% include('footer.tpl')