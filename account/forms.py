from django.forms import ModelForm
from .models import UserData, UserAccount, Entry

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['record', 'value']

    def __init__(self, *args, **kwargs):
        self.userdata = kwargs.pop('userdata', None)
        super().__init__(*args, **kwargs)

        if self.userdata:
           self.instance.userdata = self.userdata

class UserDataForm(ModelForm):
    class Meta:
        model = UserData
        fields = ['first_name', 'last_name', 'email', 'phone']

    def __init__(self, *args, **kwargs):
        self.useraccount = kwargs.pop('useraccount', None)
        super().__init__(*args, **kwargs)

        if self.useraccount:
            self.instance.useraccount = self.useraccount
            # self.fields['useraccount'].disabled = True

class UserAccountForm(ModelForm):
    class Meta:
        model = UserAccount
        fields = '__all__'