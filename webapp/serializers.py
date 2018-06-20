from rest_framework import serializers
from .models import formModel



#class employeeSerializer(serializers.ModelSerializer):
#
#	class Meta:
#		model = formModel
#		fields = '__all__'


class patientSerializer(serializers.ModelSerializer):

	class Meta:
		model = formModel
		fields = ('Name', 'Age', 'genderChoice', 'Kureid')