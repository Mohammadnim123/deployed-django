import json
from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
def get_user_data(request):
    class CustomEncoder(DjangoJSONEncoder):
        def default(self, obj):
            return str(obj)

    meta_data = json.loads(json.dumps(request.META, cls=CustomEncoder))
    return JsonResponse(meta_data, safe=False)
