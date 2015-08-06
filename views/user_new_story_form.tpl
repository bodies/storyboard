% include('header.tpl', title=title)
      <form name="newstory" method="post" action="">
        <table>
          <tr>
            <td>소제목</td>
            <td><input type="text" name="story_name" /></td>
          </tr>
          <tr>
            <td>본문</td>
            <td>
              <textarea name="story_story"></textarea>
            </td>
          </tr>
          <tr>
            <td>공개</td>
            <td>
              <input type="radio" name="s_public" value="True" /> 공개
              <input type="radio" name="s_public" value="False" checked="checked" /> 비공개
            </td>
          </tr>
          <tr>
            <td rowspan="2">
              <input type="button" value="취소" />
              <input type="submit" value="등록" />
        </table>
      </form>
% include('footer.tpl')