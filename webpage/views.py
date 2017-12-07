from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, "home.html", {})

def courseinfo(request):
	return render(request, "courseinfo.html", {})
	
def htmlcss(request):
	return render(request, "htmlcss.html", {})

def javascript(request):
	return render(request, "javascript.html", {})

def modules(request):
	return render(request, "modules.html", {})

def new(request):
	return render(request, "new.html", {})

def python(request):
	return render(request, "python.html", {})

def resources(request):
	return render(request, "resources.html", {})

def coreskilldemo(request):
	return render(request, "coreskilldemo.html", {})

def schedule(request):
	return render(request, "schedule.html", {})
