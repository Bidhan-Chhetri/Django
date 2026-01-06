from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    emails = ["bidhanchhetri52@gmail.com", "bisheshchhetri51@gmail.com"]
    context = {"email" : emails, "address" : "Butwal"}
    return render(request, 'main/contact.html', context) 

def greet(request):
    return HttpResponse("<H1>hello what are you doing Namaste!!!<h1>")