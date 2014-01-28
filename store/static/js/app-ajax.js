$(document).ready(function() {
	$('#likes').click(function(){
	var catid;
	catid = $(this).attr("data-catid");
	$.get('/app/like_category/', {category_id: catid}, function(data){
			$('#likes').hide();
		});
	});
});
