from import_export import resources
from .models import SnomedTerms

class SnomedResource(resources.ModelResource):
    class Meta:
        model = SnomedTerms
        import_id_fields = ('regex',)