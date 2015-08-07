% include('header.tpl', title=title)
      <form name="newbook" method="post" action="">
        <table>
          <tr>
            <td>제목</td>
            <td><input type="text" name="b_title" /></td>
          </tr>
          <tr>
            <td>분류</td>
            <td>
              <input type="radio" name="b_type" value="short" /> 단편
              <input type="radio" name="b_type" value="series" checked="checked" /> 연재물
            </td>
          </tr>
          <tr>
            <td>공개</td>
            <td>
              <input type="radio" name="b_public" value="True" /> 공개
              <input type="radio" name="b_public" value="False" checked="checked" /> 비공개
            </td>
          </tr>
          <tr>
            <td>키워드</td>
            <td><input type="text" name="b_keywords" /></td>
          </tr>
          <tr>
            <td>작품 소개</td>
            <td>
              <textarea name="b_intro"></textarea>
            </td>
          </tr>
          <tr>
            <td rowspan="2">
              <input type="button" value="취소" />
              <input type="submit" value="저장" />
            </td>
          </tr>
        </table>
      </form>
% include('footer.tpl')