from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LoginSerializer


csrf_exempt_method = method_decorator(csrf_exempt)


def check_authentication(request):
    print(request.user.is_authenticated)
    return JsonResponse({'authenticated': request.user.is_authenticated})



class LoginView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()
    @csrf_exempt_method
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        try:
            login(request, user)
        except Exception as e:
            return Response(str(e), status=400)
        return Response('Logged in successfully', status=201)