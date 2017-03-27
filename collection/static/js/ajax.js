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
	
});

function searchSuccess(data, textStatus, jqXHR) {
  $('#search-results').html(data);
}
