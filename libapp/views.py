from django.db.models import Q
from django.shortcuts import render, redirect
from libapp.models import user_signup
from libapp.models import Book_details
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view

# Create your views here.


def signup(request):
    if request.method == 'POST':
        Sname = request.POST.get('Name')
        print(Sname)
        Sdob = request.POST.get('Dateofbirth')
        Semail = request.POST.get('Email')
        Smob = request.POST.get('Mob')
        Spass = request.POST.get('Password')
        obj = user_signup.objects.create(
            Name=Sname, Dob=Sdob, Email=Semail, Mob=Smob, Password=Spass)
        return redirect('login')
    return render(request, 'signup.html')


def bookdetails(request):
    if request.method == "POST":
        BD_bookname = request.POST.get('Bookname')
        BD_code = request.POST.get('Code')
        BD_authorname = request.POST.get('Authorname')
        BD_date = request.POST.get('Date')
        BD_status = request.POST.get('Status')
        BD_bookamount = request.POST.get('Bookamount')
        BD_createdate = request.POST.get('Createdate')
        BD_createby = request.POST.get('Createby')
        BD_updatedate = request.POST.get('Updatedate')
        BD_updateby = request.POST.get('Updateby')
        BD_img=request.FILES['bookimage']

        obj1 = Book_details.objects.create(Book_Name=BD_bookname, Book_code=BD_code, Author_Name=BD_authorname, Date=BD_date, Status=BD_status,
                                           Book_Amount=BD_bookamount, Created_Date=BD_createdate, Created_By=BD_createby, Updated_Date=BD_updatedate, Updated_By=BD_updateby,
                                           Book_Img=BD_img)
        return redirect('bookadmin')
    return render(request, 'bookdetails.html')


def login(request):
    if request.method == "POST":
        User_Name = request.POST.get('username')
        Login_Pass = request.POST.get('login_pass')
        #try:
        get_userpass = user_signup.objects.get(
                Name=User_Name, Password=Login_Pass)
        request.session['username']=get_userpass.Name
        if get_userpass.status==1:
                return redirect('bookshow')
        else:
                return redirect('bookadmin')
        #except:
        pass
    return render(request,'login.html')


def bookdmin(request):
    obj = Book_details.objects.all()
    return render(request, 'bookadmin.html', {'obj': obj})


def updatebook(request, pk):
    obj = Book_details.objects.get(id=pk)
    if request.method == 'POST':
        update = Book_details.objects.filter(id=pk).update(Book_Name=request.POST.get('Bookname'), Book_code=request.POST.get(
            'Code'), Author_Name=request.
            POST.get('Authorname'), Date=request.POST.get('date'), Book_Amount=request.POST.get('Bookamount'),
            Book_Img=request.FILES['uploadnew'])
        return redirect('bookadmin')
    return render(request, 'updatebook.html', {'obj': obj})

def deletebook(request,pk):
    print("pk")
    print(pk)
    obj=Book_details.objects.filter(id=pk).delete()
    return redirect('bookadmin')

def bookshow(request):
    aa1=request.session['username']
    obj = Book_details.objects.all()
    if request.method=='POST':

        aa=request.POST.get('searchbook')
        # bb=request.POST.get('searchcode')
        conditons=''
        if aa !='':
            conditons=Q(Book_Name__icontains=aa)
        # if bb !='' and conditons=='':
        #     conditons=Q(Book_Code__icontains=bb)
        # if bb !='' and conditons !='':
        #     conditons &=Q(Book_Code__icontains=bb)
        if conditons !='':
            obj=Book_details.objects.filter(conditons)

    return render(request,'bookshow.html', {'obj': obj,'name':aa1})

def takebook(request,pk):
    obj=Book_details.objects.filter(id=pk).update(Status='Unavailable')
    return redirect('bookshow')

def returnbook(request,pk):
    obj=Book_details.objects.filter(id=pk).update(Status='Available')
    return redirect('bookshow')

@api_view(['GET','POST'])
def restapidemo(request):
    if request.method == 'GET':
        obj=list(Book_details.objects.all().values())
    if request.method == 'POST':
        import json
        a=json.loads(request.body)
        print(a['name'])
        obj={"message":"ok"}
    
    return JsonResponse({"Message":obj})