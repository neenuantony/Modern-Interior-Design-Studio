from django.db import models

# Create your models here.

class register(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    username=models.CharField(max_length=25)
    email=models.EmailField()
    phone=models.IntegerField()
    gender=models.CharField(max_length=10)
    address=models.CharField(max_length=200)
    dob=models.DateField()
    password=models.CharField(max_length=20)

class fileupload(models.Model):
    filename=models.CharField(max_length=50)
    fileimage=models.FileField(upload_to='djangoapp/static')
    description=models.CharField(max_length=200)

class emp_register(models.Model):
    emp_name=models.CharField(max_length=20)
    email=models.EmailField()
    company_name=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    password=models.CharField(max_length=25)

class uploads(models.Model):
    audioname=models.CharField(max_length=20)
    audio=models.FileField(upload_to='djangoapp/static')
    videoname=models.CharField(max_length=20)
    video=models.FileField(upload_to='djangoapp/static')
    pdfname=models.CharField(max_length=20)
    pdf=models.FileField(upload_to='djangoapp/static')


class select_checks_model(models.Model):
    choice=[
        ('Kerala','KERALA'), #(database,label(template))
        ('Tamilnadu','TAMIL NADU'),
        ('Karnadaka','KARNADAKA'),
        ('Kashmir','KASHMIR'),
        ('Gujrat','GUJRAT')
    ]

    name=models.CharField(max_length=50)
    state=models.CharField(max_length=30,choices=choice)
    english=models.BooleanField(default=False)
    malayalam=models.BooleanField(default=False)
    hindi=models.BooleanField(default=False)