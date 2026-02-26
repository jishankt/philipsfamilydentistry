from django.contrib import admin
from .models import (
    Service,
    Appointment,
    Testimonial,
    Gallery,
    Doctor
)

admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(Testimonial)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title']
    
admin.site.register(Doctor)