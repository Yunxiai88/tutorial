from django.shortcuts import render
from .models import Snippet
from .serializers import SnippetSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404, HttpResponse

def index(request):
    return HttpResponse('hello...')

class SnippetList(APIView):
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        obj = SnippetSerializer(snippets, many=True)
        return Response(obj.data)
    
    def post(self, request, format=None):
        obj = SnippetSerializer(data=request.data)
        if obj.is_valid():
            obj.save()
            return Response(obj.data, status=status.HTTP_201_CREATED)
        return Response(obj.errors, status=status.HTTP_400_BAD_REQUEST)

class SnippetDetail(APIView):
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        obj = SnippetSerializer(snippet)
        return Response(obj.data)
    
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        obj = SnippetSerializer(snippet, data=request.data)
        if obj.is_valid:
            obj.save()
            return Response(obj.data)
        else:
            Response(obj.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, pk, format=None):
        snippet = self.get_object()
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
"""
@csrf_exempt
@api_view(['POST', 'GET'])
def snippet_list(request, format=None):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        obj = SnippetSerializer(data=request.data)
        if obj.is_valid():
            obj.save()
            return Response(obj.data, status=status.HTTP_201_CREATED)
        return Response(obj.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""