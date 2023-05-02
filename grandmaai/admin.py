from django.contrib import admin
from .models import Goal, Level, Email, Phone

class GoalAdmin(admin.ModelAdmin):
    search_fields = ['content']


admin.site.register(Goal, GoalAdmin)

class LevelAdmin(admin.ModelAdmin):
    search_fields = ['level']


admin.site.register(Level, LevelAdmin)

class EmailAdmin(admin.ModelAdmin):
    search_fields = ['email']


admin.site.register(Email, EmailAdmin)

class PhoneAdmin(admin.ModelAdmin):
    search_fields = ['phone']


admin.site.register(Phone, PhoneAdmin)

