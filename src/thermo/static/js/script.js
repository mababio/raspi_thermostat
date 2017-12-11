$(document).ready(function() {
    $('#up').bind('click', function() {
      $.getJSON($SCRIPT_ROOT +'/handle', {
        control: $('#up').text()
      }, function(data) {
        $("h1").text(data.result);
      });
      return false;
    }
    );

     $('#down').bind('click', function() {
      $.getJSON($SCRIPT_ROOT + '/handle', {
        control: $('#down').text()
      }, function(data) {
        $("h1").text(data.result);
      });
      return false;
    }
    );

    $('#submit_time').bind('click', function() {
      $.getJSON(window.location.host+ '/setsch', {
        time: $('#temp_time').val(),
        temp: $('#temp_val').val()
      }, function(data) {
        alert("temp set!!!!");
      });
      return false;
    }
    );
}
);
