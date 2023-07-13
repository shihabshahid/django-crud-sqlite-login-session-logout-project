from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import user_table

# Create your views here.
def admin_login(request):
    if request.method=='POST':
        input_name = request.POST.get('name','')
        input_password = request.POST.get('password','')
        admin_user = authenticate(username=input_name,password=input_password)
        if admin_user is not None:
            login(request,admin_user)
            return redirect('retrieve_url')
        else:
            messages.warning (request, 'name or password not mached')
            return redirect('login_url')
    elif request.method=='GET':
        return render(request,"login.html")

@login_required 
def admin_logout(request):
    logout(request)
    return render(request,"login.html")
    
@login_required
def retrieve(request):
    Context={
        'datas':user_table.objects.all()
    }
    return render(request,"retrieve.html",Context)

@login_required
def create(request):
    if request.method=='POST':
        input_name = request.POST.get('name','')
        input_contact = request.POST.get('contact','')
        user = user_table(name=input_name,contact=input_contact)
        user.save()
        messages.success(request, 'Data Saved')
        return redirect('retrieve_url')
    elif request.method=='GET':
        return render(request,"create.html")
    
@login_required
def update(request,id):
    user_data = user_table.objects.get(id=id)
    if request.method=='POST':
        user_data.name = request.POST.get('name','')
        user_data.contact = request.POST.get('contact','')
        messages.success(request, 'Data Updated')
        user_data.save()
        return redirect('retrieve_url')
    elif request.method=='GET':
        Context={
            'datas':user_data
        }
        return render(request,"update.html",Context)

@login_required   
def delete(request,id):
    user_table.objects.get(id=id).delete()
    messages.success(request, 'Data Deleted')
    return redirect('retrieve_url')

