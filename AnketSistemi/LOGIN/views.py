from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    if request.method == 'post':
        HttpResponse('hello')
    return render(request, 'LOGIN/LOGIN.html')
