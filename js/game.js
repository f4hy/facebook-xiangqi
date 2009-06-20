$(document).ready(function () {


    function getSquare(x, y) {
	return $("#square" + x + "" + y);
    }
    
    function addPiece(type, color, x, y) {
	s = '<div class="piece">' + '<img src="images/' + type + '.png" alt="' + type + '"/>' + '</div>';
	getSquare(x,y).append($(s));
    }

    var moves;    
    
    function setboard(json) {
	var boardState = eval('(' + json + ')');
	var pieces = boardState["positions"];
	moves = boardState["moves"];
	for (x in pieces){
	    addPiece(pieces[x],"",x[0],x[2]);
	}
	draginit();
    }


    
    function parsemoves(json) {
	myMoves = eval('(' + json + ')');
	// for (move in myMoves){
	//     getSquare(move[0],move[2]).css({background:"orange"});
	// }
	seven = 8;
	return false;
    }

    var board = $("#board");
    for(i=0;i<10;i+=1){
	for(j=0;j<9;j+=1){
	    s = "<div id=square" + i + "" + j + " class='square'></div>";
	    $(s).appendTo(board).css("left",(70*j)+"px").css("top",(70*i)+"px");
	    
	}
    }
    
    //    $(".square").each(function (i) {
    //$(this).text($(this).data("index").x + "," + $(this).data("index").y);
    //   });

    // $.getJSON("moves.cgi", parsemoves );

    // function test() {
    // 	seven = 4;
    // }

    // $("body").append(myMoves);
    // test();
    // $("body").append("test");
    // $("body").append(seven);

    $.getJSON("state.cgi", setboard );

    function draginit() {

	for (move in moves){
            getSquare(move[0],move[2]).children(".piece").addClass("draggable");
	    getSquare(move[0],move[2]).children().data("moves",moves[move]);
	}

	$(".square").addClass("droppable");

	$(".droppable").bind('dropover',function () { $(this).css({background:"green"}); });
	$(".draggable").draggable({cursor: 'move', revert: "invalid", containment : "#board"});
	$('.draggable').bind('dragstart', function (event, ui) {
	    // $("body").append( $(this).data("moves") );
	    // $("body").append( "omg");

	    $(".square").droppable('disable');
	    var tmp = $(this).data("moves")
	    getSquare(tmp[0][0],tmp[0][1]).droppable('enable');
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
    
