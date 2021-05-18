from django.db import models
import datetime

# Create your models here.


class Organization(models.Model):
    INN = models.CharField(max_length=25, primary_key=True, unique=True)
    NAME = models.CharField(max_length=250)
    DOC_RESP_PERSON = models.FileField(upload_to='ORG/', blank=True)

    def __str__(self):
        return self.NAME

class Role(models.Model):
    NAME = models.CharField(max_length=50)

    def __str__(self):
        return self.NAME

class Worker(models.Model):
    FIO = models.CharField(max_length=100, blank=False, null=False)
    ORG_INN = models.ForeignKey(Organization, on_delete=models.CASCADE)
    DOC_AGREEMENT = models.FileField(upload_to='WORKERS/', blank=True)
    ADDITIONAL_INFO = models.TextField(blank=True)
    RESP_PERSONE = models.BooleanField(default=False)

    def __str__(self):
        return self.FIO

class EbRequest(models.Model):
    RESULTS_CHOICE = [
        ('Исполнено', 'Исполнено'),
        ('Отказано', 'Отказано'),
        ('В процессе', 'В процессе')
    ]
    TYPE_CHOICE = [
        ('Предоставление доступа', 'Предоставление доступа'),
        ('Добавление полномочий', 'Добавление полномочий'),
        ('Прекращение доступа', 'Прекращение доступа'),
        ('Смена сертификата', 'Смена сертификата')
    ]
    ORG_INN = models.ForeignKey(Organization, on_delete=models.CASCADE)
    CLIENT_ID = models.ForeignKey(
        Worker, related_name='client2org', on_delete=models.CASCADE, parent_link=True)
    RESP_PERSONE_ID = models.ForeignKey(
        Worker, related_name='respperson2org', on_delete=models.CASCADE, parent_link=True)
    REQUEST_TYPE = models.CharField(
        max_length=25, choices=TYPE_CHOICE, default='Предоставление доступа')
    ADDED_ROLES = models.ManyToManyField(Role, blank=True)
    GETTING_TIME = models.DateField(default=datetime.date.today(), blank=False)
    NUMBER = models.CharField(max_length=25, blank=True, null=True)
    EXECUTOR = models.CharField(max_length=100, blank=True, null=True)
    RESULT = models.CharField(
        max_length=25, choices=RESULTS_CHOICE, default='Исполнено')
    COMMENT = models.TextField(blank=True, null=True)
    MESSAGE_NUMBER = models.CharField(max_length=25, blank=True, null=True)
    MESSAGE_DATA = models.DateField(blank=True, null=True)
    TRACK_NUMBER = models.CharField(max_length=50,blank=True)
    IsDEBTOR = models.BooleanField(default=False)
