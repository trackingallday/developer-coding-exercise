from django.conf import settings
from django.http import JsonResponse, HttpResponseNotFound
from .models import Post


def post(request, slug):
    post = Post.objects.filter(slug=slug).first()
    if not post:
        return HttpResponseNotFound()
    return JsonResponse({ 'post': post.toJSON() }, safe=False)

def posts(request):
    posts_as_dicts = [p.toJSON() for p in Post.objects.all()]
    return JsonResponse(posts_as_dicts, safe=False)
