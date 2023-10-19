from django.shortcuts import render,redirect
from carapp.models import Carproductdb,Catacarsdb,ratingdb
from carwebapp.models import Checkoutdb,contactdb,registerdb,Carselldb
from django.contrib import messages




# Create your views here.
def homePage(request):
    data = Carproductdb.objects.all()
    caro =Catacarsdb.objects.all()
    revw = ratingdb.objects.all()
    return render(request,"home.html",{'data':data, 'caro':caro, 'revw':revw})
def procarss(request,cat_name):
    carr = Carproductdb.objects.all()
    cardd = Catacarsdb.objects.filter(Name3=cat_name)
    procar = Carproductdb.objects.filter(CataName3=cat_name)
    return render(request,"carssss.html",{'procar':procar, 'carr':carr,'cardd':cardd})
def singlecar(request,dataid):
    regr = registerdb.objects.all()
    carsingle = Carproductdb.objects.get(id=dataid)
    request.session['previous_url'] = request.path
    return render(request,"carssingle.html",{'carsingle':carsingle , 'regr':regr})




def contactssave(request):
    if request.method == "POST":
        ynm = request.POST.get('y_name')
        eml = request.POST.get('y_email')
        sbj = request.POST.get('subjects')
        msg = request.POST.get('messages')
        obj = contactdb(Yname=ynm,Yemail=eml, Subjct=sbj, Messeges=msg )
        obj.save()
        messages.success(request, "Messege send successfully")
    return redirect(homePage)

def restrform(request):
    return render(request,"login.html")
def loginpage(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        mb = request.POST.get('mobile')
        ps = request.POST.get('password')
        cps = request.POST.get('cpassword')
        img = request.FILES['image']
        obj = registerdb(Name=na, Email=em, Mobile=mb, Password=ps, CPassword=cps, Image=img)
        obj.save()
        messages.success(request, "Registered Successfully")
    return redirect(restrform)

def usrlgn(request):
    if request.method == "POST":
        uname = request.POST.get('name')
        pwd = request.POST.get('password')
        if registerdb.objects.filter(Name=uname, Password=pwd).exists():
            request.session['name']=uname
            request.session['password']=pwd
            messages.success(request, "LogIn successfully")

            previous_url = request.session.get('previous_url')
            previous_url2 = request.session.get('previous_url2')

            request.session['previous_url'] = None
            request.session['previous_url2'] = None

            if previous_url:
                # Clear the stored previous URL from the session
                messages.success(request, "Book now")
                return redirect(previous_url)
            elif previous_url2:
                messages.success(request, "Save Details Now")
                return redirect(previous_url2)
            else:
                return redirect(homePage)

        else:
            messages.error(request, "Invalid username or password")
            return redirect(restrform)
    return redirect(restrform)
def logoutt(request):
    del request.session['name']
    del request.session['password']

    messages.success(request, "LogOut successfully")
    return redirect(homePage)


def checkoutSave(request):
    if request.method == "POST":
        pna = request.POST.get('carname')
        pyr = request.POST.get('yearman')
        pkm = request.POST.get('prokm')
        pfl = request.POST.get('profuel')
        pr = request.POST.get('pricecar')
        na = request.session.get('name')
        try:
            register_instance = registerdb.objects.get(Name=na)

            obj = Checkoutdb(Carname=pna, Yearman=pyr, Prokms=pkm, Profuel=pfl, Pricecar=pr, Register=register_instance)
            obj.save()
            messages.info(request, "Your information has been saved, we will contact you.")
            return redirect(homePage)
        except registerdb.DoesNotExist:
            messages.error(request, "User is not registered,Please login fist")
            return redirect(restrform)
        return render(singlecar)


def search_results(request):
    if request.method == "GET":
        query = request.GET.get('query')

        # Search in Catacarsdb and Carproductdb for matching names and items
        brand_results = Catacarsdb.objects.filter(Name3__icontains=query)
        cars_results = Carproductdb.objects.filter(ProName3__icontains=query)
        brand = Catacarsdb.objects.all()



        context = {
            'brand_results': brand_results,
            'cars_results': cars_results,
            'brand': brand
        }

        return render(request, 'search_result.html', context)

def carsell(request):
    request.session['previous_url2'] = request.path
    return render(request,"carsell.html")

def carsellsave(request):
    if request.method == "POST":
        pna7 = request.POST.get('proname7')
        pyr7 = request.POST.get('proyear7')
        pkm7 = request.POST.get('prokm7')
        pfl7 = request.POST.get('profuel7')
        pr7 = request.POST.get('proprice7')
        pdr7 = request.POST.get('prodicription7')
        imgx7 = request.FILES['proimage7']
        yrmob = request.POST.get('yrmob7')
        ynm = request.POST.get('y_name')
        eml = request.POST.get('y_email')


        obj = Carselldb(ProName7=pna7, Proyear7=pyr7, Prokms7=pkm7, Profuel7=pfl7, ProPrice7=pr7, ProDescription7=pdr7, ProImage7=imgx7, Yrmob=yrmob, Yname2=ynm, Yemail2=eml)
        obj.save()
        messages.info(request, "Your information has been saved, we will contact you.")
    return redirect(carsell)


