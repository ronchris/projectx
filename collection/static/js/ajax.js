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
				button.parents(".reviewId").remove();
			}
		},
		error: function(error) {
				console.log(error.responseText)
			},
		});//end ajax
  }
  
  // add comment
  $(".comment--box--post").on("click", addComment);
	
  function addComment(e) {
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
	
  // delete comment
  $("body").on('click', ".delete_comment", deleteComment);
	
  function deleteComment(e) {
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
	
});

function searchSuccess(data, textStatus, jqXHR) {
  $('#search-results').html(data);
}
