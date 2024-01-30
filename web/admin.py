from django.contrib import admin
from .models import PersonalDetails, Achievement, LanguageSkill, Engine, Story
from .models import Testimonial, FAQ

@admin.register(PersonalDetails)
class PersonalDetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'about_heading', 'address', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('personal_details', 'icon', 'heading')
    search_fields = ('personal_details__name', 'heading')

@admin.register(LanguageSkill)
class LanguageSkillAdmin(admin.ModelAdmin):
    list_display = ('personal_details', 'name', 'percentage')

@admin.register(Engine)
class EngineAdmin(admin.ModelAdmin):
    list_display = ('personal_details', 'name', 'percentage')

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('personal_details', 'name', 'image', 'details')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')
    search_fields = ('name', 'designation')

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)
    search_fields = ('question',)
