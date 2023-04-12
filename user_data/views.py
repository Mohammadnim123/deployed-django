from datetime import datetime
import pycountry
from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
def get_user_data(request):
    country = request.META.get("HTTP_X_VERCEL_IP_COUNTRY")
    country_name = pycountry.countries.get(alpha_2=country).name +  pycountry.countries.get(alpha_2=country).flag if country else None
    timezone = request.META.get("HTTP_X_VERCEL_IP_TIMEZONE")
    return JsonResponse({"country_name": country_name,
                        "timezone": timezone}, safe=False)
