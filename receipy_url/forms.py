'''
Created on Mar. 26, 2022

@author: Louis-Philippe
'''
from django import forms

class UrlForm(forms.Form):
    url_name = forms.URLField(label="Receipy URL", max_length=300)


class ReceipyProcessingForm(forms.Form):
    # determines how the form works and appears
    # fields map to HTML input element
    # the field are themselfs classes
    # each type of field have associated wideget that can be overrithen
    
    # has a is_valid() method to validate form inputs
    # has a cleaned_data attribute once is_valid() retruns True
    
    # the data will be sent back to a view
    '''
    the form will be pre-populated, this one will be pre-populated from
    our scraping script from the previous HTMl form submission.
    This form should be bound (data is associated with it)
    
    '''
    receipy_name = forms.CharField(max_length=200)
    receipy_yield = forms.NumberInput()
    # variable number of field