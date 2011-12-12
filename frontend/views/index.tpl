<!doctype html>
<html lang="en">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />

    <title>go spotty go</title>
    <link rel="stylesheet" type="text/css" href="/static/stylesheets/index.css">
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
          <h1>go spotty go</h1>
        </div>
        <div id="search-box">
          <form method="GET" action="/results">
            <ul>
              <li>
                <label for="keyword" class="infield">What word are you looking for?</label>
                <input type="text" name="keyword" id="keyword" maxlength="100" tabindex="1"/>
              </li>
              <li class="action">
                <input type="submit" class="red-button" value="Fetch »" tabindex="2"/>
              </li>
            </ul>
          </form>
        </div> <!--/search-box-->
      </div> <!--/main-->
      <footer>
      </footer>
    </div> <!--/container-->
    
    <script type="text/javascript" src="http://code.jquery.com/jquery-1.6.4.min.js"></script>
    <script type="text/javascript" src="/static/vendor/jquery.infieldlabel.min.js"></script>
    <script type="text/javascript" src="/static/js/index.js"></script>
    <script type="text/javascript">

      var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-27674636-1']);
      _gaq.push(['_trackPageview']);

      (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
      })();

    </script>
  </body>
</html>
