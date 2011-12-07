<!doctype html>
<html lang="en">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />

    <title>{{ keyword }} - go spotty go</title>

    <link href='http://fonts.googleapis.com/css?family=Crafty+Girls|Give+You+Glory|The+Girl+Next+Door|Swanky+and+Moo+Moo|Gochi+Hand|Gloria+Hallelujah|Devonshire|Architects+Daughter|Over+the+Rainbow|Nothing+You+Could+Do|Indie+Flower|Annie+Use+Your+Telescope' rel='stylesheet' type='text/css'>
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
                <label for="keyword" class="infield">Search for keyword</label>
                <input type="text" name="keyword" id="keyword" maxlength="100" tabindex="1" value="{{ keyword }}"/>
              </li>
              <li>
                <input type="submit" value="Fetch »" tabindex="2"/>
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
              </tr>
              %end
            </tbody>
          </table>
          <div id="site-preview">
            <a class="title" href="#">{{ result[4] }}</a>
            <div class="url">{{ result[3] }}</div>
            <!--<img src="http://do.convertapi.com/web2image?curl={{result[3]}}">-->
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
