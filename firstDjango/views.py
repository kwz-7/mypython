from django.http import HttpResponse
#编写视图处理函数，一个函数相当于是一个试图
def run_views(request):
    return HttpResponse("<h1>第一个响应</h1>")