from django.shortcuts import render,redirect
from carapp.models import Catacarsdb,Carproductdb,ratingdb
from carwebapp.models import contactdb,Checkoutdb,registerdb,Carselldb
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login



# Create your views here.
def index3(request):
    return render(request,"index.html")

def brandzz(request):
    return render(request,"addcatagory.html")

def brandsave(request):
    if request.method == "POST":
        na = request.POST.get('name3')
        dr = request.POST.get('dicription3')
        img6 = request.FILES['image6']
        obj = Catacarsdb(Name3=na, Description3=dr, Image6=img6)
        obj.save()
        messages.success(request, "Saved suscessfully")
    return redirect(brandzz)

def dspbrand(request):
    data = Catacarsdb.objects.all()
    return render(request,"displaycatagory.html", {'data': data})

def editbrandpage(request, dataid):
    data = Catacarsdb.objects.get(id=dataid)
    return render(request,"catagoryedit.html", {'data':data})

def updatebrand(request,dataid):
    if request.method == "POST":
        na = request.POST.get('name3')
        dr = request.POST.get('description3')
    try:
        img6= request.FILES['image6']
        fs = FileSystemStorage()
        file = fs.save(img6.name,img6)
    except MultiValueDictKeyError:
        file = Catacarsdb.objects.get(id=dataid).Image6
    Catacarsdb.objects.filter(id=dataid).update(Name3=na, Description3=dr, Image6=file)
    messages.success(request, "Updated successfully")
    return redirect(dspbrand)

def deletebrand(request,dataid):
    data = Catacarsdb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "Deleted successfully")
    return redirect(dspbrand)



def carss(request):
    data = Catacarsdb.objects.all()
    return render(request,"addproduct.html",{'data':data})

def carssave(request):
    if request.method == "POST":
        cna = request.POST.get('catagoryname3')
        pna = request.POST.get('proname3')
        pyr = request.POST.get('proyear')
        pkm = request.POST.get('prokm')
        pfl = request.POST.get('profuel')
        pr = request.POST.get('proprice3')
        pdr = request.POST.get('prodicription3')
        imgx = request.FILES['proimage6']
        obj = Carproductdb(ProName3=pna, CataName3=cna, Proyear=pyr, Prokms=pkm, Profuel=pfl, ProPrice=pr, ProDescription3=pdr, ProImage6=imgx)
        obj.save()
        messages.success(request, "Saved successfully")
    return redirect(carss)

def dspcar(request):
    product = Carproductdb.objects.all()
    return render(request,"displayproduct.html",{'product':product})

def editcarpage(request, productid):
    brnd = Catacarsdb.objects.all()
    product = Carproductdb.objects.get(id=productid)
    return render(request,"productedit.html", {'product':product,'brnd':brnd})

def updatecar(request,productid):
    if request.method == "POST":
        cna = request.POST.get('catagoryname3')
        pna = request.POST.get('proname3')
        pyr = request.POST.get('proyear')
        pkm = request.POST.get('prokm')
        pfl = request.POST.get('profuel')
        pr = request.POST.get('proprice3')
        pdr = request.POST.get('prodicription3')
    try:
        img6 = request.FILES['proimage6']
        fs = FileSystemStorage()
        file = fs.save(img6.name, img6)
    except MultiValueDictKeyError:
        file = Carproductdb.objects.get(id=productid).ProImage6
    Carproductdb.objects.filter(id=productid).update(ProName3=pna, CataName3=cna, Proyear=pyr, Prokms=pkm, Profuel=pfl, ProPrice=pr, ProDescription3=pdr, ProImage6=file)
    messages.success(request, "Updated successfully")
    return redirect(dspcar)

def deletecars(request,productid):
    product = Carproductdb.objects.filter(id=productid)
    product.delete()
    messages.success(request, "Deleted successfully")
    return redirect(dspcar)


def loginpage(request):
    return render(request,"loginpage.html")

def adminlogin(request):
    if request.method=="POST":
        uname = request.POST.get('username')
        pswd = request.POST.get('password')
        if User.objects.filter(username__contains=uname).exists():
            user = authenticate(username=uname,password=pswd)
            if user is not None:
                login(request,user)
                request.session['username']=uname
                request.session['password']=pswd
                messages.success(request,"LogIn Susscesfully")
                return redirect(index3)
            else:
                messages.error(request,"Invalid Username or Password")
                return redirect(loginpage)
        else:
            return redirect(loginpage)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "LogOut successfully")
    return redirect(loginpage)

def displaycontact(request):
    contact = contactdb.objects.all()
    return render(request, "displaycontact.html", {'contact':contact})

def deletecontact(request,contactid):
    contact = contactdb.objects.filter(id=contactid)
    contact.delete()
    messages.success(request, "Deleted successfully")
    return redirect(displaycontact)

def dspcart(request):
    carrt = Checkoutdb.objects.all()
    return render(request,"Equiriesdisplay.html",{'carrt':carrt})

def cartdelete(request,cartid):
    carrt = Checkoutdb.objects.filter(id=cartid)
    carrt.delete()
    messages.success(request, "Deleted successfully")
    return redirect(dspcart)
def displogss(request):
    logd = registerdb.objects.all()
    return render(request,"logindetails.html",{'logd':logd})

def deletelog(request,loginnid):
    ulog = Checkoutdb.objects.filter(id=loginnid)
    ulog.delete()
    messages.success(request, "Deleted successfully")
    return redirect(displogss)
def dspcarsell(request):
    sellcar = Carselldb.objects.all()
    return render(request,"carselldisplay.html",{'sellcar':sellcar})

def carselldelete(request,carsellid):
    sellcar = Carselldb.objects.filter(id=carsellid)
    sellcar.delete()
    messages.success(request, "Deleted successfully")
    return redirect(dspcarsell)
def custrating(request):
    return render(request, "addreview.html")

def reviewsave(request):
    if request.method == "POST":
        ynm = request.POST.get('Yourname')
        yem = request.POST.get('yourmail')
        yrw = request.POST.get('yourreview')
        yimg = request.FILES['yourimage']
        obj = ratingdb(Yr_name=ynm, Email8=yem, Yr_rating=yrw, Yr_photo=yimg)
        obj.save()
        messages.success(request, "Saved successfully")
    return redirect(custrating)

def dspreview(request):
    revw = ratingdb.objects.all()
    return render(request,"dspreview.html",{'revw':revw})

def reviewdelete(request,revwid):
    reww = ratingdb.objects.filter(id=revwid)
    reww.delete()
    messages.success(request, "Deleted successfully")
    return redirect(dspreview)