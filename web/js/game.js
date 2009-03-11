$(document).ready(function () {

    function getSquare(x, y) {
	return $("#square" + x + "" + y);
    }
    
    function addPiece(type, color, x, y) {
	s = '<div class="piece ' + type + '">' + '<img src="images/' + type + color  + '.png" alt="' + type + '"/>' + '</div>';
	getSquare(x,y).append($(s));
    }
    
    

    var board = $("#board");
    for(i=0;i<9;i+=1){
	for(j=0;j<10;j+=1){
	    s = "<div id=square" + i + "" + j + " class='square'></div>";
	    $(s).appendTo(board).css("left",(70*j)+"px").css("top",(70*i)+"px");
	    
	}
    }
    
    //    $(".square").each(function (i) {
    //	$(this).text($(this).data("index").x + "," + $(this).data("index").y);
    //   });
    

    addPiece("advisor","black",3,6);
    addPiece("rook","black",0,0);

    $(".piece").addClass("draggable");
    
    //    getSquare(6,7).addClass("droppable");
    //    getSquare(1,1).addClass("droppable");
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

    
});
    
