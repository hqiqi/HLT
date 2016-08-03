function refresh() {
$.ajax({
  url: 'http://127.0.0.1:8000/indicators/MADdash/',
  success: function(data) {
  $('#q').html(data);
  }
});
};
$(function(){
    refresh();
    var int = setInterval("refresh()", 10000);
});