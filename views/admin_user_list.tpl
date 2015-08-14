% include('header.tpl', title=title)
      <div id="user-list">
        <h3>사용자 목록</h3>
        <table class="table table-condensed">
          <tr>
            <th>번호</th>
            <th>아이디</th>
            <th>사용자명</th>
            <th>이메일</th>
            <th>가입일</th>
            <th>-</th>
          </tr>
          % for u in ls:
          <tr>
            % for i in u:
            <td>{{i}}</td>
            % end
            <td>
              <a href="/admin/update_user?num={{u[0]}}">수정</a> |
              <a href="/admin/delete_user?num={{u[0]}}">탈퇴</a>
            </td>
          </tr>
          % end
        </table>
      </div>  <!-- user_list -->
% include('footer.tpl')