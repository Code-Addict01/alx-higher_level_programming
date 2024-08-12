$(document).ready(function () {
	$.get.JSON("https://hellosalut.stefanbohacek.dev/?lang=fr", function (data) {
		 $("DIV#hello").text(data.hello);
	});
});
