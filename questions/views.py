from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Question, User
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import QuestionsSerializer, UserSerializer


class QuestionsView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'questions.html'

    def get(self, request):
        questions = get_object_or_404(Question)
        serializer = QuestionsSerializer(questions)
        return Response({'serializer': serializer, 'questions': questions})

    def post(self, request):
        questions = get_object_or_404(Question)
        serializer = QuestionsSerializer(questions, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'questions': questions})
        serializer.save()
        # return redirect('dawd')


class UserView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user.html'

    def get(self, request):
        user = get_object_or_404(User)
        serializer = UserSerializer(user)
        return Response({'serializer': serializer, 'profile': user})

    def post(self, request):
        user = get_object_or_404(User)
        serializer = UserSerializer(user, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': user})
        serializer.save()
        return redirect('/')
