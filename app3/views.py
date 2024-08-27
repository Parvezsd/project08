from django.shortcuts import render # type: ignore

# Create your views here.
def app13(request):
    d={'name':'vasavi'}
    return render(request,'app13.html',context=d) # type: ignore