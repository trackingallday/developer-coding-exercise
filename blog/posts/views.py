import os
from django.conf import settings
from collections import Counter
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseServerError
from .models import Post


def post(request, slug):
    # the directory should really be an environment variable
    filepath = os.path.join(settings.BASE_DIR, 'posts/posts', slug + '.md')
    #try to find a matching post we can't find one, return a 404
    try:
        with open(filepath) as f:
            post = Post(content=f.read())
            return JsonResponse({
                'content': post.only_content(),
                'tags': post.tags(),
                'titel': post.title(),
            })
    except FileNotFoundError:
        return HttpResponseNotFound()
    except Exception as e:
        #probably a permissions error
        return HttpResponseServerError()
        

def posts(request):
    posts = []
    # the directory should really be an environment variable
    # not checking for permissions errors or any of the other kinds of errors
    for filename in os.listdir(os.path.join(settings.BASE_DIR, 'posts/posts')):
        if filename.endswith('.md'):
            filepath = os.path.join(settings.BASE_DIR, 'posts/posts', filename)
            with open(filepath) as f:
                post = Post(content=f.read(), slug=filename[:-3])
                posts.append({
                    'slug': post.slug,
                    'title': post.title(),
                })
    return JsonResponse({'posts': posts})
