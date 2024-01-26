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
            return render(request,"task-add",{"form":form})
