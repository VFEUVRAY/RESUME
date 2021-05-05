from django.db import models

# Create your models here.

class Phone(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=15)

class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phone_id = models.ForeignKey(Phone, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    github = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=50)
    github_display = models.CharField(max_length=50, blank=True, null=True)
    linkedin_display = models.CharField(max_length=50, blank=True, null=True)

class Section(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

class SubSection(models.Model):
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    text = models.CharField(max_length=500, blank=True, null=True)
    paragraph = models.CharField(max_length=500, blank=True, null=True)

class Paragraph(models.Model):
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)

