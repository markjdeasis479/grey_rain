from django.shortcuts import render;
from django.http import HttpResponse;
from django.http.response import HttpResponseRedirect;
from django.shortcuts import render, render_to_response;
from django.template import RequestContext;
from django.views.decorators.csrf import ensure_csrf_cookie;
import json;
from datetime import datetime, timedelta;
#models
from grey_rain.models import Item, ItemCategory, ItemSubcategory, ItemVariant, Customer, Carousel, Sessionizer;

# Create your views here.

#--- VIEW: INDEX
def index(request):
    #--- CAROUSEL
    carousel=Carousel.objects.all();
    carousel_arr=[];
    for i in range(carousel.count()):
        carousel_item={
            'img': carousel[i].caro_img.url.replace('utopia', ''),
            'link': carousel[i].caro_link,
        };
        carousel_arr.append(carousel_item);
    #--- CAROUSEL

    #--- NEW ARRIVALS
    new_arrivals=Item.objects.all();
    new_arrivals_arr=[];
    for i in range(new_arrivals.count()):
        new_arrivals_item={
            'id': new_arrivals[i].item_id,
            'name': new_arrivals[i].item_name,
            'img': new_arrivals[i].item_img_sm.url.replace('utopia', ''),
            'short_desc': new_arrivals[i].item_short_desc,
            'price': '{0:.2f}'.format(round(new_arrivals[i].item_price, 2)),
        };
        new_arrivals_arr.append(new_arrivals_item);
    #--- NEW ARRIVALS

    #--- CATEGORIES
    category_arr=[];
    category=ItemCategory.objects.all();
    for i in range(category.count()):
        subcategory=ItemSubcategory.objects.all().filter(isc_category=category[i].ic_id);
        subcategory_arr=[];
        for j in range(subcategory.count()):
            subcategory_item={
                'name': subcategory[j].isc_name,
                'id': subcategory[j].isc_id,
            };
            subcategory_arr.append(subcategory_item);
        category_item={
            'name': category[i].ic_name,
            'id': category[i].ic_id,
            'subcategory': subcategory_arr,
        };
        category_arr.append(category_item);
    #--- CATEGORIES

    #--- SESSIONIZER
    session_customer=None;
    session_token=None;
    if 'cust_id' in request.session and 'token_id' in request.session:
        session_customer=Customer.objects.all().filter(cust_id=request.session['cust_id'])[0];
        session_token=request.session['token_id'];
    #--- SESSIONIZER
    return render_to_response('index.html', {'new_arrivals': new_arrivals_arr, 'carousel': carousel_arr,
                                             'category': category_arr, 'session_cust': session_customer},
                                             RequestContext(request));
#--- VIEW: INDEX

#--- VIEW: REGISTER
@ensure_csrf_cookie
def register(request):
    register_mode=request.GET.get('user_register','');
    #--- Register user
    if register_mode == '1':
        _cust_email=request.POST['cust_email'];
        if Customer.objects.all().filter(cust_email=_cust_email).count() == 0:
            _cust_password=request.POST['cust_password_1'];
            _cust_prefix=request.POST['cust_prefix'];
            _cust_first_name=request.POST['cust_first_name'];
            _cust_middle_name=request.POST['cust_middle_name'];
            _cust_last_name=request.POST['cust_last_name'];
            _cust_gender=request.POST['cust_gender'];
            _cust_birth_date=request.POST['cust_birth_date'];
            _cust_phone_number=request.POST['cust_phone_number'];
            _cust_alt_phone=request.POST.get('cust_alt_phone', '');
            _cust_home_address=request.POST['cust_home_address'];
            _cust_alt_home=request.POST.get('cust_alt_home', '');
            new_customer=Customer(cust_email=_cust_email, cust_password=_cust_password, cust_prefix=_cust_prefix, cust_first_name=_cust_first_name,
                cust_middle_name=_cust_middle_name, cust_last_name=_cust_last_name, cust_gender=_cust_gender, cust_birth_date=_cust_birth_date,
                cust_phone_number=_cust_phone_number, cust_alt_phone=_cust_alt_phone, cust_home_address=_cust_home_address, cust_alt_home=_cust_alt_home);
            new_customer.save();
        return render_to_response('register.html', {'user_register': 2, 'user_email': _cust_email}, RequestContext(request));
    #--- Verify user
    elif register_mode == '2':
        _verify_code=request.POST['user_verification_code'];
        _user_email=request.POST['user_email'];
        return render_to_response('register.html', {'user_register': 2, 'user_email': _user_email, 'verification_error': 'Invalid verification code.'}, RequestContext(request));
    #--- Display registration form
    else:
        return render_to_response('register.html', {'user_register': 1}, RequestContext(request));

