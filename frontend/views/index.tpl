<!DOCTYPE html>

<html lang="en">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <title>Search Engine</title>
    <link rel="stylesheet" type="text/css" href="{{ get_url('static', path='main.css') }}"/>
  </head>
  <body>
    <div id="container">
      <div id="header">
        <h1>Search Engine Home</h1>
      </div> <!-- /header -->
      <div id="content">
        <form id="search-box" method="get" action="">
          <label for="keyword">Search for keyword:</label>
          <input type="text" name="keyword" id="keyword"/>
          <input type="submit" id="search" value="Search"/>
        </form>
      </div> <!-- /content -->
      <div id="footer">
      </div> <!-- /footer -->
    </div> <!-- /container -->
    
    <script type="text/javascript" src=""></script>

    <script type="text/javascript">
      $(function(){
        $('#submit').click(function(){
          alert('Searching!');
        });
      });
    </script>
  </body> 
</html>