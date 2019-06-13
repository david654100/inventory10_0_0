from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'success_login/success_login.html')
