from rest_framework import serializers

from . import models


class ChunkInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chunk
        fields = ['id', 'dataset', 'delimiter', 'parsing_service', 'ignore_features', 'to_lowercase',
                  'created_at', 'updated_at']
        read_only_fields = ['id', 'dataset', 'created_at', 'updated_at']


class DatasetSerializer(serializers.HyperlinkedModelSerializer):
    chunks = ChunkInfoSerializer(many=True, read_only=True)

    class Meta:
        model = models.Dataset
        fields = ['id', 'url', 'description', 'chunks', 'created_at', 'updated_at']
        read_only_fields = ['id', 'url', 'chunks', 'created_at', 'updated_at']


class ChunkSerializer(serializers.ModelSerializer):
    dataset = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = models.Chunk
        fields = ['id', 'dataset', 'content', 'delimiter', 'parsing_service', 'ignore_features', 'to_lowercase',
                  'created_at', 'updated_at']
        read_only_fields = ['id', 'dataset', 'created_at', 'updated_at']


class EstimatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Estimator
        fields = ['id', 'url', 'service']
        read_only_fields = ['id', 'url']


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault())


class TrainingSerializer(TaskSerializer):
    class Meta:
        model = models.Training
        fields = ['dataset', 'status', 'errors', 'output', 'user', 'estimator',
                  'learning_rate', 'dropout_rate',
                  'batch_size', 'started_at', 'finished_at', 'created_at', 'updated_at']
        read_only_fields = ['status', 'output', 'errors', 'started_at', 'finished_at', 'created_at', 'updated_at']


class PredictionSerializer(TaskSerializer):
    class Meta:
        model = models.Prediction
        fields = ['dataset', 'status', 'errors', 'output', 'user', 'estimator',
                  'started_at', 'finished_at', 'created_at', 'updated_at']
        read_only_fields = ['status', 'output', 'errors', 'started_at', 'finished_at', 'created_at', 'updated_at']
