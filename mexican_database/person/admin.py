from django.contrib import admin
from person.models import *
# Register your models here.


class AliasInline(admin.StackedInline):
	model=Alias
	extra=0
	classes=['collapse']

class PersonAdmin(admin.ModelAdmin):
	inlines=(
		AliasInline,
	)

admin.site.register(Occupation)
admin.site.register(Person,PersonAdmin)
admin.site.register(EnslavementRelation)
admin.site.register(EnslavementRelationType)

admin.site.register(EnslavementRelationRole)
admin.site.register(Alias)