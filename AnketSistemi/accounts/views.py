from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect


# Create your views here.
def home(request):

    if request.user.staff:
        return redirect('../admin/')
    elif request.user.ogr:
        return render(request, 'accounts/ogrenciHOME.html')
    elif request.user.hoc:
        return render(request, 'accounts/hocaHOME.html')
    elif request.user.yon:
        return render(request, 'accounts/yonetimHOME.html')
