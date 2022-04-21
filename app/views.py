
from urllib import request
from django.shortcuts import render
from .serializers import StudentSerializers
from .models import Student
import io
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer

from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method == 'Post':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializers(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'data':'created'}
            return JsonResponse(res)
        json_data = JSONRenderer.render(serializer.errors)
        return JsonResponse(json_data)

