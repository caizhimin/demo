from django.http import JsonResponse
from django.http import Http404


def echo(request):
    msg = request.GET.get('msg')
    if msg:
        response = {'msg': msg}
        return JsonResponse(response)
    else:
        raise Http404
