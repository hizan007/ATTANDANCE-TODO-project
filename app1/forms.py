from django import forms

from app1.models import attandance

class dateinput(forms.DateInput):
    input_type = 'date'

ATT=(
    ('PRESENT','PRESENT'),
    ('ABSENT','ABSENT')
)

BATCH=(
    ('CSE','CSE'),
    ('MEC','MEC'),
    ('ECE','ECE'),
    ('OTHER','OTHER')
)


class attandanceform(forms.ModelForm):
    studentyear= forms.DateField(widget=dateinput)
    attandance=forms.ChoiceField(choices=ATT)
    studentbatch=forms.ChoiceField(choices=BATCH)
    class Meta:
        model = attandance
        fields = '__all__'

