from django.shortcuts import render,redirect
from .forms import MyUserForms
from .models import MyUser
# Create your views here.
def create(request):

    form = MyUserForms(request.POST or None)
    users = MyUser.objects.all()
    if form.is_valid():
        form.save()
        return redirect('/crud')
    return render(request,'index.html',{'form':form,'users':users})

def update(request,id):
    user = MyUser.objects.get(id=id)
    form = MyUserForms(request.POST or None,instance=user)
    users = MyUser.objects.all()
    if form.is_valid():
        form.save()
        return redirect('/crud')
    return render(request,'index.html',{'form':form,'users':users})

def delete(request,id):
    user = MyUser.objects.get(id=id)
    user.delete()
    return redirect('/crud')