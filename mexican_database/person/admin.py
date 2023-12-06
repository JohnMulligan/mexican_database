from django.contrib import admin
from person.models import *
from document.models import Documento
import nested_admin



class EsclavizadorDocumentoConexionInline_b(nested_admin.NestedStackedInline):
	model = EsclavizadorDocumentoConexion
	classes = ['collapse']
	extra=0


class EsclavizadaDocumentoConexionInline_b(nested_admin.NestedStackedInline):
	model = EsclavizadaDocumentoConexion
	classes = ['collapse']
	extra=0

class PersonaEsclavizadaAdmin(nested_admin.NestedModelAdmin):
	inlines=(
		EsclavizadaDocumentoConexionInline_b,
	)
	list_display = ('primer_nombre','apellido')
	search_fields=('primer_nombre','apellido')

class EsclavizadorAdmin(nested_admin.NestedModelAdmin):
	inlines=(
		EsclavizadorDocumentoConexionInline_b,
	)
	list_display = ('nombre','apellido')
	search_fields=('nombre','apellido')



admin.site.register(CategoriaDeOcupacion)
admin.site.register(Ocupacion)
admin.site.register(Sexo)
admin.site.register(Etonimo)
admin.site.register(CalidadDePersona)
admin.site.register(HispanizacionDePersona)
admin.site.register(EstatusDeEsclavizador)
admin.site.register(SituacionDeLugarDeEsclavizador)
admin.site.register(Esclavizador,EsclavizadorAdmin)
admin.site.register(PersonaEsclavizada,PersonaEsclavizadaAdmin)
admin.site.register(TipoDeRelacion)
admin.site.register(RolDeRelacion)
