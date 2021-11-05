from django.shortcuts import *
from django.contrib import messages
from django.http import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from app.forms import *
from app.models import *


@csrf_exempt



def home(request):
    return render(request,'app/home.html')

def about(request):
    return render(request,'app/about.html')

def menu(request):
    records = Menu.objects.order_by('item_category')
    return render(request,'app/menu.html',{'records':records})

def burgers(request):
    records=Menu.objects.filter(item_category='Burgers')
    return render(request, 'app/menu.html',{'records':records})

def sweets(request):
    records=Menu.objects.filter(item_category='Sweets')
    return render(request, 'app/menu.html',{'records':records})

def drinks(request):
    records=Menu.objects.filter(item_category='Drinks')
    return render(request, 'app/menu.html',{'records':records})

def pizzas(request):
    records=Menu.objects.filter(item_category='Pizzas')
    return render(request, 'app/menu.html',{'records':records})

def restaurants(request):
    records=Restaurants.objects.all()
    return render(request,'app/restaurants.html',{'records':records})

def restwise(request,cat):
    getCat=cat
    records=Menu.objects.filter(item_rest_id=getCat)
    return render(request,'app/menu.html',{'records':records})

def gallery(request):
    return render(request,'app/gallery.html')

@csrf_exempt
def login(request):

    if request.session.has_key('cust_email'):
        cust_email = request.session['cust_email']
        records=Customer.objects.filter(cust_email=cust_email)
        return render(request,'app/userprofile.html',{'records':records})

    if request.method == "POST":
        form=Login(request.POST or none)
        cust_email=request.POST.get('cust_email')
        cust_password=request.POST.get('cust_password')

        if (Customer.objects.filter(cust_email=cust_email).exists()):
            records=Customer.objects.get(cust_email=cust_email)
            if records.cust_password == cust_password :
                request.session['cust_email'] = cust_email

                obj=Customer.objects.get(cust_email=cust_email)
                obj.orders_set.create(order_by=cust_email)

                records=Customer.objects.filter(cust_email=cust_email)
                return render(request,'app/userprofile.html',{'records':records})

            else:
                messages.error(request,'Wrong Password !')
                return redirect('login')

        else:
            messages.error(request,'Email Id is not registered. Please SignUp first')
            return redirect('login')

    form=Login()
    return render(request,'app/login.html',{'form':form})

@csrf_exempt
def signup(request):
    if request.method == "POST" :
        form=Signup(request.POST or None)
        if form.is_valid():
            try:

                records = Customer()
                records.cust_email=form.cleaned_data['cust_email']
                records.cust_password=form.cleaned_data['cust_password']
                records.cust_name=form.cleaned_data['cust_name']
                records.cust_phone=form.cleaned_data['cust_phone']
                records.cust_gender=form.cleaned_data['cust_gender']
                records.cust_address=form.cleaned_data['cust_address']
                records.save()
                messages.success(request,"Congratulations you have been successfully Registered!")
                return HttpResponseRedirect('/login/')

            except:
                pass
    else:
        form=Signup()
    return render(request,'app/signup.html',{'form':form})

def logout(request):

    try:
        del request.session['cust_email']

        messages.success(request,"Logged Out")
    except:
        pass

    return HttpResponseRedirect('/login/')


@csrf_exempt

def addtocart(request,id):
    if request.session.has_key('cust_email') == False :
        messages.error(request,"Login Required")
        return HttpResponseRedirect('/login/')

    cust_email=request.session['cust_email']
    obj=Customer.objects.get(cust_email=cust_email)

    if request.session.has_key('cust_email'):
        obj=Orders.objects.filter(order_by=cust_email).latest('order_id')
        get_order_id=obj.order_id
        
    else:
        obj.orders_set.create(order_by=cust_email)
        obj=Orders.objects.filter(order_by=cust_email).latest('order_id')
        get_order_id=obj.order_id


    obj=Menu.objects.get(item_id=int(id))
    order_item_name=obj.item_name
    order_item_price=obj.item_price
    order_item_calories=obj.item_calories
    order_item_logo=obj.item_logo

    obj=Orders.objects.filter(order_by=cust_email).latest('order_id')
    get_order_id=obj.order_id

    
    obj1=orderItem.objects.filter(order_id=get_order_id)

    if  obj1.filter(order_item_name=order_item_name).exists():
        obj2=obj1.get(order_item_name=order_item_name)
        obj2.order_item_quantity = str(int(obj2.order_item_quantity) + 1 )
        obj2.save()
    else:
        quantity = '1'

        obj=Orders.objects.filter(order_by=cust_email).latest('order_id')
        obj.orderitem_set.create(order_item_name=order_item_name,order_item_price=order_item_price,order_item_logo=order_item_logo,order_item_calories=order_item_calories,order_item_quantity=quantity)

    messages.success(request,"Item Added to Cart")
    return redirect('menu')
    

def showCart(request):

    if request.session.has_key('cust_email') == False :
        messages.error(request,"Login Required")
        return HttpResponseRedirect('/login/')

    cust_email=request.session['cust_email']
    obj=Orders.objects.filter(order_by=cust_email).latest('order_id')
    get_order_id=obj.order_id
    records=orderItem.objects.filter(order_id=get_order_id)

    total_amount=0
    total_calories=0
    get_total_amount=0

    for x in records :

        total_amount = total_amount + int(x.order_item_price) * int(x.order_item_quantity)
        total_calories = total_calories + int(x.order_item_calories) * int(x.order_item_quantity)
    
    
    get_total_calories=total_calories
    get_total_amount=total_amount

    return render(request,'app/cart.html',{'records':records,'get_total_amount':get_total_amount,'get_total_calories':get_total_calories})


def mail(request):
    
    return render(request,'app/mail.html')

def lastorders(request):

    cust_email=request.session['cust_email']
    obj=Customer.objects.get(cust_email=cust_email)
    add=obj.cust_address
    contact=obj.cust_phone
    records=Orders.objects.filter(order_by=cust_email)

    return render(request,'app/lastorders.html',{'records':records,'add':add,'contact':contact})
