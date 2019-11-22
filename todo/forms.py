from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class UserForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='e-mail')
        

    def __init__(self, *args, **kwargs):
        

        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'first_name',
            'last_name',
            'email',
            Submit('submit','Submit',css_class='btn-success')
        )
        super().__init__(*args, **kwargs)