from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Product,Contact,Order_detail
from math import *
from .paytm import Checksum
from Ecommerce import settings

MERCHANT_KEY = 'gpup7U%PxQ1T6y8u';

# Create your views here.
def index(request):
    '''prods=Product.objects.all()
    print("Products:- ",prods)
    n=len(prods)
    noofslides=ceil(n/4)
    allprods=[[noofslides,range(1,noofslides),prods]]'''
    allprods=[]
    prods=Product.objects.values('category','pid')
    categorys={i['category']for i in prods}
    #print("categorys:- ",categorys)
    for c in categorys:
        products=Product.objects.filter(category=c)
        n=len(products)
        noofslides = ceil(n / 4)
        allprods.append([noofslides,range(1,noofslides),products])
    return render(request,'shop/index.html',{'allprods':allprods})

def basic(request):
    return render(request,'shop/basic.html')

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    flag=0
    if request.method=="POST":
        name1=request.POST.get('name','')
        emailid=request.POST.get('emailid','')
        mobileno=request.POST.get('mobileno','')
        feedback=request.POST.get('feedback','')

        #print("data:- ",name,emailid,mobileno,feedback)
        con=Contact(name=name1,emailid=emailid,mobileno=mobileno,feedback=feedback)
        con.save()
        flag=1
    return render(request,'shop/contact.html',{'flag':flag})

def productview(request,pid):
    proview=Product.objects.get(pid=pid)
    #print("detail:- ",proview)
    return render(request,'shop/productview.html',{'proview':proview})

def order(request):
    flag1=False
    ver=False
    if request.method=='POST':
        itemjson=request.POST.get('citems','')
        fname=request.POST.get('firstname','')
        lname=request.POST.get('lastname','')
        email=request.POST.get('email','')
        mobno=request.POST.get('mobileno','')
        address=request.POST.get('address','')
        state=request.POST.get('state','')
        city=request.POST.get('city','')
        zipcode=request.POST.get('zipcode','')
        total=request.POST.get('total','')
        if(itemjson==''or fname=='' or lname=='' or email=='' or mobno=='' or address=='' or state=='' or city=='' or zipcode=='' or total==''):
            ver=True
        else:
            order1 = Order_detail(items=itemjson, firstname=fname, lastname=lname,
                                  email=email, mobileno=mobno,
                                  address=address, state=state, city=city,
                                  zipcode=zipcode, total=total)
            order1.save()
            flag1 = True
            # Request paytm to transfer the amount to your account after payment by user
            param_dict = {

                'MID': 'byLVwz55811088203547',
                'ORDER_ID': str(order1.oid),
                'TXN_AMOUNT': str(total),
                'CUST_ID': email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL': 'http://127.0.0.1:8000/shop/handlerequest/',

            }
            param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
            return render(request, 'shop/paytm.html', {'param_dict': param_dict})

        return render(request, 'shop/order.html',{'flag1':flag1,'ver':ver})
    return render(request,'shop/order.html')

@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'shop/paymentstatus.html', {'response': response_dict})

    '''if request.method == "POST":
        MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
        data_dict = {}
        for key in request.POST:
            data_dict[key] = request.POST[key]
        verify = Checksum.verify_checksum(data_dict, MERCHANT_KEY, data_dict['CHECKSUMHASH'])
        if verify:
            Fund_donation.objects.create(user=request.user, **data_dict)
            return render(request, "response.html", {"paytm": data_dict})
        else:
            return HttpResponse("checksum verify failed")
    return HttpResponse(status=200)'''

def searchmatch(stext,item):
    if stext.lower() in item.product_name.lower() or\
        stext.lower() in item.category.lower() or \
        stext.lower() in item.product_desc.lower():

        return True
    else:
        return False
def search(request):
    stext=request.GET.get('searchtext','')
    allprods = []
    prods = Product.objects.values('category', 'pid')
    categorys = {i['category'] for i in prods}
    # print("categorys:- ",categorys)
    for c in categorys:
        products = Product.objects.filter(category=c)
        sprod=[item for item in products if searchmatch(stext,item)]
        n = len(sprod)
        noofslides = ceil(n / 4)
        print("sprod:- ",len(allprods))
        if(n!=0):
            allprods.append([noofslides, range(1, noofslides), sprod])
        params={'allprods': allprods,"msg":""}
        if(len(allprods)==0):
            params={"msg":"Please enter Proper Product name to search"}
    return render(request, 'shop/search.html', params)
