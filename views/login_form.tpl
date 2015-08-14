% include('header.tpl', title=title)
    <div id="login">
      <div class="panel panel-default">
        <div class="panel-heading">
          <h3 class="panel-title">로그인</h3>
        </div>
        <div class="panel-body">
          <form id="form-login" method="post" action="{{action}}">
            <div class="form-group form-group-sm">
              <lable for="inputId" class="sr-only">아이디</lable>
              <input type="text" class="form-control" id="inputId" name="id" placeholder="아이디" />
            </div>  <!-- id -->
            <div class="form-group form-group-sm">
              <label for="inputPassword" class="sr-only">암호</label>
              <input type="password" class="form-control" id="inputPassword" name="password" placeholder="암호" />
            </div> <!-- password -->
            <div class="form-group form-group-sm">
              <div class="col-sm-6 col-remember">
                <div clss="checkbox">
                  <label>
                    <input type="checkbox" name="remember" checked="checked"> <span>기억하기</span>
                  </label>
                </div>
              </div>
              <div class="col-sm-6 col-btn">
                <button type="submit" class="btn btn-sm btn-primary">로그인</button>
              </div>
              <div class="clearfix"></div>
            </div>
          </form>
        </div> <!-- panel-body -->
      </div> <!-- panel -->
    </div>  <!-- #login -->
% include('footer.tpl')