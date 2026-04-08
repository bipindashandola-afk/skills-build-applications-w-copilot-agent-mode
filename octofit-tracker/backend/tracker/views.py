from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import User, Team, Workout, Activity, Leaderboard
from octofit_tracker.serializers import UserSerializer, TeamSerializer, WorkoutSerializer, ActivitySerializer, LeaderboardSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request, format=None):
    return Response({
        'users': '/api/tracker/users/',
        'teams': '/api/tracker/teams/',
        'workouts': '/api/tracker/workouts/',
        'activities': '/api/tracker/activities/',
        'leaderboard': '/api/tracker/leaderboard/',
        'health': '/api/tracker/health/',
    })

@api_view(['GET'])
@permission_classes([AllowAny])
def tracker_root(request):
    return api_root(request)

@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    return Response({'status': 'ok', 'service': 'OctoFit Tracker backend'})
