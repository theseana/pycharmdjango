from django.http import HttpResponse


def greeting(request):
    return HttpResponse("Hello welcome to MyBlog")