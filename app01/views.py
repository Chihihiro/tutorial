from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
import json

def users(request):
    user_list = ['mama', 'fafa']
    return HttpResponse(json.dumps((user_list)))


from django.views import View

class MyView(object):
    def dispatch(self, request, *args, **kwargs):
        print('before')
        ret = super(MyView, self).dispatch(request, *args, **kwargs)
        print('after')
        # func = getattr(self, request.method.lower()) #这等于上面一行
        # ret = func(request, *args, **kwargs)
        return ret


class StudentsView(MyView, View):

    # def dispatch(self, request, *args, **kwargs):
    #     ret = super(StudentsView, self).dispatch(request, *args, **kwargs)
    #     # func = getattr(self, request.method.lower()) #这等于上面一行
    #     # ret = func(request, *args, **kwargs)
    #     return ret

    def get(self, request, *args, **kwargs):
        print('tonguola~~~~~')
        return HttpResponse('GET')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST')

    def put(self, request, *args, **kwargs):
        return HttpResponse('PUT')


class TeacherView(MyView, View):

    # def dispatch(self, request, *args, **kwargs):
    #     ret = super(StudentsView, self).dispatch(request, *args, **kwargs)
    #     # func = getattr(self, request.method.lower()) #这等于上面一行
    #     # ret = func(request, *args, **kwargs)
    #     return ret

    def get(self, request, *args, **kwargs):
        return HttpResponse('GET')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST')

    def put(self, request, *args, **kwargs):
        return HttpResponse('PUT')

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class OrderView(MyView,View):

   def get(self, request, *args, **kwargs):
       return HttpResponse('get')

   def post(self, request, *args, **kwargs):
       return HttpResponse('post')

   def delete(self, request, *args, **kwargs):
       return HttpResponse('delete')