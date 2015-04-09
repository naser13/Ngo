$(document).ready(function() {
    $('#summernote').summernote();
});
$("#click").click(function(){
    var st = $('#summernote').code();
    alert("sending")
    $.get('http://127.0.0.1:8000/new',function(){
        alert('sent');
    })
});
$('#submit').click(function(){

});