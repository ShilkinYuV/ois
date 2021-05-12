from django.db import models

# Create your models here.


class ORGANIZATION(models.Model):
    INN = models.TextField(primary_key=True, unique=True)
    NAME = models.TextField()
    DOC_RESP_PERSON = models.FileField(upload_to='ORG/', name=str(INN))

    def __str__(self):
        return self.NAME


class CLIENT(models.Model):
    FIO = models.TextField(blank=False, null=False)
    ORG_INN = models.ForeignKey(ORGANIZATION, on_delete=models.CASCADE)
    DOC_AGREEMENT = models.FileField(upload_to='CLIENTS/')
    RESP_PERSONE = models.BooleanField()

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
        CLIENT, related_name='client2org', on_delete=models.CASCADE, parent_link=True)
    RESP_PERSONE_ID = models.ForeignKey(
        CLIENT, related_name='respperson2org', on_delete=models.CASCADE, parent_link=True)
    REQUEST_TYPE = models.CharField(
        max_length=25, choices=TYPE_CHOICE, default='new')
    GETTING_TIME = models.DateField(db_column='GETTING_TIME', blank=False)
    NUMBER = models.TextField(blank=True, null=True)
    EXECUTOR = models.TextField(blank=True, null=True)
    RESULT = models.CharField(
        max_length=25, choices=RESULTS_CHOICE, default='pro')
    COMMENT = models.TextField(blank=True, null=True)
    MESSAGE_NUMBER = models.TextField(blank=True, null=True)
    MESSAGE_DATA = models.DateField(db_column='MESSAGE_DATA', blank=False)
    TRACK_NUMBER = models.TextField(blank=True, null=True)
