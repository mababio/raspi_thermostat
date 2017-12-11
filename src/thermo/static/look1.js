
$(function() {
var gradi = 65;
var max = 85;
var min = 65;

function updateGr(){
  $(".heat").text("" + gradi);
  $(".fill").css("animation", "none");
}



 (".minus").mousedown(function() {
     alert("Hello! I am an alert box!!");
      $.getJSON($SCRIPT_ROOT + '/handle', {
        control: $('.heat').text()
      }, function(data) {
        $(".heat").text(data.result);
      });
      return false;
    }
    );



$(".plus").mousedown(function(){
  if(gradi < max){
    gradi++;
    updateGr();
    $(".fill1").css("transform", "rotate("+ (gradi - 65) * 8 +"deg)").css("transition-delay", "0s");
  }
});
});

