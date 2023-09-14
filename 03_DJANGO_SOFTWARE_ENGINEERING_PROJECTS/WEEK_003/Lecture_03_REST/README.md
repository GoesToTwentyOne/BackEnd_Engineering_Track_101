# Permissions

## Obsject Level Permissions
```python
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
```
## Setting Policy Permissions Global Permissions
```python
#settings congig
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```
```python
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
```
# Custom Permissions
```python
# permissions Define
from rest_framework import permissions

class AdminorReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            bool(request.user and request.user.is_staff)
            
class ReviewerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.user == request.user or request.user.is_superuser
```
```python
# Apply
from django.shortcuts import render
from rest_framework import viewsets
from my_app.models import Product,ProductReview
from rest_framework.permissions import IsAuthenticated
from my_app.serilizers import ProductSerializer,ProductReviewSerializer
from my_app.permissions import AdminorReadOnly,ReviewerOrReadOnly
# Create your views here
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AdminorReadOnly]   #custom permission classes
class ProductReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [ReviewerOrReadOnly]   #custom permission classes
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
```
# Token Authenticaiton

## Enable Token Authentication
```python
INSTALLED_APPS = [
    ...
    'rest_framework.authtoken'
]
```
```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}
```
```text
manually create token and test credentials
```
## Login
```python
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('login/',obtain_auth_token,name="login"),
    path('register/',RegistrationView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
]

```
## Registration
```python
#Serializer
from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type":'password'}, write_only='True')
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password':{'write_only' : True}
        }
    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'error': 'password does not matched'})
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({'error': 'email already exists'})
        account = User(username= username, email = email)
        account.set_password(password)
        account.save()
        return account

```
```python
# signals
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
```
```python
# views
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework import serializers,status
from rest_framework.response import Response
from rest_framework.views import APIView
from userapp.serializers import RegistrationSerializer
from userapp.signals import *
# Create your views here.
class RegistrationView(APIView):
    def post(self, request):
        data={}
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account=serializer.save()
            data['response']='Registration successful'
            data['username']=account.username
            data['email']=account.email
            token=Token.objects.get(user=account).key
            data['token']=token
        else:
            data=serializer.errors
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(data)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
```python
#urls
    path('register/',RegistrationView.as_view(),name="register"),
```


## Logout
```python
#view
class LogoutView(APIView):
    def post(self,request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
```
```python
#url
    path('logout/',LogoutView.as_view(),name="logout"),
```