$(document).ready(function(){
    $('.clickable').on('click', function(){
        window.location = $(this).data('href');
        console.log('test');
    });
});