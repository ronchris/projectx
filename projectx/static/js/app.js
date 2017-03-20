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
	
	// select list for star ratings
//	$('#id_rating').starrating({
//		clearable  : true,
//		clickFn     : null,
//		showText : false,
//	});
//	
	var numStars = $('#num-stars').text();
	console.log("numStars is " + numStars);
	var numStarsRounded = Math.round(numStars);
//	console.log("numStars rounded up is " + numStarsRounded); 
//	$( '#star-rating' ).starrating({
//		clearable  : false,
//		showText : false,
//		readOnly: true
//	});
//
//	var string = 'div.review-container option[value=' + numStarsRounded.toString() + ']'
//
//	$("#star-rating").val(numStarsRounded).change();
	
	$('div.star-rating').raty({
		cancel     : true,
  		target     : '#star-rating',
		targetType : 'number',
		readOnly: true, 
		score: numStarsRounded
	});
	
});

	