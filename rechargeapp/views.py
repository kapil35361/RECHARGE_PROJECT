from django.shortcuts import render,redirect
from rechargeapp.models import Airtelplans,VIplans,Jioplans,recharge
from rechargeapp.serializers import Airtelserializer,VIserializer,Jioserializer,rechargeserializer
from rest_framework import mixins,generics
from rest_framework import viewsets
from rechargeapp.form import rechargeform



class Airtel_recharge(viewsets.ModelViewSet):
    queryset=Airtelplans.objects.all()
    serializer_class=Airtelserializer



    

class VI_recharge(viewsets.ModelViewSet):
    queryset=VIplans.objects.all()
    serializer_class=VIserializer
'''
    def get(self,request):
        return self.list(request) 

    def post(self,request):
        return self.create(request)    

'''

class Jio_recharge(viewsets.ModelViewSet):
    queryset=Jioplans.objects.all()
    serializer_class=Jioserializer
'''
    def get(self,request):
        return self.list(request) 

    def post(self,request):
        return self.create(request)                  


'''

class Mobilerecharge(viewsets.ModelViewSet):
    queryset=recharge.objects.all()
    serializer_class=rechargeserializer


def Airtelrecharge(request,**kwargs):
    airtel=recharge.objects.filter(Airtelplans_id=(kwargs['pk']))
    response=[]
    for each in airtel:
        response.append(each)
    
    
    form=rechargeform()
    if request.method=='POST':
        form=rechargeform(request.POST)
        if form.is_valid():
            form.save()
           
         
    return render(request,'rechargeapp/airtel.html', {'form':form,'airtel':response})


def VIrecharge(request,**kwargs):
    VI=recharge.objects.filter(VIplans_id=(kwargs['pk']))
    response=[]
    for each in VI:
        response.append(each)
    
    
    form=rechargeform()
    if request.method=='POST':
        form=rechargeform(request.POST)
        if form.is_valid():
            form.save()
           
         
    return render(request,'rechargeapp/vi.html', {'form':form,'VI':response})



def VIrecharge(request,**kwargs):
    Jio=recharge.objects.filter(Jioplans_id=(kwargs['pk']))
    response=[]
    for each in Jio:
        response.append(each)
    
    
    form=rechargeform()
    if request.method=='POST':
        form=rechargeform(request.POST)
        if form.is_valid():
            form.save()
           
         
    return render(request,'rechargeapp/jio.html', {'form':form,'Jio':response})