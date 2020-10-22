from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password #(최종인)
from .models import CustomUser #(최종인)
from .forms import ImageForm, ProfileForm

# Create your views here.
def home(request):
    return redirect("login")

def register(request): #회원가입(최종인)
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pwd = request.POST['password']
        c_pwd = request.POST['check_password']
        weight = request.POST['weight']  #weight부터 faceLength까지 어떻게 처리해야할지 고민 중(최종인)
        height = request.POST['height']
        fit = request.POST['fit']
        faceLength= request.POST['faceLength']
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
            weight = weight,
            height = height,
            fit = fit,
            faceLength = faceLength,
            #face_img = face_img
        )
        customUser.set_password(pwd) #암호화해서 저장(해쉬...?(최종인))

        customUser.save()

        return redirect("home")
    else: 
        return render(request, "mypage/register.html")
    
def login(request): #로그인(최종인)
    # 안됨 - 404 /쿼리에 해당하는 객체 없다고 뜸(채혜민) --> 해결됨(최종인)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST['password']

        user = get_object_or_404(CustomUser, username = username)

        if check_password(password, user.password):
            request.session['user'] = user.username
            
            return redirect('detail-custom') #로그인 성공하면 입력한 정보를 뜨게 하고 싶은데 반영된 정보가 안보임


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

def detail_custom(request): #내 정보 상세 페이지(채혜민)
    username = request.user.username 
    # username을 받아오는 다른 방법?
    user = get_object_or_404(CustomUser, username = username)
    context = {'user': user}
    return render(request, "mypage/detail.html", context)

@login_required
def edit_custom(request): # 내 정보 수정(채혜민)
    # get current user 
    username = request.user.username
    user = get_object_or_404(CustomUser, username = username)

    # use ProfileForm
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 이미지 수정 어떻게?
            # 수정 내용 디테일 페이지에 반영 안됨/모델도 수정 안되는 것으로 확인
        return redirect('detail_custom')
    else:
        # 기존 instance 받아 돌려주기
        form = ProfileForm(instance=user)
        context = {'form': form}
        return render(request, "mypage/edit.html", context)
