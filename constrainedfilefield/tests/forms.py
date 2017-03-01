from django import forms
from .models import TestModel, TestModelNoValidate, TestElement


class TestModelForm(forms.ModelForm):
    class Meta:
        model = TestModel


class TestModelNoValidateForm(forms.ModelForm):
    class Meta:
        model = TestModelNoValidate


class TestElementForm(forms.ModelForm):
    the_file = forms.FileField(required=False, )

    class Meta:
        model = TestElement
        fields = ['the_file']

    def __init__(self, container, *args, **kwargs):
        super(TestElementForm, self).__init__(*args, **kwargs)
        self.container = container
        self.fields['the_file'].validators[0].update_quota(
            items=self.container.test_elements.all(),
            attr_name='the_file',
        )

    def save(self, *args, **kwargs):
        element = super(TestElementForm, self).save(commit=False)
        element.container = self.container
        element.save()