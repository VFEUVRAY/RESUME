from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.template import loader
from django.http import Http404

# Create your views here.

def index(request):
    template = loader.get_template('infos/cv.html')
    try:
        me = User.objects.get(id=1)
    except User.DoesNotExist:
        raise Http404("No user of given id was found")
    skills = {
        "section" : Section.objects.get(id=2).name,
        #"subsections" : SubSection.objects.get(section_id=2),
    }
    education_paragraphs = {
        "title" : Section.objects.get(id=5),
        "sub_sections" : SubSection.objects.filter(section_id=5),
        #"paragraph" : Paragraph.objects.filter(section_id=5),
    }
    projects_paragraphs = {
        "title" : Section.objects.get(id=6),
        "sub_sections" : SubSection.objects.filter(section_id=6),
        #"paragraph" : Paragraph.objects.filter(section_id=6),
    }
    professional_paragraphs = {
        "title" : Section.objects.get(id=7),
        "sub_sections" : SubSection.objects.filter(section_id=7),
        #"paragraph" : Paragraph.objects.filter(section_id=7),
    }
    context = {
        "me" : me,
        "title" : SubSection.objects.get(id=17),
        "contact_title" : Section.objects.get(id=1).name,
        "profile_title" : Section.objects.get(id=4).name,
        "profile_text" : Paragraph.objects.get(id=7).text,
        "skills" : skills,
        "sub_skill" : SubSection.objects.filter(section_id=2),
        "hobbies" : Section.objects.get(id=3).name,
        "sub_hobbies" : SubSection.objects.filter(section_id=3),
        "main" : [education_paragraphs, projects_paragraphs, professional_paragraphs],
    }
    return HttpResponse(template.render(context, request))