$(document).ready(function () {
	$('#lightgallery').justifiedGallery({
		rowHeight: 280,
	}).on('jg.complete', function () {
		lightGallery(document.getElementById('lightgallery'));
	});
});
