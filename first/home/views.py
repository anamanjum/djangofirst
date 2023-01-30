from ast import Return
from django.shortcuts import render,redirect
from .models import Language,ProgrammingCourse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
def home(request):
    lang=Language.objects.all()
    #lang=Language.objects.filter(fees=180000,name='java').all()
    #lang=Language.objects.filter(name='java').all()
    #lang=Language.objects.get(id=1)
    return render(request,"index.html",{'lang':lang})
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        rpassword=request.POST['rpassword']
        if User.objects.filter(username=username).exists():
            messages.warning(request,'username already exits')
            return redirect("/signup")
        elif User.objects.filter(email=email).exists():
            messages.warning(request,'email already exits')
            return redirect("/signup")
        elif password!=rpassword:
            messages.error(request,'passwords missmatch')
            return redirect("/signup")
        else:
            user=User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=password)
            user.save()
            return redirect("/")
            messages.success(request,"sucessfully signed up")      
    else:
        return render(request,'signup.html')
def ulogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.warning(request,'Invalid user name and password')
            return redirect('/login')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    messages.warning(request,'sucessfully logout')
    return redirect('/')
def addcourse(request):
    if request.method=='POST':
        p=ProgrammingCourse()
        p.name=request.POST['name']
        p.duration=request.POST['duration']
        fees=request.POST['fees']
        p.fees=int(fees)
        p.trainer=request.POST['trainer']
        p.save()
        messages.success(request,'sucessfully added')
        return redirect("/")
    else:
        return render(request,'addcourse.html')
def showcourse(request):
    data=ProgrammingCourse.objects.all()
    return render(request,'showcourse.html',{'lang':data})
def delete(request):
    id=request.GET['id']
    ProgrammingCourse.objects.filter(id=id).delete()
    data=ProgrammingCourse.objects.all()
    return render(request,'showcourse.html',{'lang':data})
def update(request):
    p=ProgrammingCourse()
    p.id=request.POST['id']
    p.name=request.POST['name']
    p.duration=request.POST['duration']
    fees=request.POST['fees']
    p.fees=int(fees)
    p.trainer=request.POST['trainer']
    p.save()
    data=ProgrammingCourse.objects.all()
    return render(request,'showcourse.html',{'lang':data})