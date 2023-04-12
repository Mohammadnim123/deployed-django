from datetime import datetime
import pycountry
from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
def get_user_data(request):
    keys_to_get = [
        "HTTP_X_VERCEL_IP_COUNTRY",
        "HTTP_X_VERCEL_IP_TIMEZONE"
    ]
    values = {key: request.META.get(key) for key in keys_to_get}

    country = pycountry.countries.get(alpha_2=values["HTTP_X_VERCEL_IP_COUNTRY"])

    return JsonResponse({"country_name": country.name,
                        "country_flag": country.flag,
                        "timezone": values["HTTP_X_VERCEL_IP_TIMEZONE"]}, safe=False)
