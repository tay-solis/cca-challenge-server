from django.shortcuts import render
import json
from .models import Section
from django.http import JsonResponse, HttpResponse

# Create your views here.
def all_sections(req):
    sections = Section.objects.all()
    section_list = [section.to_json for section in sections]
    return HttpResponse(json.dumps(section_list), content_type="application/json")

def section_detail(req):
    section = Section.objects.get(id = section_id)
    section_info = [section.to_json]
    return HttpResponse(json.dumps(section_info), content_type="application/json")

def section_register(req, section_id):
    section = Section.objects.get(id = section_id)
    if section.capacity == section.registered:
        return HttpResponse('Section is full.', status = 401)
    else: 
        section.register()
        section_info = [section.to_json()]
        return HttpResponse(json.dumps(section_info), content_type="application/json")

def section_drop(req, section_id):
    section = Section.objects.get(id = section_id)
    section.drop()
    section_info = [section.to_json()]
    return HttpResponse(json.dumps(section_info), content_type="application/json")

