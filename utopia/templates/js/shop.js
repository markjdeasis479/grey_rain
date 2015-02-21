jQuery(document).ready(function() {
    var _SHOPBOARD_NEW_ITEMS=jQuery('#shopboard_new_items');
    var _SHOPBOARD_PROMO_ITEMS=jQuery('#shopboard_promo_items');
    var _SHOPBOARD_HOT_ITEMS=jQuery('#shopboard_hot_items');
    var _hover_on_user_option=false;
    
    
    jQuery('.diosa_dashleft a').click(function(evt) {
        evt.preventDefault();
    });
    
    jQuery('.diosa_dashleft a').click(function() {
        jQuery('.dashmenu_active').removeClass('dashmenu_active');
        jQuery(this).find('.diosa_dashmenu').addClass('dashmenu_active');
        jQuery('.shopboard_active').removeClass('shopboard_active');
        jQuery('.diosa_shopcontent').eq(jQuery(this).index()).addClass('shopboard_active');
    });
    
    jQuery('.diosa_user_account').click(function(evt) {
        jQuery('.diosa_user_option').fadeToggle(500);
        evt.preventDefault();
    });
    
    jQuery('.diosa_user_account a').click(function(evt) {
        jQuery('.diosa_user_option').fadeToggle();
    });
    
    jQuery('.diosa_user_account, .diosa_user_option').on('mouseenter', function() {
       _hover_on_user_option=true; 
    });
    
    jQuery('.diosa_user_account, .diosa_user_option').on('mouseleave', function() {
       _hover_on_user_option=false;
        setTimeout(function() {
            if (!_hover_on_user_option) {
                jQuery('.diosa_user_option').fadeOut(500);
            }
        }, 500);
    });
});