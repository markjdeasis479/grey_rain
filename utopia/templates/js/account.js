jQuery(document).ready(function() {
    //Forms
    _FRM_ACC=jQuery('#frm_account_info');
    _FRM_PW=jQuery('#frm_account_pw');
    _REP_PW=_FRM_PW.find('.userboard_pw_report');
    _REP_ACC=_FRM_ACC.find('.userboard_acc_report');
    //Fields
    _FLD_PW_OLD_PASSWORD=_FRM_PW.find('#account_old_password');
    _FLD_PW_NEW_PASSWORD=_FRM_PW.find('#account_new_password');
    _FLD_PW_RETYPE_PASSWORD=_FRM_PW.find('#account_retype_password');
    _FLD_ACC_EMAIL=_FRM_ACC.find('#account_email');
    _FLD_ACC_PREFIX=_FRM_ACC.find('#account_prefix');
    _FLD_ACC_FNAME=_FRM_ACC.find('#account_fname');
    _FLD_ACC_MNAME=_FRM_ACC.find('#account_mname');
    _FLD_ACC_LNAME=_FRM_ACC.find('#account_lname');
    _FLD_ACC_GENDER=_FRM_ACC.find('#account_gender');
    _FLD_ACC_BDATE=_FRM_ACC.find('#account_bdate');
    _FLD_ACC_PHONE=_FRM_ACC.find('#account_phone');
    _FLD_ACC_ALT_PHONE=_FRM_ACC.find('#account_alt_phone');
    _FLD_ACC_ADDRESS=_FRM_ACC.find('#account_address');
    _FLD_ACC_ALT_ADDRESS=_FRM_ACC.find('#account_alt_address');
    //Buttons
    _BTN_UPDATE_INFO=jQuery('#btn_update_info');
    _BTN_UPDATE_PASSWORD=jQuery('#btn_update_password');
    _BTN_UPDATE_CANCEL=jQuery('#btn_update_cancel')
    _BTN_UPDATE_PWANCEL=jQuery('#btn_pw_cancel');
    _BTN_UPDATE_ACC=jQuery('#btn_update_save');
    _BTN_UPDATE_PW=jQuery('#btn_pw_save');
    
    function init() {
        _FLD_ACC_BDATE.datepicker({'dateFormat':'yy-mm-dd'});
    }
    
    _BTN_UPDATE_INFO.click(function() {
        _FRM_ACC.find('input[type="text"], select').each(function(i,e) {
            jQuery(this).css('background-color', '#FFF').removeAttr('disabled');
            jQuery(this).attr('prev_val', jQuery(this).val());
        });
        _FRM_ACC.find('textarea').each(function(i,e) {
            jQuery(this).css('background-color', '#FFF').removeAttr('disabled');
            jQuery(this).attr('prev_val', jQuery(this).text());
        });
        jQuery('.shadow_leap').removeClass('shadow_leap').fadeIn(500);
        _BTN_UPDATE_INFO.parent('div').addClass('shadow_leap');
    });
    
    _BTN_UPDATE_CANCEL.click(function() {
        _FRM_ACC.find('input[type="text"], select').each(function(i,e) {
            jQuery(this).css('background-color', '#F8F8F8').attr('disabled', '');
            jQuery(this).val(jQuery(this).attr('prev_val'));
            jQuery(this).removeAttr('prev_val');
        });
        _FRM_ACC.find('textarea').each(function(i,e) {
            jQuery(this).css('background-color', '#F8F8F8').attr('disabled', '');
            jQuery(this).text(jQuery(this).attr('prev_val'));
            jQuery(this).removeAttr('prev_val');
        });
        jQuery('.shadow_leap').removeClass('shadow_leap').fadeIn(500);
        _BTN_UPDATE_CANCEL.parent('div').addClass('shadow_leap');
    });
    
    _BTN_UPDATE_PASSWORD.click(function() {
        _FRM_ACC.find('.error_box').hide();
        _REP_ACC.hide();
        _FRM_ACC.hide();
        _FRM_PW.show();
    });
    
    _BTN_UPDATE_PWANCEL.click(function() {
        _FRM_PW.find('.error_box').hide();
        _REP_PW.hide();
        _FRM_ACC.show();
        _FRM_PW.hide();
    });
    
    _BTN_UPDATE_ACC.click(function() {
        var is_valid=true;
        //Email
        if (_FLD_ACC_EMAIL.val().length==0) {
            var _parent=_FLD_ACC_EMAIL.parent('div');
            _parent.find('.error_box').show();
            _parent.find('.error_msg').text('This field cannot be empty.');
            is_valid=false;
        }
        else if (!isValidEmail(_FLD_ACC_EMAIL.val())) {
            var _parent=_FLD_ACC_EMAIL.parent('div');
            _parent.find('.error_box').show();
            _parent.find('.error_msg').text('Invalid email address.');
            is_valid=false;
        }
        //First Name
        if (_FLD_ACC_FNAME.val().length==0) {
            var _parent=_FLD_ACC_FNAME.parent('div');
            _parent.find('.error_box').show();
            _parent.find('.error_msg').text('This field cannot be empty.');
            is_valid=false;
        }
        //Middle Name
        if (_FLD_ACC_MNAME.val().length==0) {
            var _parent=_FLD_ACC_MNAME.parent('div');
            _parent.find('.error_box').show();
            _parent.find('.error_msg').text('This field cannot be empty.');
            is_valid=false;
        }
        //Last Name
        if (_FLD_ACC_LNAME.val().length==0) {
            var _parent=_FLD_ACC_LNAME.parent('div');
            _parent.find('.error_box').show();
            _parent.find('.error_msg').text('This field cannot be empty.');
            is_valid=false;
        }
        //Phone Number
        if (_FLD_ACC_PHONE.val().length==0) {
            var _parent=_FLD_ACC_PHONE.parent('div');
            _parent.find('.error_box').show();
            _parent.find('.error_msg').text('This field cannot be empty.');
            is_valid=false;
        }
        //Address
        if (_FLD_ACC_ADDRESS.text().length==0) {
            var _parent=_FLD_ACC_ADDRESS.parent('div');
            _parent.find('.error_box').show();
            _parent.find('.error_msg').text('This field cannot be empty.');
            is_valid=true;
        }
        if (!is_valid) {
            _REP_ACC.text('There is an error in the following fields below:').show();
        }
        return is_valid; 
    });
    
    _BTN_UPDATE_PW.click(function() {
        var is_valid=true;
        if (_FLD_PW_OLD_PASSWORD.val().length==0) {
            var _parent=_FLD_PW_OLD_PASSWORD.parent('div');
            _parent.find('.error_box').show();
            _parent.find('.error_msg').text('This field cannot be empty.');
            is_valid=false;
        }
        if (_FLD_PW_NEW_PASSWORD.val().length<6) {
            var _parent=_FLD_PW_NEW_PASSWORD.parent('div');
            _parent.find('.error_box').show();
            _parent.find('.error_msg').text('This field must be of 6 characters or above.');
            is_valid=false;
        }
        if (_FLD_PW_NEW_PASSWORD.val()!=_FLD_PW_RETYPE_PASSWORD.val()) {
            var _parent=_FLD_PW_RETYPE_PASSWORD.parent('div');
            _parent.find('.error_box').show();
            _parent.fnd('.error_msg').text('New password does not match.');
            is_valid=false;
        }
        if (!is_valid) {
            _REP_PW.text("There is an error in the following fields below:").show();
        }
        return is_valid; 
    });
    
    function isValidEmail(email) {
        var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
        return regex.test(email);
    }

    function isNullOrEmpty(data) {
        return (data==null||data=='');
    }

    function isAlphaNumeric(text) {
        return (!(/[^a-zA-Z0-9._]/g.test(text)));
    }
    
    init();
});