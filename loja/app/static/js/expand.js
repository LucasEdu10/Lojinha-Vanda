$( document ).ready(function() { 
    $('.fabrics').click(function(){
        if ($(this).find('.ocult').css('display') == 'none') {
            // $(this).find('.position-img').css('display') == 'none';
            $(this).find('.ocult').slideDown("slow");
            $(this).find('.expand').css('transform', 'rotate(45deg)');
        }else{
            // $(this).find('.position-img').css('display') == 'none';
            $(this).find('.ocult').slideUp("slow");
            $(this).find('.expand').css('transform', 'rotate(315deg)');
        }
     });
});