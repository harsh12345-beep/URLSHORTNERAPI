import imp
from multiprocessing import context
from textwrap import shorten
from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
import pyshorteners
@api_view(['post'])
def UrlShortner(request):
    serializer  = UrlShortnerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save
        x = serializer.data #created varialbel to change the data in dictiolnary
        y = dict(x) #changad the data in dictionary
        z=y.values() #Getting the values from dictionary
        A = list(z) #typecasting in list        
        B = A[0] #storing data in the variable
        shor = pyshorteners.Shortener()
        C = shor.tinyurl.short(B)
        print(C)
    return Response(serializer.data)

