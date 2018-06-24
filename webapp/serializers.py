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
			'MMSE','NHISscore','Appearance','Handedness','Orientation','Emotion','Memory','SpontaneosSpeech',
			'OlfactoryLeft','OlfactoryRight','VisualAcuityLeft','VisualAcuityRight','ColorVisionLeft','ColorVisionRIght',
			'FieldLeft','FieldRight','FundusLeft','FundusRight','NystagmusLeft','NystagmusRight','MovemenstLeft','MovemenstRight',
			'PupilLeft','PupilRight','Lightreflexleft','Lightreflexright','DirectLeft','DirectRight','ConsensualLeft','ConsensualRight',
			'nystagmusleft12','nystagmusright12','accomodationLeft','accomodationRight','sensoryLeft12','sensoryRight12','motorLeft',
			'motorRight','jawjerk','comealreflexleft','comealreflexright','eyeclosesureleft','eyeclosesureright','facialexpressionsleft',
			'facialexpressionsright','Comealexpressionright','Comealexpressionleft','tasteleft','tasteright','SensoryLeft','SensoryRight',
			'rhombusleft','rhombusright','rinnesleft','rinnesright','webbers','ABCleft','ABCright','sensoryLeft1','sensoryRight1',
			'motorLeft1','motorRight1','Gagleft','GagRight','palatalleft','palatalright','uvula','trapeziusleft','trapeziusright',
			'scmleft','scmright','poweroftongueleft','poweroftongueright','wastingleft','wastingright','protrusion','toneleft','toneright',
			'bulkleft','bulkright','abductionleft','abductionright','adductionleft','adductionright','flexionleft','flexionright','extensionleft',
			'extensionright','FlexionLeft12','FlexionRight12','flexionleft1','flexionright1','extensionleft1','extensionright1','HangGripleft',
			'HangGripright','toneleft1','toneright1','abductionleft1','abductionright1','adductionleft1','adductionright1','flexionleft2',
			'flexionright2','extensionleft2','extensionright2','flexionleft3','flexionright3','extensionleft3','extensionright3','flexionleft4',
			'flexionright4','extensionleft4','extensionright4','inversionleft','inversionright','eversionleft','eversionright','ehlleft','ehlright',
			'abornmalmovementsleft','abnormalmovementsright','upperlimbleft','upperlimbright','trunkleft','trunkright','lowerLimbleft','lowerLimbright',
			'upperlimbleft1','upperlimbright1','trunkleft1','trunkright1','lowerLimbleft1','lowerLimbleft1','vibrationLeft','vibrationRight',
			'JPSleft','JPSright','bicepsleft','bicepsright','tricepsleft','tricepsright','supinatorleft','supinatorright','Kneeleft','Kneeright',
			'Ankleleft','Ankleright','Abdominalleft','Abdominalright','Cremastricleft','Cremastricright','BCleft','BCright','PlantarLeft','PlantarRight',
			'HOffmansLeft','HOffmansRight','Fingerflexionleft','Fingerflexionright','pectoralLeft','pectoralRight','rombers','fingerNoseTextleft',
			'fingerNoseTextright','pendularKneeJerkleft','pendularKneeJerkright','kneeHelltestleft','kneeHelltestright','othersLeft','othersRight',
			'CVS','Abdomen','RespiratorySystem','Section4Name'
			)