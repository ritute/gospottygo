<!doctype html>
<html lang="en">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />

    <title>go spotty go / results</title>

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
                <input type="text" name="keyword" id="keyword" maxlength="" tabindex="1" value="{{ keyword }}"/>
              </li>
              <li>
                <input type="submit" value="Fetch »" tabindex="2"/>
              </li>
            </ul>
          </form>
        </div> <!--/search-box-->
        <div id="search-results">
          <table id="result-table">
            <thead>
                <tr>
                    <th></th>
                </tr>
            </thead>
            <tbody>
              %for i in range(val):
              <tr class="link">
                <td class="titlelink">
                  <a class="title" href="#"><b>JKL</b> Components Corporation</a>
                  <div class="url">www.jkllamps.com/</div>
                  <div class="description"><b>JKL</b> Components Corporation is a lighting solutions provider offering LED, fluorescent, incandescent and ultra-violet technologies. A wide assortment of ...</div>
                </td>
              </tr>
              %end
            </tbody>
          </table>
        </div> <!--/search-results-->
      </div> <!--/main-->
      <footer>
      </footer>
    </div> <!--/container-->

    <script type="text/javascript" src="http://code.jquery.com/jquery-1.6.4.min.js"></script>
    <script type="text/javascript" src="/static/vendor/jquery.infieldlabel.min.js"></script>
    <script type="text/javascript" src="/static/vendor/DataTables/jquery.dataTables.min.js"></script>
    <script type="text/javascript" src="/static/js/results.js"></script>
  </body>
</html>
