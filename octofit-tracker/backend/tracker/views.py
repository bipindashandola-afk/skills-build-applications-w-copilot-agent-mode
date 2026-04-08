from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([AllowAny])
def tracker_root(request):
    return Response({
        'message': 'OctoFit Tracker API',
        'routes': {
            'health': '/api/tracker/health/',
            'auth': '/api/auth/',
            'registration': '/api/auth/registration/',
        },
    })


@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    return Response({'status': 'ok', 'service': 'OctoFit Tracker backend'})
