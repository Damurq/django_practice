"""views"""

from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse

def hello(request):
    return HttpResponse("Hellos")

#/?numbers=1,5,4,7,8,9,2,3,4
def hi(request):
    numbers = map(lambda x : int(x),request.GET["numbers"].split(","))#return a map object
    return JsonResponse({ "numbers" : sorted(numbers)},json_dumps_params={'indent': 4})

#/?numbers=1,5,4,7,8,9,2,3,4
def hi2(request):
    numbers= sorted([int(i) for i in request.GET['numbers'].split(",")])
    return HttpResponse(numbers,content_type="application/json")

#    path('hi/<str:name>/<int:age>/', local_views.say_hi),
def say_hi(request, name, age):
    """Return a greeting."""
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to Platzigram'.format(name)
    return HttpResponse(message)
