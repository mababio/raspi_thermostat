
$(function() {
var gradi = 65;


function updateGr(data){
     $(".heat").text(data.result);
     $(".fill").css("animation", "none");
     $(".fill1").css("transform", "rotate("+ ($(".heat").text() - 65) * 8 +"deg)").css("transition-delay", "0s");
}


$(".minus").mousedown(function(){
  $.getJSON($SCRIPT_ROOT + '/handle', {
        control: 'DOWN'
      }, function(data) {
            updateGr(data)
      });
});

$(".plus").mousedown(function(){
  $.getJSON($SCRIPT_ROOT + '/handle', {
        control: 'UP'
      }, function(data) {
            updateGr(data)
      });
});



});

