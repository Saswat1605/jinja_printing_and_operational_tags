from django.shortcuts import render

# Create your views here.
def data_render(request):
    d={'name':'ashu','age':13,'hobbies':['cricket','football']}
    return render(request,'data_render.html',context=d)


def conditions(request):
    d={'a':5,'b':8}
    return render(request,'conditions.html',context=d)

def if_elif_else(request):
    d={'a':20,'b':30}
    return render(request,'if_elif_else',context=d)