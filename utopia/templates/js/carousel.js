/**
 * Created by mark john on 11/9/2014.
 */
jQuery(document).ready(function() {
    var _CAROUSEL=jQuery('.diosa_carousel');
    var _PAGING=_CAROUSEL.find('.carousel_pager');
    var _ITEM_COUNT=0;
    var _ITEM_INDEX=0;
    var _INTERVAL=5000;
    var _PAGER=jQuery('<a href="#"><div class="pager"></div></a>');
    var _ANIMATOR=null;

    function init() {
        _ITEM_COUNT=_CAROUSEL.find('.slide_item').length;
        generatePager();
        startAnimator();
    }

    function generatePager() {
        for (var i=0;i<_ITEM_COUNT;i++){
            _PAGING.prepend(_PAGER.clone());
        }
        //Set first itemto display
        _PAGING.find('.pager:first').addClass('pager_active');
        _CAROUSEL.find('.slide_item:gt(0)').addClass('dNone');
        //Set pagers' event
        _PAGING.find('.pager').click(function() {
            var next=jQuery(this).parent().index();
            if (next!=_ITEM_INDEX) {
                //Halt animator
                clearInterval(_ANIMATOR);
                //Display next
                _ITEM_INDEX = next;
                var prev = _PAGING.find('.pager_active').parent().index();
                _CAROUSEL.find('.slide_item').eq(prev).stop(true).fadeOut(500, function() {
                    jQuery(this).addClass('dNone');
                });
                _PAGING.find('.pager').eq(prev).removeClass('pager_active');
                _CAROUSEL.find('.slide_item').eq(_ITEM_INDEX).stop(true).fadeIn(550, function() {
                    jQuery(this).removeClass('dNone');
                    startAnimator();
                });
                _PAGING.find('.pager').eq(_ITEM_INDEX).addClass('pager_active');
            }
        });
        _PAGING.find('a').click(function() {
           return false;
        });
    }

    function startAnimator(){
        _ANIMATOR=setInterval(function() {
            _ITEM_INDEX++;
            if (_ITEM_INDEX==_ITEM_COUNT) {
                _ITEM_INDEX=0;
            }
            var prev = _PAGING.find('.pager_active').parent().index();
            _CAROUSEL.find('.slide_item').eq(prev).stop(true).fadeOut(500, function() {
                jQuery(this).addClass('dNone');
            });
            _PAGING.find('.pager').eq(prev).removeClass('pager_active');
            _CAROUSEL.find('.slide_item').eq(_ITEM_INDEX).stop(true).fadeIn(550, function() {
                jQuery(this).removeClass('dNone');
            });
            _PAGING.find('.pager').eq(_ITEM_INDEX).addClass('pager_active');
        }, _INTERVAL);
    }

    init();
});