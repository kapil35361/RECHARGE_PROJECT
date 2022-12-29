from django import forms


class rechargeform(forms.Form):
    OPERATOR=[('airtel','AIRTEL'),('vi','VI'),('jio','JIO')]
    mobilenumber=forms.CharField(max_length=20)
    operator=forms.CharField(widget=forms.Select(choices=OPERATOR),max_length=20)
    price=forms.DecimalField()