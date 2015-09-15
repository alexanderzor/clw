from import_export import resources
from models import CustomUser


class ExportResource(resources.ModelResource):

    class Meta:
        model = CustomUser
        #fields = ('first_name', 'last_name', 'middle_name', 'email', 'city', 'phone', )
        #exclude = ('imported', )
