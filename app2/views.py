from django.shortcuts import render # type: ignore

# Create your views here.
def app12(request):
    d={'name':'deepak'}
    return render(request,'app12.html',context=d) # type: ignore