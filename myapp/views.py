# from django.shortcuts import render
# from .forms import sos , sosform


# # Create your views here.
# def sos(request):
#     print("Hello")
#     if request.method == 'POST':
#         form = sos(request.POST)
#         if form.is_valid():

#             La = form.cleaned_data['La']
    

#     form = sos()
#     return render(request, 'sos.html', {'form': form} )

# def sos_details(request):
#     if request.mthod == 'POST':
#         form = sosform(request.POST)
#         if form.is_valid():
#             form.save()
#             print("Sucessfully completed")

#     form = sosform()
#     return render(request, 'sos.html', {'form': form} )
from django.shortcuts import redirect, render
from .forms import *
from .models import *

def sos_form_view(request):
    if request.method=='POST':
        La = request.POST.get('La')
        Wp = request.POST.get('Fp')
        Sn = request.POST.get('Sn')
        Ws = request.POST.get('Ws')
        Cn = request.POST.get('Cn')
        user = request.user
        print("hello")
        person = so1(user=user,La=La,Fp=Wp,Sn=Sn,Ws=Ws,Ca=Cn)
        person.save()
        redirect('sos')
    return render(request, 'sos.html')