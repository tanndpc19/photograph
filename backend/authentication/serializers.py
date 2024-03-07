from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password




class UserSerializer(serializers.ModelSerializer):
    user_name= serializers.CharField(
        allow_null = True,
        validators = [UniqueValidator(queryset=User.objects.all())]
    )

    email = serializers.EmailField(
        allow_null = False,
        validators = [UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only = True,
        allow_null = True,
        validators = [validate_password]
    )

    password_confirm = serializers.CharField(
        write_only=True, 
        allow_null = True
    )

    class Meta:
        model = User
        fields = ('user_name', 'email', 'password', 'password_confirm', 'type')

    def validatePassword(self, attrs):
        if attrs.get('password') != attrs.get('password_confirm'):
            raise serializers.ValidationError({"password": "Password fields did not match."})
        return attrs
    
    def create(self, validatedData):
        del validatedData['password_confirm']
        password = make_password(validatedData.pop('password'))

        # operator (**) to unpack the remaining elements from validated_data into keyword arguments for the User model constructor. 
        user = User.objects.create(password = password, **validatedData)
        return user
    
    def update(self, validatedData, instance):
        for field, value in validatedData.items():
            if field == 'password':
                instance.password = make_password(value)
            else:
                setattr(instance, field, value)

        instance.save()
        return instance
    
