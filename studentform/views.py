
from django.http import HttpResponse

def home(request):
    return HttpResponse("Student Form Homepage (Form logic goes here)")