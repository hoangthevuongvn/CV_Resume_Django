from . models import *
import datetime
def profile_list():
    profile_query = Profile.objects.all()
    profilelist = []
    
    for i in profile_query:
        profilelist.append({'fullname': i.fullname, 'avartar': i.avartar, 'birth': i.birth, 'gender': i.gender, 'email': i.email, 'mobile' : f'0{i.mobile}', 'address': i.address, 'facebook': i.facebook, 'twitter': i.twitter, 'github': i.github, 'website': i.website})
    return profilelist[0]

def objective_list():
    objective_query = Objective.objects.all()
    objectivelist = []

    for i in objective_query:
        objectivelist.append({'objective': i.Objective_content})
    return objectivelist[0]
def education_list():
    education_query = Education.objects.all()
    educationlist = []

    for i in education_query:
        educationlist.append({'school': i.education_school, 'major': i.education_major, 'education_start': i.education_start, 'education_end': i.education_end})
    return educationlist

def experience_list():
    experience_query = Experience.objects.all()
    experiencelist = []

    for i in experience_query:
        experiencelist.append({'company': i.experience_company, 'experience_position': i.experience_position, 'experience_details': i.experience_details, 'experience_start': i.experience_start, 'experience_end': i.experience_end})
    return experiencelist

def additional_list():
    additional_query = Additional.objects.all()
    additionallist = []

    for i in additional_query:
        additionallist.append({'additional_title': i.additional_title, 'additional_details': i.additional_details})
    return additionallist

def certification_list():
    certification_query = Certification.objects.all()
    certificationlist = []

    for i in certification_query:
        certificationlist.append({'certification_title': i.certification_title, 'certification_time': i.certification_time, 'certification_details': i.certification_details})
    return certificationlist

def activity_list():
    activity_query = Activity.objects.all()
    activitylist = []

    for i in activity_query:
        activitylist.append({'activity_title': i.activity_title, 'activity_start': i.activity_start, 'activity_end': i.activity_end, 'activity_position': i.activity_position, 'activity_details': i.activity_details, 'source': i.source})
    return activitylist

def skill_list():
    skill_query = Skill.objects.all()
    skilllist = []

    for i in skill_query:
        skilllist.append({'skill_title': i.skill_title, 'skill_level': i.skill_level})
    return skilllist

def language_list():
    language_query = Language.objects.all()
    languagelist = []

    for i in language_query:
        languagelist.append({'language_title': i.language_title, 'language_level': i.language_level})
    return languagelist
