from django.contrib import admin
from .models import Phone, User, Section, Paragraph, SubSection

# Register your models here.
admin.site.register(User)
admin.site.register(Phone)
admin.site.register(Section)
admin.site.register(Paragraph)
admin.site.register(SubSection)
