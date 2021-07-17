from django.db import models

class Student(models.Model):
    number= models.IntegerField('학번')
    name = models.CharField('이름',max_length=20)
    major = models.ForeignKey(verbose_name="주전공", to='e.Department', on_delete=models.SET_NULL,null=True)
    friends= models.ManyToManyField(verbose_name="친구들",to='self',db_table='e_friendship',blank=True)
    
    def __str__(self):
        return self.name

class Department(models.Model):
    name=models.CharField("학과명",max_length=20)
    head=models.CharField("학과장",max_length=20)
    
    def __str__(self):
        return self.name