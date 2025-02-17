from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comment
from django.utils.timezone import now

# Create your views here.



def home(request):
    return render(request, "home.html")


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, is_published=True)

    if request.method == "POST" and request.user.is_authenticated:
        comment_content = request.POST.get("comment")
        if comment_content:
            Comment.objects.create(
                article=article,
                user=request.user,
                content=comment_content,
                created_at=now(),
            )
        return redirect("article_detail", slug=article.slug)

    return render(request, "article.html", {"article": article})