from knox.models import AuthToken
from knox.views import LoginView
from django.contrib.auth import login
from rest_framework import permissions, status, viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.response import Response
from .serializers import ListOfQuestionSerializer, AnswerSerializer, RegisterSerializer, UserSerializer
from .models import ListOfQuestion


class ListOfQuestionsView(viewsets.ReadOnlyModelViewSet):
    queryset = ListOfQuestion.objects.all()
    serializer_class = ListOfQuestionSerializer
    permission_classes = (permissions.AllowAny,)


class AnswerView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AnswerSerializer

    def post(self, request):
        print(request.user)
        answer = self.get_serializer(data=request.data, context=request)
        if answer.is_valid(raise_exception=True):
            answer = answer.save()
            return Response(answer.result, status=status.HTTP_200_OK)


class LoginAPIView(LoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPIView, self).post(request, format=None)


class RegistrationView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
