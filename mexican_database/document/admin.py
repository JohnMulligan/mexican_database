from django.contrib import admin
from document.models import *
from person.models import Esclavizador,PersonaEsclavizada,EsclavizadorDocumentoConexion,EsclavizadaDocumentoConexion
import nested_admin



class EsclavizadorDocumentoConexionInline(nested_admin.NestedStackedInline):
	model = EsclavizadorDocumentoConexion
	classes = ['collapse']
	extra=0


class EsclavizadaDocumentoConexionInline(nested_admin.NestedStackedInline):
	model = EsclavizadaDocumentoConexion
	classes = ['collapse']
	extra=0

class DocumentoAdmin(nested_admin.NestedModelAdmin):
	inlines=(
		EsclavizadorDocumentoConexionInline,
		EsclavizadaDocumentoConexionInline
	)
	list_display = ('ano','resumen')
	search_fields=['ano','resumen']


admin.site.register(Archivo)
admin.site.register(Fondo)
admin.site.register(SubFondo)
admin.site.register(Volumen)
admin.site.register(Asunto)
admin.site.register(Documento,DocumentoAdmin)