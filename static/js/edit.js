$(document).ready(function() {
    $('#summernote').summernote();
});
$("#click").click(function(){
    var st = $('#summernote').code();
    alert(st);
});