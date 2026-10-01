from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404,redirect,render
from .forms import ProjectForm,TaskForm
from .models import Project,Task
@login_required
def dashboard(r):
 ts=Task.objects.filter(project__owner=r.user)
 return render(r,"tasks/dashboard.html",{"projects":Project.objects.filter(owner=r.user),"tasks":ts,"todo":ts.filter(status="todo").count(),"doing":ts.filter(status="doing").count(),"done":ts.filter(status="done").count()})
@login_required
def project_list(r):return render(r,"tasks/project_list.html",{"projects":Project.objects.filter(owner=r.user)})
@login_required
def project_form(r,pk=None):
 o=get_object_or_404(Project,pk=pk,owner=r.user) if pk else None; f=ProjectForm(r.POST or None,instance=o)
 if f.is_valid():
  x=f.save(commit=False);x.owner=r.user;x.save();return redirect("project_list")
 return render(r,"tasks/form.html",{"form":f,"title":"Editar projeto" if o else "Novo projeto"})
@login_required
def project_delete(r,pk):
 o=get_object_or_404(Project,pk=pk,owner=r.user)
 if r.method=="POST":o.delete();return redirect("project_list")
 return render(r,"tasks/confirm_delete.html",{"object":o})
@login_required
def task_list(r):
 qs=Task.objects.filter(project__owner=r.user).select_related("project");q=r.GET.get("q","").strip();s=r.GET.get("status","")
 if q:qs=qs.filter(Q(title__icontains=q)|Q(project__name__icontains=q))
 if s:qs=qs.filter(status=s)
 return render(r,"tasks/task_list.html",{"tasks":qs,"q":q,"status":s,"statuses":Task.Status.choices})
@login_required
def task_form(r,pk=None):
 o=get_object_or_404(Task,pk=pk,project__owner=r.user) if pk else None;f=TaskForm(r.POST or None,instance=o,user=r.user)
 if f.is_valid():f.save();return redirect("task_list")
 return render(r,"tasks/form.html",{"form":f,"title":"Editar tarefa" if o else "Nova tarefa"})
@login_required
def task_delete(r,pk):
 o=get_object_or_404(Task,pk=pk,project__owner=r.user)
 if r.method=="POST":o.delete();return redirect("task_list")
 return render(r,"tasks/confirm_delete.html",{"object":o})