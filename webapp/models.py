from django.db import models
from django.utils.crypto import get_random_string



# Create your models here.

class formModel(models.Model):
    Name = models.CharField(max_length=120, blank=True,)
    Age = models.IntegerField(blank=True)
    genderChoice = models.CharField(max_length=10, null=True, blank=True)
    Opno = models.IntegerField(default=0, blank=True)
    Ipno = models.IntegerField(default=0, blank=True)
    Address = models.TextField(null=True, blank=True)
    Phoneno = models.IntegerField(blank=True)
    Kureid = models.CharField(max_length=120, blank=True, null=True, default='None')
    ChiefComplaints = models.CharField(max_length=120, null=True, blank=True,default='None')
    Historyofillness = models.CharField(max_length=120, null=True, blank=True,default='None')
    PastHistory = models.CharField(max_length=150, blank=True, null=True,default='None')
    FamilyHistory = models.CharField(max_length=150, blank=True, null=True,default='None')
    ProvisionalDiagnosis = models.CharField(max_length=150, blank=True, null=True,default='None')
    Medicationhistroy = models.CharField(max_length=120, null=True, blank=True,default='None')
    Alcohol = models.BooleanField(default=False, blank=True)
    Smoking = models.BooleanField(default=False, blank=True)
    Bowel = models.BooleanField(default=False, blank=True)
    Bladder = models.BooleanField(default=False, blank=True)
    Sleep = models.BooleanField(default=False, blank=True)
    Summary = models.TextField(null=True, blank=True,default='None')
    Examinedby = models.CharField(max_length=10, null=True, blank=True,default='None')
    Verifiedby = models.CharField(max_length=10, null=True, blank=True,default='None')
    # models of section 3 begin here
    # models of General Examination
    GeneralConditions = models.CharField(max_length=120, null=True, blank=True,default='None')
    Built = models.CharField(max_length=120, null=True, blank=True,default='None')
    PulseRate = models.IntegerField(default=0,blank=True)
    Systolic = models.IntegerField(default=0,blank=True)
    Diastolic = models.IntegerField(default=0,blank=True)
    Temperature = models.IntegerField(default=0,blank=True, null=True)
    pl = models.IntegerField(default=0,blank=True)
    Palar = models.BooleanField(default=False,blank=True)
    Clubbing = models.BooleanField(default=False,blank=True)
    Ictreus = models.BooleanField(default=False,blank=True)
    Lymphadenopathy = models.BooleanField(default=False,blank=True)
    Cyanosis = models.BooleanField(default=False,blank=True)
    PittingEdema = models.BooleanField(default=False,blank=True)
    NeurocutaneousMarkers = models.CharField(max_length=126, null=True,blank=True,default='None')
    SubcutaneousMarkers = models.CharField(max_length=10, null=True, blank=True,default='None')
    SkeletalExamination = models.CharField(max_length=126, null=True,blank=True,default='None')
    # models of CNS examination
    EyeResponse = models.CharField(max_length=126, null=True,blank=True,default='None')
    VerbalResponse = models.CharField(max_length=126, null=True,blank=True,default='None')
    MotorResponse = models.CharField(max_length=126, null=True,blank=True,default='None')
    MMSE = models.CharField(max_length=126, null=True,blank=True,default='None')
    NHISscore = models.CharField(max_length=126, null=True,blank=True,default='None')
    Appearance = models.CharField(max_length=126, null=True,blank=True,default='None')
    Handedness = models.CharField(max_length=126, null=True,blank=True,default='None')
    Orientation = models.CharField(max_length=126, null=True,blank=True,default='None')
    Emotion = models.CharField(max_length=126, null=True,blank=True,default='None')
    Memory = models.CharField(max_length=126, null=True,blank=True,default='None')
    SpontaneosSpeech = models.CharField(max_length=126, null=True,blank=True,default='None')
    # models of Cranial Nerves
    OlfactoryLeft = models.CharField(max_length=126, null=True,blank=True,default='None')
    OlfactoryRight = models.CharField(max_length=126, null=True,blank=True,default='None')
    # models of optic
    VisualAcuityLeft = models.CharField(max_length=126, null=True,blank=True,default='None')
    VisualAcuityRight = models.CharField(max_length=126, null=True,blank=True,default='None')
    ColorVisionLeft = models.CharField(max_length=126, null=True,blank=True,default='None')
    ColorVisionRIght = models.CharField(max_length=126, null=True,blank=True,default='None')
    FieldLeft = models.CharField(max_length=126, null=True,blank=True,default='None')
    FieldRight = models.CharField(max_length=126, null=True,blank=True,default='None')
    FundusLeft = models.CharField(max_length=126, null=True,blank=True,default='None')
    FundusRight = models.CharField(max_length=126, null=True,blank=True,default='None')
    NystagmusLeft = models.CharField(max_length=126, null=True,blank=True,default='None')
    NystagmusRight = models.CharField(max_length=126, null=True,blank=True,default='None')
    # models of occulomotor, abducent, trochlear
    MovemenstLeft = models.CharField(max_length=126, null=True,blank=True,default='None')
    MovemenstRight = models.CharField(max_length=126, null=True,blank=True,default='None')
    PupilLeft = models.CharField(max_length=120, null=True,blank=True,default='None')
    PupilRight = models.CharField(max_length=120, null=True,blank=True,default='None')
    Lightreflexleft = models.CharField(max_length=120, null=True,blank=True,default='None')
    Lightreflexright = models.CharField(max_length=120, null=True,blank=True,default='None')
    DirectLeft = models.CharField(max_length=120, null=True,blank=True,default='None')
    DirectRight = models.CharField(max_length=120, null=True,blank=True,default='None')
    ConsensualLeft = models.CharField(max_length=120, null=True,blank=True,default='None')
    ConsensualRight = models.CharField(max_length=120, null=True,blank=True,default='None')
    nystagmusleft12 = models.CharField(max_length=120, null=True,blank=True,default='None')
    nystagmusright12 = models.CharField(max_length=120, null=True,blank=True,default='None')
    accomodationLeft = models.CharField(max_length=120, null=True,blank=True,default='None')
    accomodationRight = models.CharField(max_length=120, null=True,blank=True,default='None')
    # models of trigeminal
    sensoryLeft12 = models.CharField(max_length=120, null=True,blank=True,default='None')
    sensoryRight12 = models.CharField(max_length=120, null=True,blank=True,default='None')
    motorLeft = models.CharField(max_length=120, null=True,blank=True,default='None')
    motorRight = models.CharField(max_length=120, null=True,blank=True,default='None')
    jawjerk = models.CharField(max_length=120, null=True,blank=True,default='None')
    comealreflexleft = models.CharField(max_length=120, null=True,blank=True,default='None')
    comealreflexright = models.CharField(max_length=120, null=True,blank=True,default='None')
    # models of facial nerve
    eyeclosesureleft = models.CharField(max_length=120, null=True,blank=True,default='None')
    eyeclosesureright = models.CharField(max_length=120, null=True,blank=True,default='None')
    facialexpressionsleft = models.CharField(max_length=120, null=True,blank=True,default='None')
    facialexpressionsright = models.CharField(max_length=120, null=True,blank=True,default='None')
    Comealexpressionright = models.CharField(max_length=120, null=True,blank=True,default='None')
    Comealexpressionleft = models.CharField(max_length=120, null=True,blank=True,default='None')
    tasteleft = models.CharField(max_length=120, null=True,blank=True,default='None')
    tasteright = models.CharField(max_length=120, null=True,blank=True,default='None')
    SensoryLeft = models.CharField(max_length=120, null=True,blank=True,default='None')
    SensoryRight = models.CharField(max_length=120, null=True,blank=True,default='None')
    # models of Vestibulocochlear Nerve
    rhombusleft = models.CharField(max_length=120, null=True,blank=True,default='None')
    rhombusright = models.CharField(max_length=120, null=True,blank=True,default='None')
    rinnesleft = models.CharField(max_length=120, null=True,blank=True,default='None')
    rinnesright = models.CharField(max_length=120, null=True,blank=True,default='None')
    webbers= models.CharField(max_length=120, null=True,blank=True,default='None')
    ABCleft = models.CharField(max_length=120, null=True,blank=True,default='None')
    ABCright = models.CharField(max_length=120, null=True,blank=True,default='None')
    # models of Glosopharyngeal and Vagus
    sensoryLeft1 = models.CharField(max_length=120, null=True,blank=True,default='None')
    sensoryRight1 = models.CharField(max_length=120, null=True,blank=True,default='None')
    motorLeft1 = models.CharField(max_length=120, null=True,blank=True,default='None')
    motorRight1 = models.CharField(max_length=120, null=True,blank=True,default='None')
    Gagleft = models.CharField(max_length=120, null=True,blank=True,default='None')
    GagRight = models.CharField(max_length=120, null=True,blank=True,default='None')
    palatalleft = models.CharField(max_length=120, null=True,blank=True,default='None')
    palatalright = models.CharField(max_length=120, null=True,blank=True,default='None')
    uvula = models.CharField(max_length=120, null=True,blank=True,default='None')
    # models of Accessory Nerve
    trapeziusleft = models.CharField(max_length=120, null=True,blank=True,default='None')
    trapeziusright = models.CharField(max_length=120, null=True,blank=True,default='None')
    scmleft = models.CharField(max_length=120, null=True,blank=True,default='None')
    scmright = models.CharField(max_length=120, null=True,blank=True,default='None')
    # models of Hypoglossal Nerve
    poweroftongueleft = models.CharField(max_length=120, null=True,blank=True,default='None')
    poweroftongueright = models.CharField(max_length=120, null=True,blank=True,default='None')
    wastingleft = models.CharField(max_length=120, null=True,blank=True,default='None')
    wastingright = models.CharField(max_length=120, null=True,blank=True,default='None')
    protrusion = models.CharField(max_length=120, null=True,blank=True,default='None')

    # models of motor system
    # models of upper limb
    toneleft = models.CharField(max_length=120, null=True,blank=True,default='None')
    toneright = models.CharField(max_length=120, null=True,blank=True,default='None')
    bulkleft = models.CharField(max_length=120, null=True,blank=True,default='None')
    bulkright = models.CharField(max_length=120, null=True,blank=True,default='None')
    shoulderleft = models.CharField(max_length=120, null=True,blank=True,default='None')
    shoulderright = models.CharField(max_length=120, null=True,blank=True,default='None')
    abductionleft = models.CharField(max_length=120, null=True,blank=True,default='None')
    abductionright = models.CharField(max_length=120, null=True,blank=True,default='None')
    adductionleft = models.CharField(max_length=120, null=True,blank=True,default='None')
    adductionright = models.CharField(max_length=120, null=True,blank=True,default='None')
    flexionleft = models.CharField(max_length=120, null=True,blank=True,default='None')
    flexionright = models.CharField(max_length=120, null=True,blank=True,default='None')
    extensionleft = models.CharField(max_length=120, null=True,blank=True,default='None')
    extensionright = models.CharField(max_length=120, null=True,blank=True,default='None')
    # models of Elbow
    FlexionLeft12 = models.CharField(max_length=120, null=True,blank=True,default='None')
    FlexionRight12 = models.CharField(max_length=120, null=True,blank=True,default='None')
    ExtensionLeft12 = models.CharField(max_length=120, null=True,blank=True,default='None')
    ExtensionRight12 = models.CharField(max_length=120, null=True,blank=True,default='None')
    # models of wrist
    flexionleft1 = models.CharField(max_length=120, null=True,blank=True,default='None')
    flexionright1 = models.CharField(max_length=120, null=True,blank=True,default='None')
    extensionleft1 = models.CharField(max_length=120, null=True,blank=True,default='None')
    extensionright1 = models.CharField(max_length=120, null=True,blank=True,default='None')
    # model of hanggrip
    HangGripleft = models.CharField(max_length=120, null=True,blank=True, default='None')
    HangGripright = models.CharField(max_length=120, null=True,blank=True, default='None')
    # models of Lower Limb
    toneleft1 = models.CharField(max_length=120, null=True,blank=True, default='None')
    toneright1 = models.CharField(max_length=120, null=True,blank=True, default='None')
    BulkLeft12 = models.CharField(max_length=120,blank=True, default='None')
    BulkRight12 = models.CharField(max_length=120,blank=True, default='None')
    # models of Hip
    abductionleft1 = models.CharField(max_length=120, null=True,blank=True, default='None')
    abductionright1 = models.CharField(max_length=120, null=True,blank=True, default='None')
    adductionleft1 = models.CharField(max_length=120, null=True,blank=True, default='None')
    adductionright1 = models.CharField(max_length=120, null=True,blank=True, default='None')
    flexionleft2 = models.CharField(max_length=120, null=True,blank=True, default='None')
    flexionright2 = models.CharField(max_length=120, null=True,blank=True, default='None')
    extensionleft2 = models.CharField(max_length=120, null=True,blank=True, default='None')
    extensionright2 = models.CharField(max_length=120, null=True,blank=True, default='None')
    # models of Knee
    flexionleft3 = models.CharField(max_length=120, null=True,blank=True, default='None')
    flexionright3 = models.CharField(max_length=120, null=True,blank=True, default='None')
    extensionleft3 = models.CharField(max_length=120, null=True,blank=True, default='None')
    extensionright3 = models.CharField(max_length=120, null=True,blank=True, default='None')
    # models of ankle
    flexionleft4 = models.CharField(max_length=120, null=True,blank=True, default='None')
    flexionright4 = models.CharField(max_length=120, null=True,blank=True, default='None')
    extensionleft4 = models.CharField(max_length=120, null=True,blank=True, default='None')
    extensionright4 = models.CharField(max_length=120, null=True,blank=True, default='None')
    inversionleft = models.CharField(max_length=120, null=True,blank=True, default='None')
    inversionright = models.CharField(max_length=120, null=True,blank=True, default='None')
    eversionleft = models.CharField(max_length=120, null=True,blank=True, default='None')
    eversionright = models.CharField(max_length=120, null=True,blank=True, default='None')
    ehlleft = models.CharField(max_length=120, null=True,blank=True, default='None')
    ehlright = models.CharField(max_length=120, null=True,blank=True, default='None')
    abornmalmovementsleft = models.CharField(max_length=120, null=True,blank=True, default='None')
    abnormalmovementsright = models.CharField(max_length=120, null=True,blank=True, default='None')
    # models of sensory movements
    upperlimbleft = models.CharField(max_length=120, null=True,blank=True, default='None')
    upperlimbright = models.CharField(max_length=120, null=True,blank=True, default='None')
    trunkleft = models.CharField(max_length=120, null=True,blank=True, default='None')
    trunkright = models.CharField(max_length=120, null=True,blank=True, default='None')
    lowerLimbleft = models.CharField(max_length=120, null=True,blank=True, default='None')
    lowerLimbright = models.CharField(max_length=120, null=True,blank=True, default='None')
    # models for temperature
    upperlimbleft1 = models.CharField(max_length=102, null=True,blank=True, default='None')
    upperlimbright1 = models.CharField(max_length=120, null=True,blank=True, default='None')
    trunkleft1 = models.CharField(max_length=120, null=True,blank=True, default='None')
    trunkright1 = models.CharField(max_length=120, null=True,blank=True, default='None')
    lowerLimbleft1 = models.CharField(max_length=120, null=True,blank=True, default='None')
    lowerLimbright1 = models.CharField(max_length=120, null=True,blank=True, default='None')
    # models for posterior column
    vibrationLeft = models.CharField(max_length=120, null=True,blank=True, default='None')
    vibrationRight = models.CharField(max_length=120, null=True,blank=True, default='None')
    JPSleft = models.CharField(max_length=120, null=True,blank=True, default='None')
    JPSright = models.CharField(max_length=120, null=True,blank=True, default='None')
    # models for Reflexes
    bicepsleft = models.CharField(max_length=120, null=True,blank=True, default='None')
    bicepsright = models.CharField(max_length=120, null=True,blank=True, default='None')
    tricepsleft = models.CharField(max_length=120, null=True,blank=True, default='None')
    tricepsright = models.CharField(max_length=120, null=True,blank=True, default='None')
    supinatorleft = models.CharField(max_length=120, null=True,blank=True, default='None')
    supinatorright = models.CharField(max_length=120, null=True,blank=True, default='None')
    Kneeleft = models.CharField(max_length=120, null=True,blank=True, default='None')
    Kneeright = models.CharField(max_length=120, null=True,blank=True, default='None')
    Ankleleft = models.CharField(max_length=120, null=True,blank=True, default='None')
    Ankleright = models.CharField(max_length=120, null=True,blank=True, default='None')
    Abdominalleft = models.CharField(max_length=120, null=True,blank=True, default='None')
    Abdominalright = models.CharField(max_length=120, null=True,blank=True, default='None')
    Cremastricleft = models.CharField(max_length=120, null=True,blank=True, default='None')
    Cremastricright = models.CharField(max_length=120, null=True,blank=True, default='None')
    BCleft = models.CharField(max_length=120, null=True,blank=True, default='None')
    BCright = models.CharField(max_length=120, null=True,blank=True, default='None')
    PlantarLeft = models.CharField(max_length=120, null=True,blank=True, default='None')
    PlantarRight = models.CharField(max_length=120, null=True,blank=True, default='None')
    HOffmansLeft = models.CharField(max_length=120, null=True,blank=True, default='None')
    HOffmansRight = models.CharField(max_length=120, null=True,blank=True, default='None')
    Fingerflexionleft = models.CharField(max_length=120, null=True,blank=True, default='None')
    Fingerflexionright = models.CharField(max_length=120, null=True,blank=True, default='None')
    pectoralLeft = models.CharField(max_length=120, null=True,blank=True, default='None')
    pectoralRight = models.CharField(max_length=120, null=True,blank=True, default='None')
    # models of cerebellar signs
    rombers = models.CharField(max_length=120, null=True,blank=True, default='None')
    fingerNoseTextleft = models.CharField(max_length=120, null=True,blank=True, default='None')
    fingerNoseTextright = models.CharField(max_length=120, null=True,blank=True, default='None')
    pendularKneeJerkleft = models.CharField(max_length=120, null=True,blank=True, default='None')
    pendularKneeJerkright = models.CharField(max_length=120, null=True,blank=True, default='None')
    kneeHelltestleft = models.CharField(max_length=120, null=True,blank=True, default='None')
    kneeHelltestright = models.CharField(max_length=120, null=True,blank=True, default='None')
    othersLeft = models.CharField(max_length=120, null=True,blank=True, default='None')
    othersRight = models.CharField(max_length=120, null=True,blank=True, default='None')
    # models for other systems
    CVS = models.CharField(max_length=120,blank=True, default='None')
    Abdomen = models.CharField(max_length=120,blank=True, default='None')
    RespiratorySystem = models.CharField(max_length=120,blank=True, default='None')
    Section4Name = models.CharField(max_length=120,null=True,blank=True, default='None')

    def __str__(self):
        return self.Name



class SnomedTerms(models.Model):
    conceptID = models.CharField(max_length=120)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.conceptID