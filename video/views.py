from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
from .models import Video, Category,Tag
from . import models
from helpers import pagination_data



def make_paginator(objects,page,num= 8):
    paginator = Paginator(objects, num)
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)
    return object_list,paginator


def index(request):
   videos = models.Video.objects.all()
   page = request.GET.get('page', 1)
   videos, paginator = make_paginator(videos, page)
   page_data = pagination_data(paginator, page)


   return render(request, 'video/index.html', locals())





def video_detail(request,pk):
    videos = models.Video.objects.get(id=pk)
    videos.increase_view_count()
    return render(request, 'video/detail.html', locals())


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    videos = Video.objects.filter(category=cate)

    paginator = Paginator(videos, 12)

    try:
        page = int(request.GET.get('page', 1))
        videos = paginator.page(page)
    except(EmptyPage, InvalidPage, PageNotAnInteger):
        datas = paginator.page(1)

    return render(request, 'video/category_content.html', locals())
#
def tag(request, pk):
    t = get_object_or_404(Tag, pk=pk)
    videos = Video.objects.filter(tag=t)

    paginator = Paginator(videos, 12)

    try:
        page = int(request.GET.get('page', 1))
        videos = paginator.page(page)
    except(EmptyPage, InvalidPage, PageNotAnInteger):
        datas = paginator.page(1)

    return render(request, 'video/tags.html', locals())




def all(request):
    videos = models.Video.objects.all()
    page = request.GET.get('page', 1)
    videos, paginator = make_paginator(videos, page)
    page_data = pagination_data(paginator, page)

    return render(request,'video/all.html', locals())


def all_tag(request):
    videos = models.Video.objects.all()
    page = request.GET.get('page', 1)
    videos, paginator = make_paginator(videos, page)
    page_data = pagination_data(paginator, page)
    return render(request,'video/all_tags.html', locals())

def introduction(request):

    return render(request, 'base/introduction.html')