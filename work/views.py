from django.shortcuts import render,redirect
from django.views.generic import View
from work.models import Task
from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        exclude=("date",)


# lh:8000/tasks/all/
# method get
class TaskListView(View):
    def get(self,request,*args,**kwargs):
        qs=Task.objects.all()
        return render (request,"task_list.html",{"data":qs})
    
# lh:8000/tasks/add/
# method:get/post
class TaskCreateView(View):
    def get(self,request,*args,**kwargs):
        form=TaskForm()
        return render (request,"task_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task-list")
        else:
            return render(request,"task_add.html",{"form":form})

# lh:8000/tasks/pk/
# method:get       
class TaskDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Task.objects.get(id=id)
        return render (request,"task_detail.html",{"data":qs})

# task delete view   
# lh:8000/tasks/pk/delete
# method:get
class TaskDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Task.objects.filter(id=id).delete()
        return redirect("task-list")

# taskupdateview
# lh:8000/tasks/pk/update/
# method:get
class TaskUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        task_object=Task.objects.get(id=id)
        form=TaskForm(instance=task_object)
        return render(request,"task_edit.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        task_object=Task.objects.get(id=id)
        data=request.POST
        form=TaskForm(data,instance=task_object)
        if form.is_valid():
            form.save()
            return redirect("task-list")
        else:
            return render(request,"task_add.html",{"form":form})


 
