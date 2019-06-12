from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():

    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html' {'form':form})
