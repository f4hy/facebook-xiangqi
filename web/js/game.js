$(document).ready(function () {

    function getSquare(x, y) {
	return $("#square" + x + "" + y);
    }
    
    function addPiece(type, color, x, y) {
	s = '<div class="piece">' + '<img src="images/' + type + color  + '.png" alt="' + type + '"/>' + '</div>';
	getSquare(x,y).append($(s));
    }
    
    
    function setboard(json) {
	//
	addPiece("\u8eca","",3,1);
	var myObject = eval('(' + json + ')');
	for (x in myObject){
	    // addPiece(myObject[x],"",x[0],x[2]);
	    addPiece(myObject[x],"",x[0],x[2]);
	}
	draginit();
    }
    


    var board = $("#board");
    for(i=0;i<10;i+=1){
	for(j=0;j<9;j+=1){
	    s = "<div id=square" + i + "" + j + " class='square'></div>";
	    $(s).appendTo(board).css("left",(70*j)+"px").css("top",(70*i)+"px");
	    
	}
    }
    
    //    $(".square").each(function (i) {
    //	$(this).text($(this).data("index").x + "," + $(this).data("index").y);
    //   });
    
    $.getJSON("json.html", setboard );
    

    function draginit() {


	$(".piece").addClass("draggable");
	$(".square").addClass("droppable");

	$(".droppable").bind('dropover',function () { $(this).css({background:"green"}); });
	$(".draggable").draggable({cursor: 'move', revert: "invalid", containment : "#board"});
	$('.draggable').bind('dragstart', function (event, ui) {
	    if( $(this).hasClass('rook') ) {
		$(".square").droppable('disable');
		getSquare(1,2).droppable('enable');
	    }
	});

	$(".droppable").droppable( {
	    drop: function(event, ui) { $(this).css({background:"red"}); 
					$(this).empty();
					$(this).append(ui.draggable);
					ui.draggable.css({left:"0px"}); 
					ui.draggable.css({top:"0px"}); 
				      }
	});
    }
    
});
    
