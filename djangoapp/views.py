from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
import json
from rest_framework.views import APIView
# Create your views here.

def first(request):
    return HttpResponse("My first django page")

def second(request):
    return HttpResponse("My second django page")
# render

def third(request):
    return render(request,'third.html')

def fourth(request):
    return  render(request,'fourth.html')

def registration(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        username=request.POST.get('username')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password==cpassword:
            a=register(fname=fname,lname=lname,username=username,email=email,phone=phone,gender=gender,address=address,dob=dob,password=password)
            a.save()
            return HttpResponse('Registration success')
        else:
            return HttpResponse('Password incorrect')
    return render(request,'registration.html')

# def login(request):
#     if request.method=='POST':
#         email=request.POST.get('username')
#         password=request.POST.get('password')
#         a=register.objects.all()
#         for i in a:
#             if (i.email==email and i.password==password):
#                 return HttpResponse("Login successfull")
#         else:
#             return HttpResponse("Login failed")
#     else:
#          return render(request,'login-page.html')

def uploadings(request):
    if request.method=='POST':
        audioname=request.POST.get('audioname')
        audio=request.FILES.get('audio')
        videoname=request.POST.get('videoname')
        video=request.FILES.get('video')
        pdfname=request.POST.get('pdfname')
        pdf=request.FILES.get('document')
        x=uploads(audioname=audioname,audio=audio,videoname=videoname,video=video,pdfname=pdfname,pdf=pdf)
        x.save()
        return HttpResponse('File uploads successfully completed')
    return render(request,'uploads.html')


def index(request):
    return render(request,'index.html')

def file_upload(request):
    if request.method=='POST':
        filename=request.POST.get('filename')
        image=request.FILES.get('fileimage')
        description=request.POST.get('description')
        b=fileupload(filename=filename,fileimage=image,description=description)
        b.save()
        return HttpResponse('File upload success')


    return render(request,'fileupload.html')

def employee_registration(request):
    if request.method=='POST':
        emp_name=request.POST.get('empname')
        email=request.POST.get('email')
        company_name=request.POST.get('company_name')
        designation=request.POST.get('designation')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password==cpassword:
            register=emp_register(emp_name=emp_name,email=email,company_name=company_name,designation=designation,password=password)
            register.save()
            return HttpResponse('Registration Success')
        else:
            return HttpResponse("Incorrect password")
    else:
        return render(request,'emp_register.html')


def emp_search(request):
    if request.method=='POST':
        name=request.POST.get('empname')
        designation=request.POST.get('designation')
        a=emp_register.objects.all()
        for i in a:
            if i.emp_name==name and i.designation==designation:
                return HttpResponse('Employee found')
        else:
            return HttpResponse('Employee not found')
    else:
        return render(request,'emp_search.html')

def select_checkbox(request):
    if request.method=='POST':
        name=request.POST.get('name')
        state=request.POST.get('state')
        english=request.POST.get('english')
        if english=='on':
            english=True
        else:
            english=False
        malayalam=request.POST.get('malayalam')
        if malayalam=='on':
            malayalam=True
        else:
            malayalam=False
        hindi=request.POST.get('hindi')
        if hindi=='on':
            hindi=True
        else:
            hindi=False
        b=select_checks_model(name=name,state=state,english=english,malayalam=malayalam,hindi=hindi)
        b.save()
        return HttpResponse('SUCCESS')
    else:
        return render(request,'select_checkbox.html')

def display(request):
    a=register.objects.all() #return a tuple of data
    return render(request,'display.html',{'data':a})

def emp_display(request):
    a=emp_register.objects.all() #return a tuple of data
    return render(request,'empdisplay.html',{'data':a})


def filedisplay(request):
    id=[]
    filename=[]
    image=[]
    desc=[]
    a=fileupload.objects.all()
    for i in a:
        id1=i.id
        id.append(id1)
        im=str(i.fileimage).split('/')[-1]
        image.append(im)
        name=i.filename
        filename.append(name)
        des=i.description
        desc.append(des)
    mylist=zip(id,filename,image,desc)
    return render(request,'filedisplay.html',{'file':mylist})


def uploadsdisplay(request):
    id=[]
    a_name=[]
    audios=[]
    v_name=[]
    video=[]
    pdf_name=[]
    pdf=[]
    b=uploads.objects.all()
    for i in b:
        id1=i.id
        id.append(id1)
        aname=i.audioname
        a_name.append(aname)
        audio1=str(i.audio).split('/')[-1]
        audios.append(audio1)
        vname=i.videoname
        v_name.append(vname)
        video1=str(i.video).split('/')[-1]
        video.append(video1)
        pdfname=i.pdfname
        pdf_name.append(pdfname)
        pdf1=str(i.pdf).split('/')[-1]
        pdf.append(pdf1)
    list=zip(id,a_name,audios,v_name,video,pdf_name,pdf)
    return render(request, 'uploadsdisplay.html', {'upload': list})


def update_data(request,id):
    a=register.objects.get(id=id)
    if request.method=='POST':
        a.fname=request.POST.get('fname')
        a.lname=request.POST.get('lname')
        a.username=request.POST.get('username')
        a.email=request.POST.get('email')
        a.phone=request.POST.get('phone')
        # a.gender=request.POST.get('gender')
        if str(request.POST.get('gender')) in ['Female','Male']:
            a.gender = request.POST.get('gender')
        else:
            a.save()
        a.address=request.POST.get('address')
        # a.dob=request.POST.get('dob')
        if len(str(request.POST.get('dob')))>0:
            a.dob = request.POST.get('dob')
        else:
            a.save()
        a.save()
        return redirect(display)
    return render(request, 'edit_profile.html',{'data':a})

def emp_update(request,id):
    a = emp_register.objects.get(id=id)
    if request.method=='POST':
        a.emp_name=request.POST.get('empname')
        a.email=request.POST.get('email')
        a.company_name=request.POST.get('company_name')
        a.designation=request.POST.get('designation')
        a.save()
        return redirect(emp_display)
    return render(request, 'empupdation.html', {'data': a})

def file_edit(request,id):
    a=fileupload.objects.get(id=id)
    image=str(a.fileimage).split('/')[-1]
    if request.method=='POST':
        a.filename=request.POST.get('filename')
        if len(str(request.FILES.get('fileimage')))>0:
            a.fileimage=request.FILES.get('fileimage')
        else:
            a.save()
        a.description=request.POST.get('description')
        a.save()
        return redirect(filedisplay)
    return render(request,'file_edit.html',{'file':a,'img':image})

def edit_uploads(request,id):
    a=uploads.objects.get(id=id)
    audio=str(a.audio).split('/')[-1]
    video=str(a.video).split('/')[-1]
    pdf=str(a.pdf).split('/')[-1]
    if request.method=='POST':
        a.audioname=request.POST.get('audioname')
        if request.FILES.get('audio')==None:
            a.save()
        else:
            a.audio = request.FILES.get('audio')
            a.save()
        a.videoname=request.POST.get('videoname')
        if request.FILES.get('video')==None:
            a.save()
        else:
            a.video = request.FILES.get('video')
            a.save()
        a.pdfname=request.POST.get('pdfname')
        if request.FILES.get('document')==None:
            a.save()
        else:
            a.pdf = request.FILES.get('document')
            a.save()
        a.save()
        return redirect(uploadsdisplay)
    return render(request,'edit_uploads.html',{'file':a,'aud':audio,'vid':video,'pdf':pdf})


def delete_profile(request,id):
    a=register.objects.get(id=id)
    a.delete()
    return redirect(display)

def delete_emp(request,id):
    a=emp_register.objects.get(id=id)
    a.delete()
    return redirect(emp_display)

def delete_file(request,id):
    a=fileupload.objects.get(id=id)
    a.delete()
    return redirect(filedisplay)

def delete_uploads(request,id):
    a=uploads.objects.get(id=id)
    a.delete()
    return redirect(uploadsdisplay)

def userregistration(request):
    if request.method=='POST':
        a=userreg(request.POST)
        if a.is_valid():    #it check the validity of the form
            us=request.POST.get('username')
            em=request.POST.get('email')
            fn=request.POST.get('first_name')
            ln=request.POST.get('last_name')
            pa=request.POST.get('password')
            b=User(username=us,first_name=fn,last_name=ln,email=em,password=pa)
            b.save()
            return HttpResponse('authenticated user added')
        else:
            return HttpResponse('user not added')

    else:
        form=userreg()
        return render(request,'userregister.html',{'form':form})


def userReg(request):
    if request.method=='POST':
        a=userform(request.POST)
        if a.is_valid():
            us = a.cleaned_data['username']
            em = a.cleaned_data['email']
            fn = a.cleaned_data['first_name']
            ln = a.cleaned_data['last_name']
            pa = a.cleaned_data['password']
            conf=a.cleaned_data['conf']
            if pa==conf:
                b = User(username=us, first_name=fn, last_name=ln, email=em)
                User.set_password(pa) #create a new user instance and set the password using set_password to avoid hashing error
                b.save()
                return HttpResponse('authenticated user added')
            else:
                return HttpResponse("password doesn't match")
        else:
            return HttpResponse('user not added')

    else:
        form = userform()
        return render(request, 'userreg.html', {'form': form})

def user_login(request):
    if request.method=='POST':
        form=userlogin(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponse('logged in successfully.')
            else:
                return HttpResponse('Invalid Username or Password')
        else:
            return HttpResponse('Invalid username or password')
    else:
        return render(request,'login.html')



def product_api_response():
    with open(r"C:\Users\user\PycharmProjects\DjangoProjects\djangopro\djangoapp\product.json","r",encoding="utf8") as f:
        data = json.load(f)
    return data


class product_api(APIView):
    def get(self,request):
        data=product_api_response()
        return render(request,'product_api.html',{'data':data})

def media_file_load():
    with open(r"C:\Users\user\PycharmProjects\DjangoProjects\djangopro\djangoapp\media_files.json","r",encoding='utf8') as a:
        data=json.load(a)
    return data

class media_file_api(APIView):
    def get(self,request):
        data=media_file_load()
        return render(request,'media_file.html',{'data':data})

