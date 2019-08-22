from django.http import HttpResponse


def some(request):
    return HttpResponse('Some page')


def sometwo(request):
    return HtppResponse('Some-two page')