from django.contrib import admin
from .models import Colegio, Profesor,Ciudad

admin.site.register(Ciudad)
admin.site.register(Colegio)
admin.site.register(Profesor)
