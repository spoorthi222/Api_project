from django.db import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50 , default="N/A")
    age  = models.IntegerField(default=18)
    gender = models.CharField(max_length=6 , default="common")
    email_id = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=30, default="")
    salt =  models.CharField(max_length=20 , default="")


    def save(self, *args, **kwargs):
        return super(Users, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table = 'users'
        app_label = 'src'