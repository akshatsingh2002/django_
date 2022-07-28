from http.client import HTTPResponse
from django.shortcuts import HttpResponse
def index(request):
    ans = request.GET['number']
    ans = int(ans)**2
    print(ans)
    return HttpResponse(f'{ans}')