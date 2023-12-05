from django.contrib import admin
from document.models import *
from person.models import Person,EnslavementRelation
import nested_admin

class EnslavementRelationInline(nested_admin.NestedStackedInline):
	model = EnslavementRelation
	classes = ['collapse']
	extra=0
	exclude=['source','place','text_ref','unnamed_enslaved_count','date','amount','is_from_voyages']

class DocumentoAdmin(nested_admin.NestedModelAdmin):
	inlines=(
		EnslavementRelationInline,
	)





admin.site.register(Archivo)
admin.site.register(Fondo)
admin.site.register(SubFondo)
admin.site.register(Volume)
admin.site.register(Asunto)
admin.site.register(Documento,DocumentoAdmin)