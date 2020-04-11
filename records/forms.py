from django import forms

DEPT_CHOICES = (
    ('ME', 'Mechanical Engineering'),
    ('EE', 'Electrical Engineering'),
    ('CE', 'Civil Engineering'),
    ('CTE', 'Computer Engineering'),
    ('AE', 'Agricultural Engineering'),
    ('CS', 'Computer Science'),
    ('SLT', 'Science Laboratory Technology'),
    ('FST', 'Food Science Technology'),
    ('PT', 'Pharmaceutical Technology'),
    ('DOP', 'Dispensary and Opticiary')
)
class DeptForm(forms.Form):
    dept = forms.CharField(
        max_length=20,
        widget=forms.Select(choices=DEPT_CHOICES)
    )
    name = forms.CharField(label='Your name', max_length=200)
    amount = forms.DecimalField(label='amount', max_digits=10, decimal_places=2)
    balance = forms.DecimalField(label='balance', max_digits=10, decimal_places=2)
    total = forms.DecimalField(label='total', max_digits=10, decimal_places=2)