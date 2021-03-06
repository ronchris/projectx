$(document).ready(function(){
 
  console.log("ajax file");
	
  // search results
  $('#destination-search').keyup(function() {
    $.ajax({
		type: 'GET',
		url: '/search/',
		data: {
			'q': $('#destination-search').val(),
			'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
		},
		success: searchSuccess,
		dataType: 'html'
	});
  });
  
  // delete review
  $("body").on('click', ".delete_review", deleteReview);
	
  function deleteReview(e) {
	e.preventDefault();
	var button = $(this);
	console.log(button);
	var reviewId = button.attr("data-reviewId");
	console.log(reviewId);
	// get id from template
	$.ajax({
		type: "GET",
		url: "/profiles/delete_review/",
		data: {'reviewId': reviewId },
		success: function(data) {
			console.log(data);
			if (data && data.status == "success") {
				$("#" + reviewId).remove();
			}
		},
		error: function(error) {
				console.log(error.responseText)
			},
		});//end ajax
  }
  
  // delete question
  $("body").on('click', ".delete_question", deleteQuestion);
	
  function deleteQuestion(e) {
	e.preventDefault();
	var button = $(this);
	console.log(button);
	var questionId = button.attr("data-questionId");
	console.log(questionId);
	// get id from template
	$.ajax({
		type: "GET",
		url: "/profiles/delete_question/",
		data: {'questionId': questionId },
		success: function(data) {
			console.log(data);
			if (data && data.status == "success") {
				button.parents(".questionId").remove();
			}
		},
		error: function(error) {
				console.log(error.responseText)
			},
		});//end ajax
  }
	
  // add comment to review
  $(".comment--box--post").on("click", addCommentToReview);
	
  function addCommentToReview(e) {
	console.log("i am clicked")
	e.preventDefault();
	var button = $(this);
	var commentForm = button.prev('.comment-form');
	console.log(commentForm)
	if (!commentForm) return;
	var text = commentForm.find('textarea').val();
	  if (!text || !text.trim()) {
		  // $(".comment-error").html("Please enter a comment.");
		  button.next().html("Please enter a comment.");
	  }
	 var form  = commentForm.parent();
	 var uri = form.attr('action');
	 console.log(uri.split('/'))
	 console.log(uri.split('/')[4]);
	 reviewId = Number(uri.split('/')[4]);
	 destinationId = Number(uri.split('/')[2]);
	 console.log(reviewId);
	 console.log(text)
	 var commentId = button.attr("data-commentId");
	 // console.log(reviewId);
	 // get id from template
	$.ajax({
		type: "GET",
		url: "/destinations/" + destinationId + "/add_comment_to_review/" + reviewId,
		beforeSend: function(xhr, settings) {
			//if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            	xhr.setRequestHeader("X-CSRFToken", $('input[name=csrfmiddlewaretoken]').val());
        	//}//
    	},
		data: {'reviewId': reviewId,  'destinationId': destinationId, text: text},
		success: function(data) {
			console.log(data);
			console.log(data.message.datetime);
			var id = "#review-" + reviewId;
			if (data && data.status == "success") {
				var html = 	'<div class="comment--text" id="comment-' + 
								  data.message.id + '">';
				html += ' <img class="comment--profile--img" src="';
				html += data.message.image;
				html += '"height="45" width="45" />';
				html += '<p>' + data.message.text + '</p>';
				html += '<p> commented by ' + data.message.username + '</p>';
				html += '<p> commented on ' + moment(data.message.datetime).format('LLL'); + '</p>';
				html += '<br><br><a class="delete_comment" data-commentId="' + data.message.id + '">'
				html += 'Delete</a>';
				html += '</div>';
									
				$(id).append(html); 
				$('textarea').val("");
			}
		},
		error: function(error) {
			
		},
     });//end ajax
  }

  // add comment to question
  $(".comment--box--submit").on("click", addCommentToQuestion);
	
  function addCommentToQuestion(e) {
	console.log("i am clicked")
	e.preventDefault();
	var button = $(this);
	var commentQForm = button.prev('.commentq-form');
	console.log(commentQForm)
	if (!commentQForm) return;
	var text = commentQForm.find('textarea').val();
	  if (!text || !text.trim()) {
		  // $(".comment-error").html("Please enter a comment.");
		  button.next().html("Please enter a comment.");
	  }
	 var form  = commentQForm.parent();
	 var uri = form.attr('action');
	 console.log(uri.split('/'))
	 console.log(uri.split('/')[4]);
	 questionId = Number(uri.split('/')[4]);
	 destinationId = Number(uri.split('/')[2]);
	 console.log(questionId);
	 console.log(text)
	 var commentQId = button.attr("data-commentQId");
	 // console.log(reviewId);
	 // get id from template
	$.ajax({
		type: "GET",
		url: "/destinations/" + destinationId + "/add_comment_to_question/" + questionId,
		beforeSend: function(xhr, settings) {
			//if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            	xhr.setRequestHeader("X-CSRFToken", $('input[name=csrfmiddlewaretoken]').val());
        	//}//
    	},
		data: {'questionId': questionId,  'destinationId': destinationId, text: text},
		success: function(data) {
			console.log(data);
			console.log(data.message.datetime);
			var id = "#question-" + questionId;
			if (data && data.status == "success") {
				var html = 	'<div class="comment--text" id="commentQ-' + 
								  data.message.id + '">';
				html += ' <img class="comment--profile--img" src="';
				html += data.message.image;
				html += '"height="45" width="45" />';
				html += '<p>' + data.message.text + '</p>';
				html += '<p> commented by ' + data.message.username + '</p>';
				html += '<p> commented on ' + moment(data.message.datetime).format('LLL'); + '</p>';
				html += '<br><br><a class="delete_commentq" data-commentQId="' + data.message.id + '">'
				html += 'Delete</a>';
				html += '</div>';
									
				$(id).append(html); 
				$('textarea').val("");
			}
		},
		error: function(error) {
			
		},
     });//end ajax
  }
	
  // delete comment
  $("body").on('click', ".delete_comment", deleteComment);
	
  function deleteComment(e) {
//	return console.log($(this));
	e.preventDefault();
	var button = $(this);
	console.log(button);
	var commentId = button.attr("data-commentId");
	console.log(commentId);
	// get id from template
	$.ajax({
		type: "GET",
		url: "/profiles/delete_comment/",
		data: {'commentId': commentId },
		success: function(data) {
			console.log(data);
			var id = "#comment-" + commentId;
			console.log(id);
			console.log($(id))
			if (data && data.status == "success") {
				$(id).remove();
				console.log("comment removed");
			}
		},
		error: function(error) {
				console.log(error.responseText);
			},
		});//end ajax
   }
	
   // delete comment
  $("body").on('click', ".delete_commentq", deleteCommentQ);
	
  function deleteCommentQ(e) {
//	return console.log($(this));
	e.preventDefault();
	var button = $(this);
	console.log(button);
	var commentQId = button.attr("data-commentQId");
	console.log(commentQId);
	// get id from template
	$.ajax({
		type: "GET",
		url: "/profiles/delete_commentq/",
		data: {'commentQId': commentQId },
		success: function(data) {
			console.log(data);
			var id = "#commentQ-" + commentQId;
			console.log(id);
			console.log($(id))
			if (data && data.status == "success") {
				$(id).remove();
				console.log("comment removed");
			}
		},
		error: function(error) {
				console.log(error.responseText);
			},
		});//end ajax
   }
	
	// like/dislikes
	$("body").on('click', ".likes", likedislikeRequest);
	
	function likedislikeRequest() {
		var likesCount = $(this).data("rid");
		var colorButton = $(this).css('color');
		console.log(colorButton);
		if (colorButton == 'rgb(128, 128, 128)') {
			console.log("sending the like ajax request");
			$.ajax({
				type: "GET",
				url: "/destinations/" + $(this).data('did') + "/add_like_to_review/" + $(this).data('rid'),
				success: function (e) {
					console.log(e);

					console.log(likesCount);
					$('.likes--count').filter("[data-prid=" +likesCount+"]").text(e.likes);
					$('.likes').filter("[data-rid=" +likesCount+"]").css("color", "#a2db68");
				}
			});
		}
		else {
			console.log("sending the dislike ajax request");
			$.ajax({
				type: "GET",
				url: "/destinations/" + $(this).data('did') + "/add_dislike_to_review/" + $(this).data('rid'),
				success: function (e) {
					console.log(e);

					console.log(likesCount);
					$('.likes--count').filter("[data-prid=" +likesCount+"]").text(e.likes);
					$('.likes').filter("[data-rid=" +likesCount+"]").css("color", "gray");
				}
			});
		}
	};
	
	// saves/unsaves
	$("body").on('click', ".saves", saveUnsaveRequest);
	
	function saveUnsaveRequest() {
		var colorButton = $(this).css('background-color');
		console.log(colorButton);
		if (colorButton == 'rgb(128, 128, 128)') {
			console.log("sending the save ajax request");
			$.ajax({
				type: "GET",
				url: "/destinations/" + $(this).data('did') + "/save_destination/",
				success: function (e) {
					console.log(e);
					$('.saves').css("background-color", "#a2db68");
				}
			});
		}
		else {
			console.log("sending the unsave ajax request");
			$.ajax({
				type: "GET",
				url: "/destinations/" + $(this).data('did') + "/unsave_destination/",
				success: function (e) {
					console.log(e);
					$('.saves').css("background-color", "gray");
				}
			});
		}
	};
	
});

function searchSuccess(data, textStatus, jqXHR) {
  $('#search-results').html(data);
}
