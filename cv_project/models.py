from djongo import models
import uuid

# from django.db.models.fields import BinaryField, CharField
# from django.db.models.fields.related import ForeignKey

# Create your models here.

#profile Models:


class Cv_user(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    cv_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return str(self.cv_name)



class Profile(models.Model):
    profile_cv = models.ForeignKey(Cv_user, on_delete=models.CASCADE)
    avartar = models.ImageField(
        null=True, blank=True, default="morning.jpg")
    fullname = models.CharField(max_length=30)
    birth = models.DateField()
    gender = models.CharField(max_length=5)
    email = models.EmailField()
    mobile = models.IntegerField()
    address = models.CharField(max_length=100)
    github = models.CharField(max_length=255, blank=True)
    facebook = models.CharField(max_length=255, blank=True)
    twitter = models.CharField(max_length=255, blank=True)
    website = models.CharField(max_length=255, blank=True)
                    
    def __str__(self):
        return str(f'Mục tiêu  nghề nghiệp {self.fullname}')


class Objective(models.Model):
    Objective_cv = models.ForeignKey(Cv_user, on_delete=models.CASCADE)
    Objective_content = models.TextField()

    def __str__(self):
        return str(self.Objective_cv)


class Education(models.Model):
    education_cv = models.ForeignKey(Cv_user, on_delete=models.CASCADE)
    education_school = models.CharField(max_length=50)
    education_major = models.CharField(max_length=40)
    education_start = models.DateField()
    education_end = models.DateField()

    def __str__(self):
        return str(self.education_school)

  
class Experience(models.Model):
    experience_cv = models.ForeignKey(Cv_user, on_delete=models.CASCADE)
    experience_company = models.CharField(max_length=50)
    experience_position = models.CharField(max_length=40)
    experience_details = models.TextField()
    experience_start = models.DateField()
    experience_end = models.DateField()

    def __str__(self):
        return str(self.experience_company)


class Additional(models.Model):
    additional_cv = models.ForeignKey(Cv_user, on_delete=models.CASCADE)
    additional_title = models.CharField(max_length=40)
    additional_details = models.TextField()

    def __str__(self):
        return str(self.additional_title)
    

class Certification(models.Model):
    certification_cv = models.ForeignKey(Cv_user, on_delete=models.CASCADE)
    certification_title = models.CharField(max_length=40)
    certification_time = models.DateField()
    certification_details = models.TextField()

    def __str__(self):
        return str(self.certification_title)


class Activity(models.Model):
    activity_cv = models.ForeignKey(Cv_user, on_delete=models.CASCADE)
    activity_title = models.CharField(max_length=40)
    activity_start = models.DateField()
    activity_end = models.DateField()
    activity_position = models.CharField(max_length=50)
    activity_details = models.TextField()
    source = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.activity_title)


class Skill(models.Model):
    skill_cv = models.ForeignKey(Cv_user, on_delete=models.CASCADE)
    skill_title = models.CharField(max_length=15)
    skill_level = models.SmallIntegerField()

    def __str__(self):
        return str(self.skill_title)


class Language(models.Model):
    language_cv = models.ForeignKey(Cv_user, on_delete=models.CASCADE)
    language_title = models.CharField(max_length=10)
    language_level = models.CharField(max_length=10)

    def __str__(self):
        return str(self.language_title)



