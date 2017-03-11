$(function() {

		var geocoder, location, map;
		geocoder = new google.maps.Geocoder();

		var latlng = new google.maps.LatLng(11.9283293, 120.23973360000002);

		var options = {
		zoom: 10,
		center: latlng,
		mapTypeId: google.maps.MapTypeId.ROADMAP
		
  	};
	
	$.each($('.destination'), function() {
		location = $(this).find('.address').text();
		map = new google.maps.Map($(this).find('.map')[0], options);

		geocoder.geocode( { 'address': location }, function(results, status) {
			if (status === google.maps.GeocoderStatus.OK) {
				map.setCenter(results[0].geometry.location);

				var marker = new google.maps.Marker({
					map: map,
					position: results[0].geometry.location
				});
			}
			else {
				console.log("We've got an error with our geocode.");
			}
		});
	});
});