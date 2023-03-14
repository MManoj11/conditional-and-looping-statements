from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':350,'b':300,'c':200}
    return render(request,'conditions.html',d)


def loops(request):
    d={'name':'manoj'}
    return render(request,'loops.html',d)
