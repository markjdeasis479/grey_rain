jQuery(document).ready(function(){
    var _REGISTER_FORM=jQuery('.utopia_registration_form');
    var _CUST_EMAIL=_REGISTER_FORM.find('#cust_email');
    var _CUST_PASSWORD_1=_REGISTER_FORM.find('#cust_password_1');
    var _CUST_PASSWORD_2=_REGISTER_FORM.find('#cust_password_2');
    var _CUST_PREFIX=_REGISTER_FORM.find('#cust_prefix');
    var _CUST_FIRST_NAME=_REGISTER_FORM.find('#cust_first_name');
    var _CUST_MIDDLE_NAME=_REGISTER_FORM.find('#cust_middle_name');
    var _CUST_LAST_NAME=_REGISTER_FORM.find('#cust_last_name');
    var _CUST_GENDER=_REGISTER_FORM.find('#cust_gender');
    var _CUST_BIRTH_DATE=_REGISTER_FORM.find('#cust_birth_date');
    var _CUST_PHONE_NUMBER=_REGISTER_FORM.find('#cust_phone_number');
    var _CUST_ALT_PHONE=_REGISTER_FORM.find('#cust_alt_phone');
    var _CUST_HOME_ADDRESS=_REGISTER_FORM.find('#cust_home_address');
    var _CUST_ALT_HOME=_REGISTER_FORM.find('#cust_alt_home');
    var _CUST_SUBMIT=_REGISTER_FORM.find('#cust_register_submit');
    _CUST_BIRTH_DATE.datepicker({'dateFormat':'yy-mm-dd'});

    _CUST_EMAIL.on('blur', function() {
        var _this=jQuery(this);
        var msg=null;
        if (_this.val().length==0) {
            msg='Email address cannot be empty.';
        }
        else if (!isValidEmail(_this.val())) {
            msg='Invalid email address.';
        }
        if (!isNullOrEmpty(msg)) {
            _this.parent('div').find('.error_box').fadeIn(500);
            _this.parent('div').find('.error_box .error_msg').html(msg);
        }
        else {
            _this.parent('div').find('.error_box').fadeOut(500);
        }
    });
                       
    _CUST_PASSWORD_1.on('blur', function() {
        var _this=jQuery(this);
        var msg=null;
        if (_this.val().length<6) {
            msg='Password must be 6 characters or more.'
        }
        if (!isNullOrEmpty(msg)) {
            _this.parent('div').find('.error_box').fadeIn(500);
            _this.parent('div').find('.error_box .error_msg').html(msg);
        }
        else {
            _this.parent('div').find('.error_box').fadeOut(500);
        }
    });
    
    _CUST_PASSWORD_2.on('blur', function() {
        var _this=jQuery(this);
        var msg=null;
        if (_this.val().length<6) {
            msg='Password must be 6 characters or more.'
        }
        else if (_this.val()!=_CUST_PASSWORD_1.val()) {
            msg='Password does not match.';
        }
        if (!isNullOrEmpty(msg)) {
            _this.parent('div').find('.error_box').fadeIn(500);
            _this.parent('div').find('.error_box .error_msg').html(msg);
            
        }
        else {
            _this.parent('div').find('.error_box').fadeOut(500);
        }
    });
    
    _CUST_PREFIX.on('change', function() {
        var _this=jQuery(this);
        if (_this.val()=='Mr.') {
            _CUST_GENDER.val('Male');
            _this.parent('div').find('.error_box').fadeOut(500);
        }
        else {
            _CUST_GENDER.val('Female');
            _this.parent('div').find('.error_box').fadeOut(500);
        }
    });
    
    _CUST_GENDER.on('change', function() {
        var _this=jQuery(this);
        if (_this.val()=='Male') {
            _CUST_PREFIX.val('Mr.');
            _this.parent('div').find('.error_box').fadeOut(500);
        }
        else {
            _CUST_PREFIX.val('Ms.');
            _this.parent('div').find('.error_box').fadeOut(500);
        }
    });
    
    inputValidator(_CUST_FIRST_NAME, 'First Name');
    inputValidator(_CUST_MIDDLE_NAME, 'Middle Name');
    inputValidator(_CUST_LAST_NAME, 'Last Name');
    inputValidator(_CUST_BIRTH_DATE, 'Birth date');
    inputValidator(_CUST_GENDER, 'Gender');
    inputValidator(_CUST_PHONE_NUMBER, 'Phone Number');
    inputValidator(_CUST_HOME_ADDRESS, 'Home Address');
    
    _CUST_SUBMIT.on('click', function() {
        var is_valid=true;
        //Email Address
        if (_CUST_EMAIL.val().length==0) {
            _CUST_EMAIL.parent('div').find('.error_box').fadeIn(500);
            _CUST_EMAIL.parent('div').find('.error_msg').html('Email address cannot be empty.');
            is_valid=false;
        }
        else if (!isValidEmail(_CUST_EMAIL.val())) {
            _CUST_EMAIL.parent('div').find('.error_box').fadeIn(500);
            _CUST_EMAIL.parent('div').find('.error_msg').html('Email address cannot be empty.');
            is_valid=false;
        }
        //Password
        if (_CUST_PASSWORD_1.val().length<6) {
            _CUST_PASSWORD_1.parent('div').find('.error_box').fadeIn(500);
            _CUST_PASSWORD_1.parent('div').find('.error_msg').html('Password must be 6 characters or more.');
            is_valid=false;
        }
        if (_CUST_PASSWORD_2.val().length<6) {
            _CUST_PASSWORD_2.parent('div').find('.error_box').fadeIn(500);
            _CUST_PASSWORD_2.parent('div').find('.error_msg').html('Password must be 6 characters or more.');
            is_valid=false;
        }
        else if (_CUST_PASSWORD_1.val()!=_CUST_PASSWORD_2.val()) {
            _CUST_PASSWORD_2.parent('div').find('.error_box').fadeIn(500);
            _CUST_PASSWORD_2.parent('div').find('.error_msg').html('Password does not match');
            is_valid=false;
        }
        var fields_list=[_CUST_PREFIX, _CUST_FIRST_NAME, _CUST_MIDDLE_NAME, _CUST_LAST_NAME, _CUST_GENDER, _CUST_BIRTH_DATE, _CUST_PHONE_NUMBER, _CUST_HOME_ADDRESS],
            fields_name=['Prefix', 'First Name', 'Middle Name', 'Last Name', 'Gender', 'Birth date', 'Phone Number', 'Home Address'];
        for (var i=0;i<fields_list.length;i++) {
            if (fields_list[i].val().length==0) {
                fields_list[i].parent('div').find('.error_box').fadeIn(500);
                fields_list[i].parent('div').find('.error_msg').html(fields_name[i]+' cannot be empty.');
                is_valid=false;
            }
        }
        return is_valid;
    });
                       
    jQuery('#submit_register').click(function() {
        var _this=jQuery(this).parentsUntil('.diosa_register');
        var csrf=_this.find('input[name="csrfmiddlewaretoken"]').val();
        //Process
        jQuery.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                    // Only send the token to relative URLs i.e. locally.
                    xhr.setRequestHeader("X-CSRFToken", csrf);
                }
            }
        });
        jQuery.ajax({
           url: '//'+window.location.host+'/ajax_server/?register='+_this.find('#email_register').val(),
           type: 'GET',
           contentType: 'application/json',
           success: function(data) {
           }
        });
        return false;
    });
    
    function inputValidator(elem, name) {
        elem.on('blur', function() {
            var msg=null;
            if (elem.val().length==0) {
                msg=name + ' cannot be empty.';
            }
            if (!isNullOrEmpty(msg)) {
                elem.parent('div').find('.error_box').fadeIn(500);
                elem.parent('div').find('.error_box .error_msg').html(msg);
                
            }
            else {
                elem.parent('div').find('.error_box').fadeOut(500);
            }
        });
    }
                       
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
});