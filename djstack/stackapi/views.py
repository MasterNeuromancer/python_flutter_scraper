from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Question
from .serializer import QuestionSerializer
from bs4 import BeautifulSoup

import requests
import json

# Create your views here.

def index(request):
    return HttpResponse('Success')

class QuestionApi(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

def latest(request):
    try:
        res = requests.get('https://stackoverflow.com/questions')

        soup = BeautifulSoup(res.text, 'html.parser')

        questions = soup.select('.question-summary')
        for question in questions:
            q = question.select_one('.question-hyperlink').getText()
            vote_count = question.select_one('.vote-count-post').getText()
            views = question.select_one('.views').attrs['title']
            tags = [i.getText() for i in (question.select('.post-tag'))]

            question = Question()
            question.question = q
            question.vote_count = vote_count
            question.views = views
            question.tags = tags

            question.save()
        return HttpResponse('Latest Data Fetched from Stack Overflow')
    except Exception as e:
        return HttpResponse(f'Failed {e}')