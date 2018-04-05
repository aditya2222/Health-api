from rest_framework import serializers
from .models import stepOneModel



class employeeSerializer(serializers.ModelSerializer):

	class Meta:
		model = stepOneModel
		fields = '__all__'


