from django.db import models

# Create your models here.

class Home(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField( null=True, blank=True, upload_to='portfolio/images/')
    role = models.CharField(max_length=250, null=True, blank=True)
    about = models.TextField( null=True, blank=True)
    file = models.FileField(null=True, blank=True, upload_to='portfolio/files/')
    years_of_experiance = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return 'Home'

    class Meta:
        verbose_name_plural = 'Home'
    

class Skill(models.Model):
    name = models.CharField(max_length=250)
    progressbar_color = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    

class TimeLine(models.Model):
    duration = models.CharField(max_length=250)
    role = models.CharField(max_length=250)
    company = models.CharField(max_length=250)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'({self.time}) {self.role} - {self.company}'
    

class Portfolio(models.Model):
    title_text = models.TextField()

    def __str__(self):
        return "Portfolio text"
    

class Project(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField()

    def __str__(self):
        return self.title
    

class Links(models.Model):
    project = models.ForeignKey(Project, related_name='links', on_delete=models.CASCADE)
    icon_class = models.CharField(max_length=250)
    icon_link= models.URLField( max_length=2000)
    
class Contact(models.Model):
    text = models.TextField()
    location = models.CharField( max_length=250)
    email = models.EmailField(max_length=254)
    education = models.CharField( max_length=500)
    mobile_number = models.CharField(max_length=30)
    languages = models.CharField( max_length=250)

    def __str__(self):
        return 'Contact details'
    

class SocialMedia(models.Model):
    title = models.CharField(max_length=50)
    icon_class = models.CharField(max_length=250)
    icon_link = models.URLField( max_length=2000)

    def __str__(self):
        return self.title
    

class Message(models.Model):
    name = models.CharField( max_length=500)
    email = models.EmailField( max_length=254)
    subject = models.CharField( max_length=500)
    text = models.TextField()
    
    def __str__(self):
        return self.name
    