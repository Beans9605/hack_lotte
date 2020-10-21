from django.shortcuts import render, redirect, get_object_or_404 #(최종인)
from django.contrib.auth.hashers import check_password #(최종인)
from .models import CustomUser #(최종인)
from .forms import ImageForm #(최종인)

# Create your views here.

def register(request): #회원가입(최종인)
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pwd = request.POST['password']
        c_pwd = request.POST['check_password']
        #weight = request.POST['weight']  #weight부터 faceLength까지 어떻게 처리해야할지 고민 중(최종인)
        #height = request.POST['height']
        #fit = request.POST['fit']
        #faceLength= request.POST['faceLength']
        #face_img=request.POST['face_img'] #여기에 사진 업로드 하는거를 아직 고민 중(최종인)
        

        if CustomUser.objects.filter(username=username).distinct(): #중복 아이디 존재시 에러(최종인)
            return render(request, "mypage/register.html", {"err1" : "중복 아이디 존재"})

        if pwd != c_pwd : #비밀번호 확인 섹션(최종인)
            return render(request, "mypage/register.html", {"err2" : "암호는 서로 일치해야 합니다."})

        customUser = CustomUser(   
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = email,
            #weight = weight,
            #height = height,
            #fit = fit,
            #faceLength = faceLength,
            #face_img = face_img
        )
        customUser.set_password(pwd) #암호화해서 저장(해쉬...?(최종인))

        customUser.save()

        return redirect("home")
    else: 
        return render(request, "mypage/register.html")
    
def login(request): #로그인(최종인)
    if request.method == "POST":
        username = request.POST['username']
        pwd = request.POST['password']

       
        user = get_object_or_404(CustomUser, username = username)

        if check_password(pwd, user.password):
            request.session['user'] = user.username
            return redirect('home')
        
        else:
            return render(request, "mypage/login.html", {"err": "패스워드가 틀렸습니다."})

    else:
        return render(request, 'mypage/login.html')

def logout(request): #로그아웃(최종인)
    if request.session.get('user', False) :
        request.session.modified = True
        del request.session['user']
        return redirect("home")
    else:
        return redirect("home")


def upload(request): #이미지 업로드 테스트(최종인)
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'mypage/index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'mypage/index.html', {'form': form})
