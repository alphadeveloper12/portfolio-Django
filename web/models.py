from django.db import models
from ckeditor.fields import RichTextField

class PersonalDetails(models.Model):
    name = models.CharField(max_length=100)
    about_heading = models.CharField(max_length=200)
    about_details = models.TextField()
    cv = models.FileField(upload_to='cv_pdfs/')
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    facebook = models.URLField(blank=True, null=True)
    discord = models.CharField(max_length=50, blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Achievement(models.Model):
    personal_details = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='achievement_icons/')
    detail_image = models.ImageField(upload_to='achievement_detail/')
    details = RichTextField()
    heading = models.CharField(max_length=200)

    def __str__(self):
        return self.heading

class LanguageSkill(models.Model):
    personal_details = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    percentage = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Engine(models.Model):
    personal_details = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    percentage = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Story(models.Model):
    personal_details = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='story_images/')
    details = models.TextField()
    delivered_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonial_images/')
    designation = models.CharField(max_length=100)
    details = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question