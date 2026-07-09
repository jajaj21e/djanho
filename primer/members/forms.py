from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Row, Column

from .models import Member

class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ['firstname', 'lastname']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('firstname', css_class='form-group col-md-6 mb-0'),
                Column('lastname', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Submit')
        )
