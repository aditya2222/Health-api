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
		fields = ('id','Name', 'Age', 'genderChoice', 'Kureid',
			'Opno','Ipno','Address','Phoneno',
			'ChiefComplaints','Historyofillness',
			'PastHistory','FamilyHistory','ProvisionalDiagnosis',
			'Medicationhistroy','Alcohol','Smoking','Bowel','Bladder',
			'Sleep','Summary','Examinedby','Verifiedby','PulseRate',
			'Systolic','Diastolic','Temperature','pl','Palar','Clubbing',
			'Ictreus','Lymphadenopathy','Cyanosis','PittingEdema','SubcutaneousMarkers',
			'SkeletalExamination','EyeResponse','VerbalResponse','MotorResponse',
			'MMSE','NHISscore','Appearance','Handedness','Orientation','Emotion','Memory','SpontaneosSpeech'
			)