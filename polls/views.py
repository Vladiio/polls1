from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import Response
from rest_framework.decorators import api_view

from .serializers import QuestionSerializer
from .models import Question


@api_view(['GET'])
def index(req):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response({"questions": serializer.data})


@api_view(['POST'])
def create_poll(req):
    print(req.data)
    
    return Response({})