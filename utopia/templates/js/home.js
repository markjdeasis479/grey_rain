jQuery(document).ready(function() {
    var _HEADER_MENU=jQuery('.diosa_menu');
    var _PLACER_FLAG=false;
    var _POSITIONER=_HEADER_MENU.position();

    function stickyHeader() {
        jQuery(window).scroll(function() {
           if (jQuery(window).scrollTop()>_POSITIONER.top) {
               if (_PLACER_FLAG==false) {
                   _PLACER_FLAG=true;
                   setTimeout(function() {
                       _HEADER_MENU.css({
                           'position': 'fixed',
                           'left': _HEADER_MENU.offset().left + 'px',
                           'width': '960px',
                           'top': '-45px',
                           'z-index': 200,
                       });
                       _HEADER_MENU.stop(true).animate({top: '+=55px'}, 300);
                   }, 500);
               }
           }
           else {
                if (_PLACER_FLAG==true) {
                    _PLACER_FLAG=false;
                    setTimeout(function() {
                        _HEADER_MENU.css({
                            'position': 'relative',
                            'left': 0,
                            'width': '960px',
                            'top': 0,
                            'z-index': 'auto',
                        });
                    },500);
                }
           }
        });
    }

    stickyHeader();
});