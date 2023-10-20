from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Apply
from django.shortcuts import render, get_object_or_404
from .forms import ApplyForm
from django.shortcuts import redirect

def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all()
    print(posts)
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = ApplyForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = 'a'
            post.published_date = timezone.now()
            post.save()
        return redirect('post_list')
    else:
        form = ApplyForm()
    return render(request, 'blog/post_edit.html', {'form': form})

