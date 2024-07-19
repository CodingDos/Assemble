from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Hackathon, Team, Skill
from .serializers import UserSerializer, HackathonSerializer, TeamSerializer, SkillSerializer

# Create your views here.

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class HackathonList(generics.ListAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer

class HackathonDetail(generics.RetrieveUpdateAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer

class TeamListCreate(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class SkillList(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
