from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from rest_framework import status
from .models import formModel, SnomedTerms
from .serializers import patientSerializer, tableSerializer
from django.views.generic import TemplateView, CreateView, ListView, TemplateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.renderers import StaticHTMLRenderer
from .forms import myForm
from django.utils.decorators import method_decorator
from reportlab.pdfgen import canvas
import reportlab.rl_config
import json
from django.template.loader import get_template


# Create your views here.

class empList(APIView):
    def get(self, request):
        employees1 = formModel.objects.all()
        serializer = employeeSerializer(employees1, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class createPDFReport(APIView):
    def get(self, request):
        parameters = request.query_params
        kureid = parameters.get('kureid')
        print(kureid)
        c = canvas.Canvas("/Users/vyramach/Documents/Kure/MVP/source/mvp/pdfs/" + kureid + ".pdf")
        c.drawString(100, 100, kureid)
        c.showPage()
        c.save()
        return Response(kureid)


class CreatePatientForm(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    template_name = 'webapp/createPatient.html'
    form_class = myForm
    success_url = 'webapp/stepOneModel_list.html'
    reportlab.rl_config.warnOnMissingFontGlyphs = 0
    def get_context_data(self, **kwargs):
        kwargs['object_list'] = SnomedTerms.objects.all()
        return super(CreatePatientForm, self).get_context_data(**kwargs)


class CreatePatientAutofilledForm(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    template_name = 'webapp/createPatientautofill.html'
    form_class = myForm
    success_url = 'webapp/stepOneModel_list.html'
    reportlab.rl_config.warnOnMissingFontGlyphs = 0


# class dashboard(LoginRequiredMixin,APIView):
#	login_url='/login/'
#	def get(self,request):
#		return render(request, 'webapp/formmodel_list.html')


# @api_view(['GET'])
# @permission_classes((IsAuthenticated, ))
@login_required(login_url='/login/')
def dashboard(request, path=''):
    return render(request, 'webapp/formmodel_list.html')


class PatientsList(LoginRequiredMixin, APIView):
    login_url = '/login/'

    def get(self, request):
        patients = formModel.objects.all()
        serializer = patientSerializer(patients, many=True)
        return Response(serializer.data)


class tableintializeView(APIView):
    def get(self, request):
        patients = formModel.objects.all()
        serializer = tableSerializer(patients, many=True)
        return Response(serializer.data)


# class PatientsList(LoginRequiredMixin,ListView):
#	login_url='/login/'
#	model = formModel
#	paginate_by = 50
#
#	def get_queryset(self):
#		#print(formModel.objects)
#		return formModel.objects.filter(Opno__isnull=False)


class ThankYouPage(TemplateView):
    template_name = 'webapp/thankyou.html'


class PatientUpdate(UpdateView):
    model = formModel
    form_class = myForm
    template_name = 'webapp/editpatient.html'
    success_url = '/'


class ViewPatient(UpdateView):
    model = formModel
    form_class = myForm
    template_name = 'webapp/createPatientautofill.html'


from django.http import HttpResponse
from django.views.generic import View

from webapp.utils import render_to_pdf  # created in step 4


class GeneratePDF(DetailView):
    model = formModel

    def get(self, request, *args, **kwargs):
        template = get_template('webapp/invoice.html')
        context = {
            "Name": self.get_object().Name,
            "Kureid": self.get_object().Kureid,
            "Name": self.get_object().Name,
            "Age": self.get_object().Age,
            "Gender": self.get_object().genderChoice,
            "Ipno": self.get_object().Ipno,
            "Opno": self.get_object().Opno,
            "Address": self.get_object().Address,
            "Phoneno": self.get_object().Phoneno,
            "Historyofillness": self.get_object().Historyofillness,
            "Medicationhistroy": self.get_object().Medicationhistroy,
            "Alcohol": self.get_object().Alcohol,
            "Smoking": self.get_object().Smoking,
            "Bowel": self.get_object().Bowel,
            "Bladder": self.get_object().Bladder,
            "Summary": self.get_object().Summary,
            "Examinedby": self.get_object().Examinedby,
            "Verifiedby": self.get_object().Verifiedby,
            "PulseRate": self.get_object().PulseRate,
            "Systolic": self.get_object().Systolic,
            "Diastolic": self.get_object().Diastolic,
            "Temperature": self.get_object().Temperature,
            "Palar": self.get_object().Palar,
            "Clubbing": self.get_object().Clubbing,
            "Ictreus": self.get_object().Ictreus,
            "Cyanosis": self.get_object().Cyanosis,
            "PittingEdema": self.get_object().PittingEdema,
            "Lymphadenopathy": self.get_object().Lymphadenopathy,
            "SubcutaneousMarkers": self.get_object().SubcutaneousMarkers,
            "SkeletalExamination": self.get_object().SkeletalExamination,
            "EyeResponse": self.get_object().EyeResponse,
            "VerbalResponse": self.get_object().VerbalResponse,
            "MotorResponse": self.get_object().MotorResponse,
            "MMSE": self.get_object().MMSE,
            "NHISscore": self.get_object().NHISscore,
            "Appearance": self.get_object().Appearance,
            "Handedness": self.get_object().Handedness,
            "Orientation": self.get_object().Orientation,
            "Emotion": self.get_object().Emotion,
            "Memory": self.get_object().Memory,
            "SpontaneosSpeech": self.get_object().SpontaneosSpeech,
            "OlfactoryRight": self.get_object().OlfactoryRight,
            "OlfactoryLeft": self.get_object().OlfactoryLeft,
            "VisualAcuityRight": self.get_object().VisualAcuityRight,
            "VisualAcuityLeft": self.get_object().VisualAcuityLeft,
            "ColorVisionRIght": self.get_object().ColorVisionRIght,
            "ColorVisionLeft": self.get_object().ColorVisionLeft,
            "FieldRight": self.get_object().FieldRight,
            "FieldLeft": self.get_object().FieldLeft,
            "FundusRight": self.get_object().FundusRight,
            "FundusLeft": self.get_object().FundusLeft,
            "NystagmusRight": self.get_object().NystagmusRight,
            "NystagmusLeft": self.get_object().NystagmusLeft,
            "MovemenstRight": self.get_object().MovemenstRight,
            "MovemenstLeft": self.get_object().MovemenstLeft,
            "PupilRight": self.get_object().PupilRight,
            "PupilLeft": self.get_object().PupilLeft,
            "DirectRight": self.get_object().DirectRight,
            "DirectLeft": self.get_object().DirectLeft,
            "ConsensualRight": self.get_object().ConsensualRight,
            "ConsensualLeft": self.get_object().ConsensualLeft,
            "accomodationRight": self.get_object().accomodationRight,
            "accomodationLeft": self.get_object().accomodationLeft,
            "sensoryRight12": self.get_object().sensoryRight12,
            "sensoryLeft12": self.get_object().sensoryLeft12,
            "motorRight": self.get_object().motorRight,
            "motorLeft": self.get_object().motorLeft,
            "jawjerk": self.get_object().jawjerk,
            "comealreflexright": self.get_object().comealreflexright,
            "comealreflexleft": self.get_object().comealreflexleft,
            "eyeclosesureright": self.get_object().eyeclosesureright,
            "eyeclosesureleft": self.get_object().eyeclosesureleft,
            "facialexpressionsright": self.get_object().facialexpressionsright,
            "facialexpressionsleft": self.get_object().facialexpressionsleft,
            "tasteright": self.get_object().tasteright,
            "tasteleft": self.get_object().tasteleft,
            "SensoryRight": self.get_object().SensoryRight,
            "SensoryLeft": self.get_object().SensoryLeft,
            "rinnesright": self.get_object().rinnesright,
            "rinnesleft": self.get_object().rinnesleft,
            "webbers": self.get_object().webbers,
            "ABCright": self.get_object().ABCright,
            "ABCleft": self.get_object().ABCleft,
            "sensoryRight1": self.get_object().sensoryRight1,
            "sensoryLeft1": self.get_object().sensoryLeft1,
            "motorRight1": self.get_object().motorRight1,
            "motorLeft1": self.get_object().motorLeft1,
            "GagRight": self.get_object().GagRight,
            "Gagleft": self.get_object().Gagleft,
            "palatalright": self.get_object().palatalright,
            "palatalleft": self.get_object().palatalleft,
            "uvula": self.get_object().uvula,
            "trapeziusright": self.get_object().trapeziusright,
            "trapeziusleft": self.get_object().trapeziusleft,
            "scmright": self.get_object().scmright,
            "scmleft": self.get_object().scmleft,
            "poweroftongueright": self.get_object().poweroftongueright,
            "poweroftongueleft": self.get_object().poweroftongueleft,
            "protrusion": self.get_object().protrusion,
            "wastingleft": self.get_object().wastingleft,
            "wastingright": self.get_object().wastingright,
            "protrusion": self.get_object().protrusion,
            "toneleft": self.get_object().toneleft,
            "toneright": self.get_object().toneright,
            "bulkleft": self.get_object().bulkleft,
            "bulkright": self.get_object().bulkright,
            "shoulderleft": self.get_object().shoulderleft,
            "shoulderright": self.get_object().shoulderright,
            "abductionleft": self.get_object().abductionleft,
            "adductionleft": self.get_object().adductionleft,
            "adductionright": self.get_object().adductionright,
            "adductionright": self.get_object().adductionright,
            "adductionright": self.get_object().adductionright,
            "adductionright": self.get_object().adductionright,
            "adductionright": self.get_object().adductionright,
            "adductionright": self.get_object().adductionright,
            "adductionright": self.get_object().adductionright,
            "adductionright": self.get_object().adductionright,
            "adductionright": self.get_object().adductionright,
            "adductionright": self.get_object().adductionright,
            "adductionright": self.get_object().adductionright,

        }
        html = template.render(context)
        pdf = render_to_pdf('webapp/invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "patientdetails.pdf"
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")




from tablib import Dataset

def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')




# class SnomedTermsView(ListView):
#     model = SnomedTerms
#     template_name = 'webapp/createPatient.html'

#     def get_queryset(self):
#         return SnomedTerms.objects.all()