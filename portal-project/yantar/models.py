from django.db import models

# Create your models here.
class Certificatestore(models.Model):
    fio = models.TextField(blank=True, null=True)
    numberkey = models.TextField(db_column='numberKey', blank=True, null=True)
# Field name made lowercase.
    beforedate = models.DateField(db_column='beforeDate', blank=True, null=True)
  # Field name made lowercase.
    afterdate = models.DateField(db_column='afterDate', blank=True, null=True)
# Field name made lowercase.
    commentary = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CertificateStore'