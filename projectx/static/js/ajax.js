$(function() {
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
});

//function searchSuccess(data, textStatus, jqXHR) {
//  $('#search-results').html(data);
//}
//
//function deleteReview() {
//        $("body").on('click', "#delete", function(e){
//            e.preventDefault();
//            // get id from template
//            var reviewId = $('#reviewId').val();
//            $.ajax({
//                type: "GET",
//                url: "/delete/",
//                data: {'id': reviewId },
//                success: function(data) {
//                    if (data == "success") {
//
//                        $('#detailId').hide();
//  
//                    }
//                },
//                error: function(error) {
//                        console.log(error.responseText)
//                    },
//        });//end ajax
//    })//end
//}


$('#delete').on('click', function(event) {
  var del = $(this);
	
	console.log("this button wass clicked");

  // find all the checked box input and grab their value;

  var selected = [];
  $('.checkbox input:checked').each(function() {
	  selected.push($(this).attr('value'));
  });

  if (selected.length === 0) {
	alert('Nothing selected!!');
  } else {
	var response = confirm('Are you sure about this ?');
  }

  if (response == true) {
	  $.ajax({
		  type: "GET",
		  url: "/delete/",
		  select: selected,
		  data: { reviews: selected },
		  success: function(data){
			if (data === "success") {
			  this.select.forEach(function(item){
				  document.getElementById(item).remove();
			  })
			}
		  }
		})
  } else {
	  alert("No action was performed.");
  }
})


//$(document).ready(function(){
//  deleteReview();
//});
