import json
from datetime import datetime
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import View


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


class AddView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        a = float(data['A'])
        b = float(data['B'])
        try:
            if request.path.split('/')[1] == 'add':
                result = a + b
            elif request.path.split('/')[1] == 'subtract':
                result = a - b
            elif request.path.split('/')[1] == 'multiply':
                result = a * b
            elif request.path.split('/')[1] == 'divide':
                result = a / b
            else:
                result = None
            return JsonResponse({
                'result': result
            })
        except Exception as e:
            response = JsonResponse({
                'error': str(e)
            })
            response.status_code = 400
            return response











