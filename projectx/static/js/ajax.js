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

function searchSuccess(data, textStatus, jqXHR) {
  $('#search-results').html(data);
}

