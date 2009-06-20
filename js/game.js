/*global $ */

/*jslint bitwise: true, browser: true, eqeqeq: true, evil: true, forin: true, immed: true, newcap: true, nomen: true, plusplus: true, regexp: true, undef: true */

$(document).ready(function () {

    var moves;    
    
    function getSquare(x, y) {
	return $("#square" + x + "" + y);
    }
    
    function addPiece(type, color, x, y) {
	var div = '<div class="piece">' + '<img src="images/' + type + '.png" alt="' + type + '"/>' + '</div>';
	getSquare(x,y).append($(div));
    }

    function draginit() {

	for (var move in moves){
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
	    var selectedMoves = $(this).data("moves");
	    for(var i=0; i < selectedMoves.length; i += 1) {
		    getSquare(selectedMoves[i][0],selectedMoves[i][1]).droppable('enable');
	    }

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


    function setboard(json) {
	var boardState = eval('(' + json + ')');
	var pieces = boardState.positions;
	moves = boardState.moves;
	for (var x in pieces) {
	    addPiece(pieces[x] ,"", x[0], x[2]);
	}
	draginit();
    }

    var board = $("#board");
    for(var i=0; i < 10; i += 1) {
	for(var j = 0; j < 9; j += 1) {
	    var div = "<div id=square" + i + "" + j + " class='square'></div>";
	    $(div).appendTo(board).css("left",(70*j)+"px").css("top",(70*i)+"px");
	    
	}
    }
    
    // $("body").append(myMoves);
    // test();
    // $("body").append("test");
    // $("body").append(seven);

    $.getJSON("state.cgi?turn=b", setboard );
    
});
    
