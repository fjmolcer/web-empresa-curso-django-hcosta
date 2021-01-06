from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Personal').exists():
            return ('key', 'name')
        else:
            return ('created', 'updated')

#Podemos usar el método get_excluded que permite ocultar campos en 
# lugar de ponerlos de solo lectura

admin.site.register(Link, LinkAdmin)