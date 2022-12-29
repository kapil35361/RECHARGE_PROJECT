from rest_framework import serializers 
from rechargeapp.models import Airtelplans,VIplans,Jioplans,recharge




class Airtelserializer(serializers.ModelSerializer):
    class Meta:
        model=Airtelplans
        fields='__all__'



class VIserializer(serializers.ModelSerializer):
    class Meta:
        model=VIplans
        fields='__all__'

class Jioserializer(serializers.ModelSerializer):
    class Meta:
        model=Jioplans
        fields='__all__'        


class rechargeserializer(serializers.ModelSerializer):
    class Meta:
        model=recharge
        fields='__all__'