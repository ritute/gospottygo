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
    $('#result-table_paginate').find('span.paginate_button_disabled').hide();
    $('#result-table_paginate span').click(function(){
      if ($(this).hasClass('paginate_button_disabled'))
        $(this).hide();
      else
        $(this).show();
    });
}

$(function(){
  $('label.infield').inFieldLabels();
  configTable();
});