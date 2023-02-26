$(document).ready(function(){
	$('header .current_user_info').hover(function(){
		$('header .current_user_info .user_list').toggleClass('hide_user_list');
	})
})