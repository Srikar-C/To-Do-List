from django.shortcuts import redirect, render

from app.models import Items, UserDetails

# Create your views here.


def home(request):
    return render(request, 'home.html')



def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')



credentials = {}

def loginDetails(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    credentials["username"] = username
    credentials["password"] = password
    print('User Details: ',username,password)
    users = UserDetails.objects.all().values()
    existuser = UserDetails.objects.filter(username=username,password=password)
    if existuser.exists():
        return render(request,'user.html',{'user':username})
    else:
        return render(request,'register.html')
    

def regDetails(request):
    users = UserDetails.objects.all().values()
    for i in range(len(users)):
        if users[i]['username']==request.POST['username'] and users[i]['email']==request.POST['email']:
            return render(request,'login.html',{'note':'User already exist, Try to login'})
    
    newuser = UserDetails(username = request.POST['username'],email = request.POST['email'],password=request.POST['password'])
    newuser.save()
    credentials['username'] = request.POST['username']
    credentials['password'] = request.POST['password']
    return render(request,'user.html',{'user':credentials['username']})


def user(request):
    return render(request,'user.html',{'user':credentials['username']})

def addItems(request):
    return render(request,'add.html',{'user':credentials['username']})


def addList(request):
    user = UserDetails.objects.get(username = credentials['username'])
    print("user: ",user)
    if user:
        list = Items.objects.all().values()
        Items.objects.create(user_list = user , list = request.POST['crntlist'])
        print('List of Items: ',list)
        return render(request, 'add.html',{'note':'Item added successfully','user':credentials['username']})
    

def viewlist(request):
    user = UserDetails.objects.get(username = credentials['username'])
    if user:
        list = Items.objects.filter(user_list = user).values()
        return render(request, 'viewlist.html',{'list':list,'user':credentials['username']})
    
def modify(request):
    user = UserDetails.objects.get(username = credentials['username'])
    modify = request.POST.get('modifylists')
    modifylists = Items.objects.get(id = modify)
    modifylists.list = request.POST['lists']
    modifylists.save()
    return redirect('viewlist')


def delete(request):
    user = UserDetails.objects.get(username = credentials['username'])
    delete = request.POST.get('dellists')
    deletelist = Items.objects.get(id = delete)
    deletelist.delete()
    return redirect('viewlist')

