from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validate_date):
        user = User.objects.create_user(**validate_date)
        return user

class LoginSerializers(serializers.Serializer):
    usarname = serializers.CharField()
    password = serializers.CharField()

    def validate(self, date):
        user = authenticate(**date)
        if user and user.is_activate:
            return user
        raise serializers.ValidationError("Неверные учетные данные ")

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'status']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    user = UserProfileSimpleSerializer()
    class Meta:
        model = Rating
        fields = '__all__'

class RatingSimpleSerializer(serializers.ModelSerializer):
    user = UserProfileSimpleSerializer()
    class Meta:
        model = Rating
        fields = ['product', 'user']

class ReviewSerializer(serializers.ModelSerializer):
    author = UserProfileSimpleSerializer()
    created_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = Review
        fields = '__all__'

class ReviewSimpleSerializer(serializers.ModelSerializer):
    author = UserProfileSimpleSerializer()
    class Meta:
        model = Review
        fields = ['author', 'text']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    reviews = ReviewSimpleSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    date = serializers.DateField(format="%Y-%m-%d")
    class Meta:
        model = Product
        fields = ['product_name', 'category', 'description', 'price',
                  'product_video', 'date', 'average_rating', 'ratings', 'reviews']

    def get_average_rating(self, obj):
        return obj.get_average_rating()
