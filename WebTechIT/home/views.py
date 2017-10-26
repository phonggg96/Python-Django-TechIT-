# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.http import  Http404
from django.urls import reverse
from django.utils.text import slugify

from .forms import  LoginForm, CommnentForm, RegisterForm
from django.shortcuts import render, get_object_or_404, redirect

from .models import DanhMuc, TinTuc, HashTag, Category, LoaiTin, Images, Comment

def index(request):
    posts = TinTuc.objects.all().order_by("-id")[:5]
    congnghes = TinTuc.objects.all().order_by("-id")[10:]
    tintucs = TinTuc.objects.all().order_by("-id")

    danhmucs = DanhMuc.objects.all()
    context = {
        "danhmucs"      : danhmucs,
        "top_post"      : posts[0],
        "posts"         : posts[1:],
        "tinmois"       : posts,
        "noibats"       : posts,
        "tamsucoder"    : tintucs[:5],
        "tintucs"       : tintucs[:5],
        "moinhats"      : posts,
        "top_congnghe"  : congnghes[0],
        "congnghes"     : congnghes[1:],
        "categories"    : Category.objects.order_by('-likes'),
        "loaitins"      : LoaiTin.objects.all(),
        "images"        : Images.objects.all(),
    }
    return render(request, 'home/index.html',context)


def login_view(request):
    title = "Login"
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username     = form.cleaned_data.get("username")
        password     = form.cleaned_data.get("password")
        user         = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect("/")

    return render(request, "login1.html", {"form": form, "title": title,  "danhmucs": DanhMuc.objects.all(),})


def logout_view(request):
    logout(request)

    return redirect(reverse('home:index'))

def register_user_view(request):
    title = "Register"
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()

            return redirect(reverse('home:login'))

    return render(request, "register.html", {"register_form": form })


@login_required #Bắt buộc đăng nhập
def add_comment(request, id):
    if request.method == "POST":
        comment_form = CommnentForm(request.POST, user=request.user, post=TinTuc.objects.get(pk=id))
        if comment_form.is_valid():
            comment_form = comment_form.save(commit=True)
            comment_form.save()
            return redirect(reverse("post-detail", kwargs={"post_id": id}))

    return HttpResponseNotFound()


#@login_required
def post_detail_view(request, slug):
        post = get_object_or_404(TinTuc, slug=slug)
        comment_form = CommnentForm()
        return render(request, 'post/post_detail.html', {
            'tintucs'            : TinTuc.objects.get(slug=slug),
            "danhmucs"           : DanhMuc.objects.all(),
            "tinmois"            : TinTuc.objects.all(),
            "tamsucoder"         : TinTuc.objects.all(),
            'comment_form'       : comment_form,
            "add_comment_action" : reverse("home:new-comment", kwargs={"slug": slug}),

    })

def about_view(request):
    return render(request, 'home/About.html')