#--- VIEW: LOGIN
@ensure_csrf_cookie
def login(request):
    _cust_email=request.POST.get('cust_email', '');
    _cust_password=request.POST.get('cust_password', '');
    _cust_keep_login=request.POST.get('cust_keep_login', '');
    #--- Display login form
    if len(_cust_email) == 0:
        return render_to_response('login.html', {}, RequestContext(request));
    #Evaluate credentials
    else:
        #Display error in login form
        _sign_cust=Customer.objects.all().filter(cust_email=_cust_email, cust_password=_cust_password);
        if _sign_cust.count() == 0:
            return render_to_response('login.html', {'login_error': True}, RequestContext(request));
        #Redirect to user account page
        else:
            #Clear recent session
            request.session.flush();
            #set session expiry to browser closing
            request.session.set_expiry(0);
            request.session['cust_id']=_sign_cust[0].cust_id;
            request.session['token_id']=generateToken(request.session['cust_id']);
            _new_session=Sessionizer(session_user=_sign_cust[0], session_token=request.session['token_id'],
                                     session_date_time_expired=datetime.now()+timedelta(days=1));
            _new_session.save();
            #redirect to myaccount
            #return HttpResponse('cust_id' in request.session);
            return HttpResponseRedirect('/myaccount');
#--- VIEW: LOGIN
        
#--- VIEW: MY ACCOUNT
def myaccount(request):
    _cust_id=request.session['cust_id'];
    if _cust_id:
        _my_acc=Customer.objects.all().filter(cust_id=_cust_id);
        if _my_acc.count()==0:
            return HttpResponseRedirect('/login');
        else:
            _my_acc=_my_acc[0];
            _param_update=request.GET.get('update', '');
            #Updates Customer Information
            if _param_update == 'info':
                #Form Fields
                _fld_email=request.POST['account_email'];
                _fld_prefix=request.POST['account_prefix'];
                _fld_fname=request.POST['account_fname'];
                _fld_mname=request.POST['account_mname'];
                _fld_lname=request.POST['account_lname'];
                _fld_bdate=request.POST['account_bdate'];
                _fld_gender=request.POST['account_gender'];
                _fld_phone=request.POST['account_phone'];
                _fld_alt_phone=request.POST['account_alt_phone'];
                _fld_address=request.POST['account_address'];
                _fld_alt_address=request.POST['account_alt_address'];
                #Customer Fields Update
                _my_acc.cust_email=_fld_email;
                _my_acc.cust_prefix=_fld_prefix;
                _my_acc.cust_first_name=_fld_fname;
                _my_acc.cust_middle_name=_fld_mname;
                _my_acc.cust_last_name=_fld_lname;
                _my_acc.cust_birth_date=_fld_bdate;
                _my_acc.cust_gender=_fld_gender;
                _my_acc.cust_phone_number=_fld_phone;
                _my_acc.cust_alt_phone=_fld_alt_phone;
                _my_acc.cust_home_address=_fld_address;
                _my_acc.cust_alt_home=_fld_alt_address;
                #Save changes
                _my_acc.save();
                _update_report={
                    'userboard_update': 'Account information has been updated successfully.',
                    'userboard_status': True,
                };
                return render_to_response('myaccount.html', _update_report, RequestContext(request));
            #Updates Customer Password
            elif _param_update == 'password':
                #Form Fields
                _fld_old_password=request.POST['account_old_password'];
                _fld_new_password=request.POST['account_new_password'];
                _update_report={};
                if _fld_old_password == _my_acc.cust_password:
                    _my_acc.cust_password=_fld_new_password;
                    #Save changes
                    _my_acc.save();
                    _update_report={
                        'userboard_update': 'New password has been updated successfully.',
                        'userboard_status': True,
                    };        
                else:
                    _update_report={
                        'userboard_update': 'You have entered your current password incorrectly.',
                        'userboard_status': False,
                    };
                return render_to_response('myaccount.html', _update_report, RequestContext(request));
            else:        
                _my_info={
                    'email': _my_acc.cust_email,
                    'prefix': _my_acc.cust_prefix,
                    'fname': _my_acc.cust_first_name,
                    'mname': _my_acc.cust_middle_name,
                    'lname': _my_acc.cust_last_name,
                    'bdate': _my_acc.cust_birth_date,
                    'gender': _my_acc.cust_gender,
                    'phone': _my_acc.cust_phone_number,
                    'alt_phone': _my_acc.cust_alt_phone,
                    'address': _my_acc.cust_home_address,
                    'alt_address': _my_acc.cust_alt_home,
                };
                return render_to_response('myaccount.html', _my_info, RequestContext(request));
    else:
        return HttpResponseRedirect('/login');
#--- VIEW: MY ACCOUNT

#--- VIEW: LOG OUT
def logout(request):
    request.session.flush();
    return HttpResponseRedirect('/');
#--- VIEW: LOG OUT

#--- HELPER: GENERATETOKEN
def generateToken(customer_id):
    token=datetime.strftime(datetime.now(), '%Y%m%d%H%M%S');
    token*=customer_id;
    return hex(int(token));
#--- HELPER: GENERATETOKEN