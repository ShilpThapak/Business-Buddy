from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db import IntegrityError
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import User, role, lead, activity, task


def index(request):
    return render(request, 'business/index.html')

def business_buddy(request):
    return render(request, "business/business-index.html")
    #return HttpResponse("This is business buddy home page")

def sales(request):
    return render(request, "business/sales.html",{
        "leads": lead.objects.all
    })

@login_required(login_url='/business-buddy/login')
def leadpage(request, leadid):
    salesrole = role.objects.get(pk=1)
    leadprofile = lead.objects.get(pk=leadid)
    return render(request, "business/leadpage.html",{
        "lead": lead.objects.get(pk=leadid),
        "associates": User.objects.filter(role=salesrole),
        "activities": activity.objects.filter(oflead=leadprofile).order_by("-time"),
        "tasks": task.objects.all().order_by("time")
    })

@csrf_exempt
def assign(request):
    userid = request.POST['userid']
    leadid = request.POST['leadid']
    user = User.objects.get(pk=userid)
    leadtoassign = lead.objects.get(pk=leadid)
    print(leadtoassign)
    print(user)
    leadtoassign.assignedto = user
    leadtoassign.save()
    #return HttpResponse(status=204)
    return JsonResponse({"associate": user.username}, status=201)

@csrf_exempt
def editstatus(request):
    leadid = request.POST['leadid']
    newstatus = request.POST['newstatus']
    print(leadid)
    print(newstatus)

    leadtoupdate = lead.objects.get(pk=leadid)
    leadtoupdate.status = newstatus
    leadtoupdate.save()

    return JsonResponse({"newtext": leadtoupdate.status}, status=201)

@csrf_exempt
def savelead(request):
    leadname = request.POST['leadname']
    leademail = request.POST['leademail']
    leadnumber = request.POST['leadnumber']
    leadinterest = request.POST['leadinterest']
    print(leadname, leademail, leadnumber, leadinterest)
    newlead = lead(fullname=leadname, email=leademail, number=leadnumber, interest=leadinterest, status="New")
    newlead.save()
    #newactivity = activity()
    return HttpResponse(status=204)

def addactivity(request):
    userid = request.POST["userid"]
    author = User.objects.get(pk=userid)
    leadid = request.POST["leadid"]
    oflead = lead.objects.get(pk=leadid)
    text = request.POST["text"]
    activitytype = request.POST["activitytype"]
    print(userid, leadid, text, activitytype)
    newactivity = activity(activitytype=activitytype, text=text, oflead=oflead, author=author)
    newactivity.save()
    return HttpResponseRedirect(reverse("leadpage", args=leadid))

def addtask(request):
    userid = request.POST["userid"]
    author = User.objects.get(pk=userid)
    leadid = request.POST["leadid"]
    oflead = lead.objects.get(pk=leadid)
    text = request.POST["tasktext"]
    time = request.POST["time"]
    newtask = task(text=text, time=time, oflead=oflead, author=author)
    newtask.save()
    return HttpResponseRedirect(reverse("leadpage", args=leadid))

@csrf_exempt
def taskdone(request):
    if request.method == 'POST':
        taskid = request.POST['taskid']
        print(taskid)
        taskdone = task.objects.get(pk=taskid)
        taskdone.delete()
        return HttpResponse(status=204)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("business-buddy"))

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("business-buddy"))
        else:
            return render(request, "business/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "business/login.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        roleid = request.POST["roleid"]
        userrole = role.objects.get(pk=roleid)

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "business/register.html", {
                "message": "Passwords must match.",
                "roles": role.objects.all()
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.role = userrole
            user.save()
        except IntegrityError:
            return render(request, "business/register.html", {
                "message": "Username already taken.",
                "roles": role.objects.all()
            })
        login(request, user)
        return HttpResponseRedirect(reverse("business-buddy"))
    else:
        return render(request, "business/register.html", {
            "roles": role.objects.all()
        })