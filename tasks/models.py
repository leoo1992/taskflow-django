from django.contrib.auth.models import User
from django.db import models
class Project(models.Model):
 name=models.CharField("Nome",max_length=120)
 description=models.TextField("Descrição",blank=True)
 owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name="projects")
 created_at=models.DateTimeField(auto_now_add=True)
 def __str__(self): return self.name
class Task(models.Model):
 class Status(models.TextChoices):
  TODO="todo","A fazer"; DOING="doing","Em andamento"; DONE="done","Concluída"
 class Priority(models.TextChoices):
  LOW="low","Baixa"; MEDIUM="medium","Média"; HIGH="high","Alta"
 project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name="tasks")
 title=models.CharField("Título",max_length=160)
 description=models.TextField("Descrição",blank=True)
 status=models.CharField("Status",max_length=10,choices=Status.choices,default=Status.TODO)
 priority=models.CharField("Prioridade",max_length=10,choices=Priority.choices,default=Priority.MEDIUM)
 due_date=models.DateField("Prazo",null=True,blank=True)
 created_at=models.DateTimeField(auto_now_add=True)
 def __str__(self): return self.title