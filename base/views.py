from unicodedata import name
from django.shortcuts import render
from .models import Category,Tag,Post
# Create your views here.
from django.db.models import Q

def homeView(request):
    
    categories = Category.objects.all()
    posts = Post.objects.all()[:1]
    latestposts = Post.objects.all()[1:4]
    eachcategory = {category: Post.objects.filter(category = category) for category in Category.objects.all()}
    context = {'categories':categories,'posts':posts,'latestposts':latestposts,'eachcategory':eachcategory}
    if 'q' in request.GET:
        q = request.GET['q']
        search = Q(Q(title__icontains = q) | Q(description__icontains = q))
        results = Post.objects.filter(search)
        context ={'results':results,'q':q,'categories':categories}
        return render(request, 'base/searchresult.html', context)
    return render(request,'base/home.html',context)

def detailView(request,slug):
    categories = Category.objects.all()
    post = Post.objects.get(slug=slug)
    post.views = post.views+1
    post.save()
    post_tags = post.tags.all()
    similarposts = Post.objects.filter(tags__in = post_tags).exclude(slug=slug)
    tags = Tag.objects.all()
    popularposts = Post.objects.order_by('-views')[:4]
    context = {'categories':categories,'post':post,'popularposts':popularposts,'tags':tags,'similarposts':similarposts}
    if 'q' in request.GET:
        q = request.GET['q']
        search = Q(Q(title__icontains = q) | Q(description__icontains = q))
        results = Post.objects.filter(search)
        context ={'results':results,'q':q,'categories':categories}
        return render(request, 'base/searchresult.html', context)
    return render(request,'base/detail.html',context)

def categoryView(request,slug):
   
    categories = Category.objects.all()
    category = Category.objects.get(slug=slug)
    categoryposts = Post.objects.filter(category=category)
    context = {'categories':categories,'categoryposts':categoryposts,'slug':slug}
    if 'q' in request.GET:
        q = request.GET['q']
        search = Q(Q(title__icontains = q) | Q(description__icontains = q))
        results = Post.objects.filter(search)
        context ={'results':results,'q':q,'categories':categories}
        return render(request, 'base/searchresult.html', context)
    return render(request,'base/categorypost.html', context)

def tagView(request,slug):
   
    categories = Category.objects.all()
    tags = Tag.objects.get(slug=slug)
    tagposts = Post.objects.filter(tags=tags)
    context = {'categories':categories,'tagposts':tagposts,'slug':slug}
    if 'q' in request.GET:
        q = request.GET['q']
        search = Q(Q(title__icontains = q) | Q(description__icontains = q))
        results = Post.objects.filter(search)
        context ={'results':results,'q':q,'categories':categories}
        return render(request, 'base/searchresult.html', context)
    return render(request,'base/tagpost.html', context)

def aboutView(request):
    
    categories = Category.objects.all()
    context = {'categories':categories}
    if 'q' in request.GET:
        q = request.GET['q']
        search = Q(Q(title__icontains = q) | Q(description__icontains = q))
        results = Post.objects.filter(search)
        context ={'results':results,'q':q,'categories':categories}
        return render(request, 'base/searchresult.html', context)
    return render(request,'base/about.html', context)

def contactView(request):
    
    categories = Category.objects.all()
    context = {'categories':categories}
    if 'q' in request.GET:
        q = request.GET['q']
        search = Q(Q(title__icontains = q) | Q(description__icontains = q))
        results = Post.objects.filter(search)
        context ={'results':results,'q':q,'categories':categories}
        return render(request, 'base/searchresult.html', context)
    return render(request,'base/contact.html', context)
