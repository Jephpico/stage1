import string
from tkinter.tix import INTEGER
from tokenize import String
from xmlrpc.client import Boolean
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Slackdeets
import json
from django.http import JsonResponse

# Create your views here.


class SlackdeetViews(APIView):

    def get(self, request):
        slackdeets = {"slackUsername": "Lee", "backend": True, "age": 27, "bio":"my name is lee, and i have just one goal here; becoming a finalist!"}
        #json_slackdeet = json.dumps(slackdeets, safe=False)
        return JsonResponse(slackdeets)