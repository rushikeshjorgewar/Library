from calendar import week
from datetime import datetime
from xml.dom import VALIDATION_ERR
from django import forms


class renewBookForm(forms.form):
    renewal_date=forms.DateField(help_text='enter the date of returning book')
    
    def clean_renewal_date(self):
        data=self.cleaned_data['renewal_data']
        
        if data<datetime.today():
            raise VALIDATION_ERR('invalid date field. it is in the past.')
        
        if data>datetime.today()+datetime.time(week=4):
            raise VALIDATION_ERR('invalid date field. it exceeds the borrowing date')
        
        return data
    
    
    
    