from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
#from upload_validator import FileTypeValidator

def signup(request):
    while True:
        #try:
        if request.method == 'POST':
            # User has info and wants an account now!
            if request.POST['password1'] == request.POST['password2']:
                try:
                    user = User.objects.get(username=request.POST['username'])
                    return render(request, 'accounts/signup.html', {'error':'Username has already been taken'})
                except User.DoesNotExist:
                    user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                    auth.login(request,user)
                    return redirect('home')
            else:
                return render(request, 'accounts/signup.html', {'error':'Passwords must match'})
        else:
            # User wants to enter info
            return render(request, 'accounts/signup.html')

        #except ValueError:
            #return render(request, 'accounts/signup.html', {'error': 'You have to fill in your username and/or password'})

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error':'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

@login_required
def addatrail(request):
    context = {}
    if request.method == 'POST':
        upload_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(upload_file.name, upload_file)
        context['url'] = fs.url(name)
#        validator = FileTypeValidator(
#    allowed_extensions=['.shp', '.csv', '.kml', '.json'])
    return render(request, 'accounts/addatrail.html', context)
