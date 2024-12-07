from django.shortcuts import render


# Create your views here.
def f_view(request):
    return render(request, 'func_template.html')


def cl_view(request):
    return render(request, 'class_template.html')
