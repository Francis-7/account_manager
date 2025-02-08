from django.db import models
from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r'^\+?(\d{1,3})?(\d{10})$', message="Phone number must be in the format shown")

# Create your models here.
class Account(models.Model):
    PURPOSE = models.TextChoices('PURPOSE', 'Solo, Multipurpose')
    purpose = models.CharField(max_length=20, choices=PURPOSE)
    # record = models.OneToOneField("MultiPurposeRecord", on_delete=models.CASCADE)


    class Meta:
        abstract = True

class UserAccount(models.Model):
    name = models.CharField(max_length=30)
    date_opened = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'useraccount'

    def __str__(self):
        return f"{self.name} was created on {self.date_opened}"


class SoloRecord(models.Model):
    # user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    record = models.CharField(max_length=100)
    value = models.FloatField()  # for inputing figures in the form of money

    class Meta:
        abstract = True

class MultiPurposeRecord(models.Model):
    # user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    record = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=15, decimal_places=2)  # for inputing figures in the form of money

    class Meta:
        abstract = True

class UserData(models.Model):
    useraccount = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, validators=[phone_regex], help_text='+234-0000 or 0<your phone number>')

    class Meta:
        db_table = 'userdata'

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
    
class Entry(MultiPurposeRecord):
    userdata = models.ForeignKey(UserData, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'entry'
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.record}"
