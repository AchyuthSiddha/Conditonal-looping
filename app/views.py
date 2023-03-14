from django.shortcuts import render

# Create your views here.
def Condition(request):
    d={'a':101,'b':3011,'c':302}
    # d={'name':'achyuth'}
    return render(request,'Condition.html',d)
def loops(request):
    d={'name':'Achyuth'}
    return render(request,'loops.html',d)