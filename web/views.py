from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    personal_details = PersonalDetails.objects.first()
    achievements = Achievement.objects.filter(personal_details=personal_details)
    language_skills = LanguageSkill.objects.filter(personal_details=personal_details)
    engines = Engine.objects.filter(personal_details=personal_details)
    stories = Story.objects.filter(personal_details=personal_details)
    faqs = FAQ.objects.all()
    testimonials = Testimonial.objects.all()

    context = {
        'personal_details': personal_details,
        'achievements': achievements,
        'language_skills': language_skills,
        'engines': engines,
        'stories': stories,
        'faqs': faqs,
        'testimonials': testimonials,
    }

    return render(request, 'index.html', context=context)