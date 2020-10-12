import json
from datetime import datetime
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

def get_token_view(request, *args, **kwargs):
    if request.method == 'Get':
        return HttpResponse()
    return HttpResponseNotAllowed('Only get request are alowed')


@ensure_csrf_cookie
def json_echo_view(request, *args, **kwargs):
    answer = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'method': request.method,
    }
    if request.method == 'POST':
        data = json.loads(request.body)
        answer['data'] = data
    return JsonResponse(answer)




