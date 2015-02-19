from django.shortcuts import render;
from django.http import HttpResponse;
from django.http.response import HttpResponseRedirect;
from django.shortcuts import render, render_to_response;
from django.template import RequestContext;
from django.views.decorators.csrf import ensure_csrf_cookie;
import json;
#models
from grey_rain.models import Item, ItemCategory, ItemSubcategory, ItemVariant, Customer, Carousel;

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
    #--- NEW ARRIVALS

    #--- CATEGORIES
    category_arr=[];
    category=ItemCategory.objects.all();
    for i in range(category.count()):
        subcategory=ItemSubcategory.objects.all().filter(category=category[i].ic_id);
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

    return render_to_response('index.html', {'new_arrivals': new_arrivals, 'carousel': carousel_arr, 'category': category_arr}, RequestContext(request));
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
        return render_to_response('login.html', {'user_register': 2, 'user_email': _cust_email}, RequestContext(request));
    #--- Verify user
    elif register_mode == '2':
        _verify_code=request.POST['user_verification_code'];
        _user_email=request.POST['user_email'];
        return render_to_response('login.html', {'user_register': 2, 'user_email': _user_email, 'verification_error': 'Invalid verification code.'}, RequestContext(request));
    #--- Display registration form
    else:
        return render_to_response('login.html', {'user_register': 1}, RequestContext(request));

#--- VIEW: LOGIN