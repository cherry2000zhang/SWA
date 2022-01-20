from wtforms import Form, StringField,RadioField,SelectField,TextAreaField,validators, SelectMultipleField,widgets
from wtforms.fields import EmailField, DateField
from wtforms.widgets import PasswordInput

class CreateUserForm(Form):
    first_name=StringField('First Name',[validators.Length(min=1,max=150),validators.DataRequired()])
    last_name=StringField('Last Name',[validators.Length(min=1,max=150),validators.DataRequired()])
    gender=SelectField('Gender',[validators.DataRequired()],choices=[("",'Select'),('F','Female'),('M','Male')],default="")
    membership=RadioField('Membership',choices=[('F','Fellow'),('S','Senior'),('P','Professional')],default='F')
    remarks=TextAreaField('Remarks',[validators.Optional()])

class CreateCustomerForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    date_joined = DateField('Date Joined', format='%Y-%m-%d')
    address = TextAreaField('Mailing Address', [validators.length(max=200), validators.DataRequired()])
    membership = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')], default='F')
    remarks = TextAreaField('Remarks', [validators.Optional()])
    contactby = SelectMultipleField('Contact by',
                                  choices=[('P', 'Phone'), ('E', 'Email'),('S','SMS')], default='',
                                  option_widget=widgets.CheckboxInput(),
                                  widget=widgets.ListWidget(prefix_label=False)
                                    )

class CreateLoginForm(Form):
    userID=StringField('User ID',[validators.DataRequired()])
    userPwd=StringField('Password',[validators.DataRequired()], widget=PasswordInput(hide_value=False))

class createCompanyForm(Form):
    companyID=StringField('Company ID',[validators.DataRequired()])
    companyName=StringField('Company Name',[validators.DataRequired()])
