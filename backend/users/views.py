from django.shortcuts import render

# Create your views here.
def login_error(request):
    return render(request, 'login_error.html')