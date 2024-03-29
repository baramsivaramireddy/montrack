from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import Http404, HttpResponse,HttpResponseRedirect ,HttpResponseNotFound,JsonResponse
from .models import stats ,took ,gave,expenses

from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
 

from decimal import Decimal
#  serializer for take and gave

class gaveSerializer(serializers.ModelSerializer):
    class Meta :
        model = gave
        fields = '__all__'



class tookSerializer(serializers.ModelSerializer):
    class Meta :
        model = took
        fields = '__all__'

class ExpensesSerializer(serializers.ModelSerializer):
    class Meta :
        model = expenses
        fields = '__all__'  
class statsSerializer(serializers.ModelSerializer):
    class Meta :
        model = stats
        fields = '__all__'


def index(request):

    if request.user.is_authenticated :
        return HttpResponseRedirect("/stat")
    if request.method == "POST":
       username = request.POST['username'] 
       password = request.POST['password']
       user = authenticate(username=username, password=password)

       if user :
           login(request, user)
           return HttpResponseRedirect('stat')
       else :
           return HttpResponseNotFound("wrong password")
                                                          
    else : 
        return render(request,'track/index.html')




def stat(request):
    if not request.user.is_authenticated :
        return HttpResponseRedirect("/")

    try : 
        context = {
            "stat":stats.objects.get(pk=1),    
        }
    except :
        context = {
            'stat':0
        }
    return render(request,'track/stat.html',context)




def add_view(request):
    if not request.user.is_authenticated :
        return HttpResponseRedirect("/")
    return render(request,'track/add.html')


def add(request):
    if request.user.is_authenticated :
        amount  = request.POST['amount']
        purpose  = request.POST['purpose']
        category  = request.POST['category']

        if category == "mama":
            new_instance = took(amount=amount,purpose =purpose)
            try :
                total_taken = stats.objects.get(pk=1)
                total_taken.took += Decimal(amount)
                total_taken.save()
            except :
                stats(gave=0,took=Decimal(amount),expenses=0).save()
            new_instance.save()
        elif category == "expenses" :
            new_instance = expenses(amount=amount,purpose =purpose)
            try :
                total_expense = stats.objects.get(pk=1)
                total_expense.expenses += Decimal(amount)
                total_expense.save()
            except :
                stats(gave=0,took=0, expenses=Decimal(amount)).save()
            new_instance.save()
            

        else :
            new_instance = gave(amount=amount,purpose =purpose)
            try :
                total_given = stats.objects.get(pk=1)
                total_given.gave += Decimal(amount)
                total_given.save()
            except :
                stats(gave=Decimal(amount),took=0,expenses=0).save()
            new_instance.save()
        return  HttpResponseRedirect('/add')
        

    else :
        return HttpResponseRedirect('/')


@api_view()
def all_took(request):
    data    =   took.objects.all()
    
    json = tookSerializer(data,many=True)
    return Response(json.data)

@api_view()
def expenses_view(request):
    data    =   expenses.objects.all()
    json = ExpensesSerializer(data,many=True)
    return Response(json.data)

@api_view()
def all_gave(request):
    data    =   gave.objects.all()
    json    =          gaveSerializer(data,many=True)
    return Response(json.data)


@api_view()
def all_stats(request):
    data    =   stats.objects.all()
    json    =          statsSerializer(data,many=True)
    return Response(json.data)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

