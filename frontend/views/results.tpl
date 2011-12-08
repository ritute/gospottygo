<!doctype html>
<html lang="en">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />

    <title>{{ keyword }} - go spotty go</title>

    <link rel="stylesheet" type="text/css" href="/static/stylesheets/results.css">
  </head>

  <body>
    <div id="container">
      <header>
      </header>
      <div id="about">
        <a href="/about"></a>
      </div>
      <div id="main" role="main">
        <div id="logo">
          <a href="/">go spotty go</a>
        </div>
        <div id="search-box">
          <form method="GET" action="#">
            <ul>
              <li>
                <label for="keyword" class="infield">What are you looking for?</label>
                <input type="text" name="keyword" id="keyword" maxlength="100" tabindex="1" value="{{ keyword }}"/>
              </li>
              <li>
                <input type="submit" class="red-button" value="Fetch" tabindex="2"/>
              </li>
            </ul>
          </form>
        </div> <!--/search-box-->
        <div id="search-results">
          <div id="search-time">
            %if len(results)>1:
              Fetched {{len(results)}} results ({{time}} seconds)
            %elif len(results)==1:
              Fetched 1 result ({{time}} seconds)
            %else:
              No results found!
            %end
          </div> <!--/search-time-->
          <table id="result-table">
            <thead>
                <tr>
                    <th></th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
              %for result in results:
              <tr class="link">
                <td class="titlelink">
                  <a class="title" href="{{result[3]}}">{{ result[4] }}</a>
                  <div class="url">{{ result[3] }}</div>
                  <div class="description">{{ result[5] }}</div>
                </td>
                <td class="preview-arrow"><div class="wrapper"><div class="arrow"></div></div></td>
              </tr>
              %end
            </tbody>
          </table>
          <div id="site-preview">
            <a class="title" href=""></a>
            <div class="url"></div>
            <div class="loader"></div>
            <img src="">
          </div> <!--/site-preview-->
        </div> <!--/search-results-->
      </div> <!--/main-->
      <footer>
      </footer>
    </div> <!--/container-->
    <div id="line"></div>
    
    <script type="text/javascript" src="http://code.jquery.com/jquery-1.6.4.min.js"></script>
    <script type="text/javascript" src="/static/vendor/jquery.infieldlabel.min.js"></script>
    <script type="text/javascript" src="/static/vendor/DataTables/jquery.dataTables.min.js"></script>
    <script type="text/javascript" src="/static/js/results.js"></script>
  </body>
</html>
