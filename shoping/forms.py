from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('editor',)


    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name', '')
        description = cleaned_data.get('description', '')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in name.lower() or word in description.lower():
                raise forms.ValidationError('Нельзя добавлять запрещенные слова в название или описание продукта')
        return cleaned_data



class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['version_indicator'].label = 'Активная версия'
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-10'
        self.helper.add_input(Submit('submit', 'Сохранить'))


    def clean_version_indicator(self):
        version_indicator = self.cleaned_data.get('version_indicator')
        if version_indicator:
            product = self.cleaned_data.get('product')
            active_versions_count = Version.objects.filter(product=product, version_indicator=True).count()
            if active_versions_count > 0:
                raise forms.ValidationError('Может быть только одна активная версия для каждого продукта')
        return version_indicator