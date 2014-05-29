$(document).ready(function() {
  $('.block').click(function(){
      var $this = $(this);
      if($(this).css("background-color") === "rgb(128, 128, 128)")
     {
      var x = $(this).index();
      var y = $(this).parent().index()-1;
      dic = {"x":x,"y":y};
      console.log(dic)      
      $.post("http://127.0.0.1:5000/start",dic ,
        function(data)
      {
        $this.css("background-color", "white");
      })
     }
     else
     {
      var x = $(this).index();
      var y = $(this).parent().index()-1;
      dic = {"x":x,"y":y};
      console.log(dic)      
      $.post("http://127.0.0.1:5000/start",dic ,
        function(data)
      {
        $this.css("background-color", "grey");
      })
     }
     }
  );
});