from .models import Candidate
from rest_framework import serializers

# Candidate serializer
class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['first_name', 'email', 'mobile_number']