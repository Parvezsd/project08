from django.shortcuts import render # type: ignore

# Create your views here.
def app11(request):
    d={'name':'parvez'}
    return render(request,'app11.html',context=d) # type: ignore