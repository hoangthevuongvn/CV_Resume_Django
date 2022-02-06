from django.shortcuts import render
from django.http import HttpResponse
from . untils import *

# Create your views here.
def hello(request):
    return render(request, 'cv_project/hello.html', {})

def cv(request):
    full_list = profile_list() #profilelist = {'fullname': fullname, 'birth': birth, 'gender': gender, 'mobile' : mobile, 'address': address }
    full_list.update(objective_list())
    full_list['educationlist'] = education_list()
    full_list['experiencelist'] = experience_list()
    full_list['additionallist'] = additional_list()
    full_list['certificationlist'] = certification_list()
    full_list['activitylist'] = activity_list()
    full_list['skilllist'] = skill_list()
    full_list['languagelist'] = language_list()
    print(full_list['activitylist'])
    return render(request, 'cv_project/cv.html', full_list)
# Create your views here.






