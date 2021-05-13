from django.db import models
import datetime

# Create your models here.


class ORGANIZATION(models.Model):
    INN = models.TextField(primary_key=True, unique=True)
    NAME = models.TextField()
    DOC_RESP_PERSON = models.FileField(upload_to='ORG/', blank=True)

    def __str__(self):
        return self.NAME

class ROLE(models.Model):
    NAME = models.CharField(max_length=50)

    def __str__(self):
        return self.NAME

class WORKER(models.Model):
    FIO = models.TextField(blank=False, null=False)
    ORG_INN = models.ForeignKey(ORGANIZATION, on_delete=models.CASCADE)
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
    ORG_INN = models.ForeignKey(ORGANIZATION, on_delete=models.CASCADE)
    CLIENT_ID = models.ForeignKey(
        WORKER, related_name='client2org', on_delete=models.CASCADE, parent_link=True)
    RESP_PERSONE_ID = models.ForeignKey(
        WORKER, related_name='respperson2org', on_delete=models.CASCADE, parent_link=True)
    REQUEST_TYPE = models.CharField(
        max_length=25, choices=TYPE_CHOICE, default='Предоставление доступа')
    ADDED_ROLES = models.ManyToManyField(ROLE)
    GETTING_TIME = models.DateField(default=datetime.date.today(), blank=False)
    NUMBER = models.TextField(blank=True, null=True)
    EXECUTOR = models.TextField(blank=True, null=True)
    RESULT = models.CharField(
        max_length=25, choices=RESULTS_CHOICE, default='Исполнено')
    COMMENT = models.TextField(blank=True, null=True)
    MESSAGE_NUMBER = models.TextField(blank=True, null=True)
    MESSAGE_DATA = models.DateField(blank=True, null=True)
    TRACK_NUMBER = models.TextField(blank=True)
    IsDEBTOR = models.BooleanField(default=False)
