# from rest_framework import serializers
# from api.models import Board
#
# class BoardSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     type = serializers.CharField(max_length=20, default='public')
#
#     def create(self, validated_data):
#         return Board.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#
#         instance.type = validated_data.get('type', instance.type)
#         instance.save()
#         return instance

from rest_framework import serializers
from django.utils import timezone
from api.models import Board, TaskList, Card
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    boards = serializers.PrimaryKeyRelatedField(many=True, queryset=Board.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'boards')

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('name','description','task_list')

class TaskListSerializer(serializers.ModelSerializer):
    card = CardSerializer(read_only=True, many=True)
    class Meta:
        model = TaskList
        fields = ('id','board','name','card')

class BoardSerializer(serializers.ModelSerializer):
    task_list = TaskListSerializer(read_only=True,many=True)
    # print(task_lists)
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Board
        fields = ('id','name','pub_date','task_list','owner')
