from django.shortcuts import render,HttpResponse
from django.shortcuts import redirect
from.models import *
from django.contrib.auth import authenticate,logout,login
from datetime import date
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
def home(request):
    allblog=Blog.objects.all()
    start_three_blog=allblog[:3]
    lastblog=allblog[len(allblog)-1]
    allblog=allblog[::-1]
    last_four_blog=allblog[2:6]
    d={"lastblog":lastblog,"last_four_blog":last_four_blog,"start_three_blog":start_three_blog}

    return render(request,'index.html',d)
def about(request):
    return render(request, 'about.html')
def contact(request):
    if request.method=='POST':
        dic=request.POST
        n=dic['name']
        e=dic['email']
        s=dic['subject']
        m=dic['msg']
        message.objects.create(name=n,email=e,subject=s,message=m)
        return redirect('home')

    return render(request, 'contact.html')
def foods(request,cid):
    catdata=category.objects.get(id=cid)
    foodblog=Blog.objects.filter(cat=catdata)
    paginator=Paginator(foodblog,6)
    page=request.GET.get('page',1)
    try:
        blog=paginator.page(page)
    except PageNotAnInteger:
        blog=paginator.page(1)
    except EmptyPage:
        blog=paginator.page(paginator.num_pages)
    d={"foodblog":blog}
    return render(request, 'foods.html',d)
def lifestyle(request,cid):
    catdata=category.objects.get(id=cid)
    lifestyleblog = Blog.objects.filter(cat=catdata)
    d = {"lifestyleblog":lifestyleblog }
    return render(request, 'lifestyle.html',d)
def fashion(request,cid):
    catdata=category.objects.get(id=cid)
    fashionblog = Blog.objects.filter(cat=catdata)
    d = {"fashionblog": fashionblog}
    return render(request, 'fashion.html', d)
    return render(request,'fashion.html')

def blog_detail(request,bid):

    allcat=category.objects.all()
    allcat=allcat[0:5]
    blog_data=Blog.objects.get(id=bid)
    comment_data=user_comment.objects.filter(blogdata=blog_data)
    comment_data=comment_data[ : :-1]
    comment_data=comment_data[ :6]
    allblog = Blog.objects.all()
    allblog = allblog[::-1]
    last_four_blog = allblog[2:6]

    if request.method == 'POST':
        dic = request.POST
        usr = request.user
        c = dic['comment']
        i = request.FILES['img']
        user_comment.objects.create(blogdata=blog_data, usr=usr, comment=c, images=i)
        return redirect('home')


    d={"blog_data":blog_data,"comment_data":comment_data,"allcat":allcat,"recent_blog":last_four_blog}
    return render(request,'blog_detail.html',d)

def user_blog_form(request):
    if not request.user.is_authenticated:
        return redirect("login")
    allcategory=category.objects.all()
    d={"allcategory":allcategory}
    if request.method=='POST':
        dic=request.POST
        c=dic['cat_id']
        catdata=category.objects.get(id=c)
        t=dic['title']
        s=dic['short']
        l=dic['long']
        i=request.FILES['img']
        u=request.user
        d=date.today()
        Blog.objects.create(cat=catdata,title=t,sdes=s,long_des=l,usr=u,images=i,date=d)
        return redirect('home')

    return render(request,'add_blog_form.html',d)
def admin_category_form(request):
    if request.method == 'POST':
        dic = request.POST
        t = dic['add_cat']
        category.objects.create(name=t)
        return redirect('home')
    return render(request,'add_category_form.html')
def signup(request):
    error=False
    if request.method=='POST':
        dic=request.POST
        fn=dic['first']
        ln=dic['last']
        u=dic['user']
        e=dic['email']
        p=dic['pass']
        i=request.FILES['img']
        m=dic['mobile']
        user=User.objects.filter(username=u)
        if user:
            error=True
        else:
            userdata=User.objects.create_user(username=u,password=p,first_name=fn,last_name=ln,email=e)
            user_detail.objects.create(usr=userdata,images=i,mobile_no=m)
            return redirect("login")
    d={"error":error}
    return render(request,'signup.html',d)
def login_user(request):
    error=False
    if request.method=="POST":
        dic=request.POST
        u=dic['user']
        p=dic['pass']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect("home")
        else:
            error=True
    d={"error":error}
    return render(request,'login.html',d)
def logout_user(request):
    logout(request);
    return redirect("home")

def user_dashboard(request,type):

    blogdata=Blog.objects.filter(usr=request.user)
    userdata=user_detail.objects.filter(usr=request.user).first()
    c1=''
    c2=''
    if type=='MyBlog':
        c1='active'
    elif type=='profile':
        c2='active'
    d={"type":type,"class1":c1,"class2":c2,"blogdata":blogdata,"userdata":userdata}
    return render(request,'dashboard.html',d)
def blog_like(request,bid):
    user=request.user
    blogdata=Blog.objects.get(id=bid)
    data=like_blog.objects.filter(usr=user,blog_like=blogdata)
    if not data:
        like_blog.objects.create(usr=request.user,blog_like=blogdata)
    else:
        data.delete()
    return redirect('blog_detail',bid)
def edit_blog(request,bid):
    blogdata=Blog.objects.get(id=bid)
    allcat=category.objects.all()
    d={"blog_data":blogdata,"allcat":allcat}
    return render(request,'edit_blog.html',d)
def delete_blog(request,bid):
    blogdata=Blog.objects.get(id=bid)
    blogdata.delete()
    return redirect('home')





