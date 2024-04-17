from django.shortcuts import render



# Create your views here.
def info(request):
    return render(request, 'info.html')

def table(request):
    return render(request, 'table.html')

def collection(request):
    return render(request, 'collection.html')
