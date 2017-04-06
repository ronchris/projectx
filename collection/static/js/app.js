$(document).ready(function(){
	
	// prevent enter submission 
	$(document).on('keyup keypress', 'form input[type="text"]', function(e) {
		if(e.which == 13) {
			e.preventDefault();
			return false;
  		}
	});

	// responsive carousel/slider plugin
	$('.destination-slides').slick({
	  dots: true,
	  infinite: false,
	  speed: 300,
	  slidesToShow: 2,
	  slidesToScroll: 2,
	  responsive: [
		{
		  breakpoint: 1024,
		  settings: {
			slidesToShow: 2,
			slidesToScroll: 2,
			infinite: true,
			dots: true
		  }
		},
		{
		  breakpoint: 600,
		  settings: {
			slidesToShow: 2,
			slidesToScroll: 2
		  }
		},
		{
		  breakpoint: 480,
		  settings: {
			slidesToShow: 1,
			slidesToScroll: 1
		  }
		}
		// You can unslick at a given breakpoint now by adding:
		// settings: "unslick"
		// instead of a settings object
	  ]
	});
	
	// splice string "," 
	var myStringActivities = $(".activities-value").text();
	var myArrayActivities = myStringActivities.split(',');
	//	console.log(myArrayActivities);
	
	for (var i=0; i<myArrayActivities.length; i++) {
		var container = $(".activities-container");
		container.append('<p class="activity--box--destination--activities">' + myArrayActivities[i] + '</p>');
	}
	
	var myStringFeatures = $(".features-value").text();
	var myArrayFeatures = myStringFeatures.split(',');
	//	console.log(myArrayFeatures);
	
	for (var i=0; i<myArrayFeatures.length; i++) {
		var container = $(".features-container");
		container.append('<p class="activity--box--destination--features">' + myArrayFeatures[i] + '</p>');
	}
	
	var myStringMisc = $(".misc-value").text();
	var myArrayMisc = myStringMisc.split(',');
	//	console.log(myArrayMisc);
	
	for (var i=0; i<myArrayMisc.length; i++) {
		var container = $(".misc-container");
		container.append('<p class="activity--box--destination--misc">' + myArrayMisc[i] + '</p>');
	}
	
	// star rating average for all reviews
	var numStars = $('#num-stars').text();
	
	$("#star-rating").val(numStars).change();
	
	$('div.star-rating').raty({
		cancel: true,
  		target: '#star-rating',
		targetType: 'number',
		readOnly: true,
		score: numStars
	});
	
	// star rating form value
	$('div.star-rating2').raty({
		cancel: false,
  		target: '#id_rating',
		targetType: 'number',
		readOnly: false, 
		targetKeep: true,
		// targetText : '0',
	});
	
	$('div.star-rating2 i').removeAttr("title");
	
	// star rating for each review
	var numStars2 = $('#num-stars2').text();
		
	$('.star-rating3').raty({
		//cancel: false,
		//target: '#star-rating3',
		targetType: 'number',
		readOnly: true, 
		score: function() {
			return $(this).attr('data-score');
		}
	});
	
	// comments
	$(".comment--box").hide();
	
	$(".comment--show-hide").click(function() {   
		console.log("button clicked");
			$(this).closest('div').find('.comment--box').toggle("slow");
			if ($(this).text() == "Comment") { 
				$(this).text("hide comment(s)").css("font-weight", "bold"); 
			} else { 
				$(this).text("Comment").css("font-weight", "bold"); 
			}; 
	});
	
	// tabs for reviews/comments
	$( function() {
		$( "#tabs" ).tabs();
	});
	
	// show error for not choosing stars on review form
	$("#reviewInput").click(function(e) {
		var ratingDiv = $('.star-rating2');
		var ratingInput = ratingDiv.children('input[name="score"]');
		console.log(ratingInput.val());
		if (!ratingInput.val() || !ratingInput.val().trim()) {
			var errorDiv = $("#error-message-review");
			errorDiv.html("Please add a review and a rating.");
			errorDiv.css("visibility", "visible");
			errorDiv.css("color", "red");
			e.preventDefault();
		}
	});
	
});

	