//------------------------------------------------------------------------------
//  SEARCH RESULT TABLE CONFIGURATION
//------------------------------------------------------------------------------
function configTable() {
    var oTable = $('#result-table').dataTable({
      "sPaginationType": "full_numbers",
      "bLengthChange": false,
      "bFilter": false,
      "bSort": false,
      "bInfo": false,
    });
    
    // Filter search results
    // $('#keyword').keyup(function(){
    //   oTable.fnFilter(this.value, 0);
    // });

    // Make entire table row clickable
    $('tr').click(function() {
      var href = $(this).find("a").attr("href");
      if (href) window.location = href;
    });
    
    // Bottom pagination fixups
    $('#result-table_previous').text('Prev');
    // $('#result-table_paginate').find('span.paginate_button_disabled').hide();
    // $('#result-table_paginate span').click(function(){
    //   if ($(this).hasClass('paginate_button_disabled'))
    //     $(this).hide();
    //   else
    //     $(this).show();
    // });
    
    $('tr').hover(function(){
        $(this).find('td.preview-arrow').show();
    }, function(){
        $(this).find('td.preview-arrow').hide();
    });
    
    function getPreview(href) {
        
        $.ajax({
            type: "POST",
            dataType: 'jsonp',
            url: 'http://do.convertapi.com/Web2Image/json/',
            data: {
                'CUrl': href,
                'OutputFormat': 'png',
                'PageWidth': 600
            },
            jsonp: "callback",
            success: function(data) {
                if (data.Result) {
                    $('#site-preview img').attr('src', 'data:image/png;base64,'+data.File);
                    $('div.loader').hide();
                } else {
                    console.log("Error in retrieving preview image!");
                }
            }
        });
        
        
        $("#site-preview img").click(function(){
           window.location = href; 
        });
    }
    
    inPreview = false;
    
    function showPreview($tr) {
        $('#site-preview').show();
        href = $tr.find('a.title').attr('href');
        $('#site-preview').find('a.title').text( $tr.find('a.title').text() );
        $('#site-preview').find('a.title').attr('href', href);
        $('#site-preview').find('div.url').text(href);
        $('#site-preview').hover(function(){
            inPreview = true;
        }, function(){
            inPreview = false;
        });
        getPreview(href);
    }
    
    $('td.preview-arrow').hover(function(){
        $(this).addClass('active');
        showPreview($(this).parent());
    }, function(){
        if (!inPreview)
            $(this).removeClass('active');
        //$('#site-preview').hide();
    });
}

$(function(){
  $('label.infield').inFieldLabels();
  configTable();
});