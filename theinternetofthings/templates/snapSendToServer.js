// Send photo with ajax
$(document).ready(function() {

   $("#snap").click(function() {
      var canvas = document.getElementById('canv');
      var dataURL = canvas.toDataURL();
      $.ajax({
         type: "POST",
         url: "/capture",
         data: { img: dataURL }
      }).done(function(msg){
         alert(msg);
      });
   });

});
