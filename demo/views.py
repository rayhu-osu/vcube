from django.http import  HttpResponseRedirect
from .models import Number
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .a import excelToWeb, webToExcel

def index(request):
    number_list = Number.objects.all()
    context = {'number_list': number_list}
    return render(request, 'demo/index.html', context)

def detail(request, number_id1):
    aNumber = get_object_or_404(Number, pk=number_id1)
    return render(request, 'demo/detail.html', {'number': aNumber})


def results(request, number_id2):

    key = int(number_id2) + 16

    number = get_object_or_404(Number, pk=key)

    excel_list = excelToWeb()

    web_list = [number.number_1, number.number_2]

    webToExcel(number.number_1, number.number_2)

    return render(request, 'demo/results.html', {'excel_list': excel_list, "web_list": web_list})


def vote(request, number_id):
    firstNum = Number.objects.all().first()

    number1 = request.POST['number1']
    number2 = request.POST['number2']

    aNewNumber = Number (number_1=number1, number_2=number2)

    aNewNumber.save()
    firstNum.delete()


    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('demo:results', args=(number_id)))