from django import forms

class Formulario(forms.From):
	correo= forms.EmailField()
	mensaje= forms.CharField(max_length=1000)
	nombre= forms.CharField(max_length=100)
