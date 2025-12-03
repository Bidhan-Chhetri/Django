from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello welcome to my webpage")

def hello(request):
    return HttpResponse("Hello! How are you? are you ok.")