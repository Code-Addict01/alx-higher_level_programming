$(document).ready(function () {
	$("INPUT#btn_translate").click(function () {
		const language_code = $("INPUT#language_code").val();
		$.get.JSON(
			 'https://www.fourtonfish.com/hellosalut/hello/?lang=${language_code}',
			 function (data) {
				 $("#hello").text(data.hello);
			 }
		);
	});
});
