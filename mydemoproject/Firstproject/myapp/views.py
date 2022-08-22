from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .forms import RegistrationForm,ContentForm
from .models import User,Content
from django.db.models import Q

def indexfunction(request):
    return HttpResponse("My First Django Project")
def userfunction(request):
    return HttpResponse("User Project")
def guestfunction(request):
    return HttpResponse("guest Project")
def userfunction1(request,id):
    return HttpResponse(id) 
def addfunction(request,a,b):
    return HttpResponse(a+b)
def userfunction2(request,name):
    return HttpResponse(name)
def userfunction3(request,name,id):
    mydict={
        "name": name,
        "id":id
    }  
    return JsonResponse(mydict)
def userpage(request):
    return redirect("user")


def indexpage(request):
    return render(request,"index.html")

def adminlogin(request):
    return render(request,"adminlogin.html")

def userlogin(request):
    return render(request,"userlogin.html")

def userhome(request):
    uname=request.session['uname']    #retriving session variable
    return render(request,"userhome.html",{'uname':uname})

def userreg(request):
    return render(request,"userreg.html")

def changepwd(request):
    uname=request.session['uname']
    return render(request,"changepwd.html",{'uname':uname})


def ulogout(request):
    return render(request,"userlogin.html")

def contactpage(request):
    return render(request,"contactus.html")

def adminhome(request):
    return render(request,"adminhome.html")

def alogout(request):
    return render(request,"adminlogin.html")

def viewusers(request):
    users=User.objects.all()   #select * from user_table;
    count=User.objects.all().count() #select count(*) from user_table
    return render(request,"viewusers.html",{'users':users,'count':count}) #you can consider different names for key and value

def deleteuser(request,id):
    #User.objects.filter(id=id) select * from user_table where id=id 
    User.objects.filter(id=id).delete()
    users=User.objects.all()
    count=User.objects.all().count()
    return render(request,"viewusers.html",{'users':users,'count':count})

def deleteuserbyid(request):
    users=User.objects.all()
    return render(request,"deleteuserbyid.html",{'users':users})

def deleteuserbyid1(request):
    users=User.objects.all()
    if request.method=="POST":
        uid=request.POST['uid']
        User.objects.filter(id=uid).delete()
        users=User.objects.all()
        count=User.objects.all().count()
        return render(request,"viewusers.html",{'users':users},{'count':count})
    else:
        users=User.objects.all()
        return render(request,"deleteuserbyid.html",{'users':users})
    return render(request,"deleteuserbyid.html",{'users':users})


def checkadmin(request):
    if request.method=="POST":
        aid=request.POST['aid']
        apwd=request.POST['apwd']
        if aid=='admin' and apwd=='admin':
            return redirect("adminhome")
        else:
            return HttpResponse("Login Invalid")


def userreg(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userlogin')
    else:
        form=RegistrationForm()
    return render(request,'userreg.html',{'form':form})

def addcontent(request):
    if request.method=='POST':
        form=ContentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addcontent')
    else:
        form=ContentForm()
    return render(request,'addcontent.html',{'form':form})


def checkuser(request):
    if request.method=="POST":
        uname=request.POST['uname']   
        pwd=request.POST['pwd']
        flag=User.objects.filter(Q(username__iexact=uname) & Q(password__iexact=pwd))
        if flag:
            request.session['uname']=uname   #creating session variable
            return redirect("userhome")
        else:
            return HttpResponse("Login InValid")
    else:
        return render("userlogin.html")
    return render("userlogin.html")




def changepwd1(request):
    uname=request.session['uname']
    if request.method=="POST":
        opwd=request.POST['opwd']
        npwd=request.POST['npwd']
        flag=User.objects.filter(Q(username__iexact=uname) & Q(password__iexact=opwd))
        if flag:
            User.objects.filter(username=uname).update(password=npwd)
            return HttpResponse('Password is Updated Successfully')
        else:
            return HttpResponse('Old Password is incorrect')
    else:
        return render('changepwd.html')
    return render('changepwd.html')

def searchcontent(request):
    uname=request.session['uname']
    return render(request,"searchcontent.html")

def searchcontent1(request):
    uname=request.session['uname']
    if request.method == "POST":
        keyword=request.POST['keyword']
        flag=Content.objects.filter(Q(title__icontains=keyword))
        if flag:
            content=Content.objects.filter(Q(title__icontains=keyword))
            return render(request,"displaycontent.html",{'content':content})
        else:
            return HttpResponse('Search Not Found')
    else:
        return render(request,"searchcontent.html")
    return render(request,"searchcontent.html")


