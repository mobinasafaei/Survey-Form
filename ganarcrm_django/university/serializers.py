from rest_framework import serializers

from .models import Result

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = (
            'id',
            'student_id',
            'q1',
            'q2',
            'q3',
            'q4',
            'q5',
            'q6',
            'q7',
        )
