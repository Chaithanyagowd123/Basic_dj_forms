from django import forms



g=[['MALE','MAle'],['FEMALE','FEmaLE']]
c=[['PYThon','PYTHON'],['DJANGO','django']]
class NameForm(forms.Form):
    Sname=forms.CharField()
    Sage=forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea(attrs={'cols':7,'rows':5}))
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)

    #course=forms.MultipleChoiceField(choices=c)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
