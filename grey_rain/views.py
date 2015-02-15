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

#--- VIEW: LOGIN
@ensure_csrf_cookie
def login(request):
    return render_to_response('login.html', {'do_param': request.GET.get('do', ''), 'email_register':request.POST.get('email_register', '')}, RequestContext(request));

#--- VIEW: LOGIN