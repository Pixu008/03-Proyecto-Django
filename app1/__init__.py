from django.shortcuts import render

def v1(request):
    return render(request, 'app1/app1v1.html')

def v2(request):
    return render(request, 'app1/app1v2.html')