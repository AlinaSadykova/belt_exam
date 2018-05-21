from django.shortcuts import render, redirect
from .models import User, Trip
import bcrypt
from django.contrib import messages


def index(request): #HOME PAGE
    return render(request, "exam_app/index.html")

def process(request): #PROCESSING REGISTRATION
    if request.method == "POST":
        result = User.objects.basic_validator(request.POST)
        if len(result['errors'])>0:
            for g in result['errors']:
                messages.error(request, g) 
            return redirect("/")       
        else:
            for h in result['success']:
                messages.error(request, h)
            ps = request.POST['password']
            hash1 = bcrypt.hashpw(ps.encode(), bcrypt.gensalt())
            y = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=hash1)
            request.session['user_id'] = y.id
            return redirect("/success")
  
        

def success(request): #USER HOME PAGE
    if 'user_id' in request.session:
        b =  User.objects.get(id=request.session['user_id']).trips.values()
        muk = User.objects.get(id = request.session['user_id'])
        # myuser = Trip.objects.get(id = id).users.values()
        t = Trip.objects.all().values()
        # gty = User.objects.exclude(id=request.session['user_id']).trips.values()
        u = Trip.objects.exclude(users=muk)
        ki = User.objects.exclude(id = muk.id)
        
        
        # w = User.objects.get(id = request.session['user_id']).trips
        # print("this is trip", w)
        p = {
            'name': muk.first_name,
            'trips': b,
            'travel': t,
            'excl': u,
            'user': ki 
        }
        
        print("Alina ", ki)
        # if request.method == POST:
            
        return render(request, "exam_app/index2.html", p)
    return redirect("/")   


def login(request): #PROCESSING LOGING
    if request.method == "POST":
        result = User.objects.validation2(request.POST)
        if result['status']:
            m = User.objects.filter(last_name = request.POST['last_name'])
            request.session["user_id"] = m[0].id 
            for g in result['errors']:
                messages.error(request, g)          
            return redirect("/success")
        else:
            for g in result['errors']:
                messages.error(request, g)
                return redirect("/") 


def reset(request): #LOGGINGOUT DELETE SESSION
    del request.session['user_id']
    return redirect("/")

def almostdone(request, id): #  trip information
    mytrip = Trip.objects.get(id=id)
    myuser = Trip.objects.get(id = id).users.values()
    print("shalll", myuser)
    # u = Trip.objects.exclude(users=muk)
    ty = User.objects.filter(trips = mytrip)
    print("iuyu", ty)
    # User.objects.get(id=request.session['user_id']).trips.values()
    yu = Trip.objects.get(id = id).users.exclude(id = request.session['user_id']).values()
    context =  {
        'gt': mytrip,
        'lk': yu,
        'pypy': ty,
        'kuku': myuser[0]['last_name']
    }
    print('alina', yu)
    return render(request, "exam_app/index4.html", context)

def addtravel(request): #PAGE WITH FORM FOR ADDING NEW TRIP
    # yuy =  User.objects.get(id=request.session['user_id'])
    
    # context =  {
    #     "g": yuy
    # }

    return render(request, "exam_app/index3.html")

def processtrip(request): #PROCESS A TRIP ADDING
    if request.method == "POST":
        us = User.objects.get(id = request.session['user_id'])
        y = Trip.objects.create(destination=request.POST['destination'], description=request.POST['description'], startdate=request.POST['startdate'],enddate=request.POST['enddate'])
        this_trip = Trip.objects.get(id=y.id)
        this_user = User.objects.get(id=us.id)
        this_user.trips.add(this_trip)
        b =  User.objects.get(id=request.session['user_id']).trips.values()
        print("BBBBB", b)
        return redirect("/success")


def join(request): #JOIN the TRIP
    if request.method == "POST":
        this_trip = Trip.objects.get(id=request.POST['travel'])
        this_user = User.objects.get(id=request.session['user_id'])
        this_user.trips.add(this_trip) 
    return redirect("/success")



    

