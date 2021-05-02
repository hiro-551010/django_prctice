from django.shortcuts import render
from django.http import HttpResponse

def add(request, num1, num2):
    num = num1 + num2
    return HttpResponse(f'<h1>{num}<h1>')

def minus(request, num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    num = num1 - num2
    return HttpResponse(f'<h1>{num}<h1>')

def div(request, num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    num = round(num1 / num2)
    return HttpResponse(f'<h1>{num}<h1>')