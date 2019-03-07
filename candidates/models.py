from django.db import models

class Candidate(models.Model):
    ID = models.PositiveIntegerField('參選號碼', unique=True)
    Firstname = models.CharField('名字')
    Lastname = models.CharField('姓')
    age = models.PositiveIntegerField('年齡')
    Politics = models.TextField('政見')
    Vote = models.PositiveIntegerField('得票數')