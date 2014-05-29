$(document).ready(function() {
      $('body').dblclick(function(){
      var life = setInterval(function() 
      {
          var extinct = true;
          $.getJSON('http://127.0.0.1:5000/live', function(data, textStatus, jqXHR) 
               {
                    var world = data;
                    var population_multi = Object.keys(world).length;
                    cells = document.getElementsByClassName('block');
                    for (var i=0; i < cells.length; i++){
                      cells[i].style.backgroundColor = 'white';
                    };
                    
                    for ( var x = 0; x < population_multi; x++){
                      for ( var y = 0; y < population_multi; y++){
                        if (world[x][y] == 1) {
                          extinct = false;                          
                          cell = document.getElementsByClassName('block-cont')[y].getElementsByClassName('block')[x];
                          cell.style.backgroundColor = 'black';
                        };  
                      };
                    };
                    if (extinct == true)
                    {
                         clearInterval(life);
                    }
               });          
     }, 2000);
      });
});