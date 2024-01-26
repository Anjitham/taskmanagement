from django.db import models

class Task(models.Model):
    title=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True,blank=True)
    user=models.CharField(max_length=200)
    options=(
        ("Completed","Completed"),
        ("Inprogress","Inprogress"),
         ("Pending","Pending")
    )
    status=models.CharField(max_length=200,choices=options,default="Pending")

    def __str__(self):
        return self.title

