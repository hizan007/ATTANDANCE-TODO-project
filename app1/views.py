from django.shortcuts import render, redirect

from app1.forms import attandanceform
from app1.models import attandance


# Create your views here.
def attandance1(request):
    return render(request,'index.html')

def add_attandance1(request):
    form = attandanceform()
    if request.method=='POST':
        form=attandanceform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_attandance1')
    return render(request,'2ndpage.html',{'form':form})

def view_attandance1(request):
    data=attandance.objects.all()
    return render(request,'3rdpage.html',{'data':data})


def update_attandance1(request,id):
    data=attandance.objects.get(id=id)
    form=attandanceform(instance=data)
    if request.method=='POST':
        form=attandanceform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('view_attandance1')
    return render (request,'update.html',{'form':form})



def delete_attandance1(request,id):
    attandance.objects.get(id=id).delete()
    return redirect('view_attandance1')


