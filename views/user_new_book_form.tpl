% include('header.tpl')
      <div id="user-new-book">
        <div class="panel panel-default">
          <div class="panel-heading">
            <h4 clas="panel-title">새 작품 등록</h4>
          </div>
          <div class="panel-body">
            <form id="form-new-book" method="post" action="/u/{{member['user_id']}}/newbook">

              <div class="form-group form-group-sm">
                <label class="radio-inline">
                  <input type="radio" name="is_novel" value="True">장편
                </label>
                <label class="radio-inline">
                  <input type="radio" name="is_novel" value="False" checked>단편
                </label>
              </div>

              <div class="form-group form-group-sm">
                <label for="inputBookname" class="sr-only">작품 제목</label>
                <input type="text" class="form-control" id="inputBookname" name="title" placeholder="작품 제목" />
              </div>

              <div class="form-group form-group-sm">
                <label for="inputKeywords" class="sr-only">키워드</label>
                <input type="text" class="form-control" id="inputKeywords" name="keywords" placeholder="키워드 (쉼표로 구분)" />
              </div>

              <div class="form-group form-group-sm">
                <label for="textareaBookintro" class="sr-only">작품 소개</label>
                <textarea class="form-control" rows="5" name="intro" placeholder="작품 소개"></textarea>
              </div>

              <div class="form-group form-group-sm">
                <label class="radio-inline">
                  <input type="radio" name="is_public" value="True">공개
                </label>
                <label class="radio-inline">
                  <input type="radio" name="is_public" value="False" checked>비공개
                </label>
              </div>

              <div class="form-group form-group-sm">
                <button type="submit" class="btn btn-sm btn-primary join-btn">작품 등록</button>
              </div>
              <div class="clearfix"></div>
            </form>
          </div>  <!-- panel-body -->
        </div>  <!-- panel -->
      </div> <!-- user-new-book -->
% include('footer.tpl')