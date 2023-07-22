from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, SelectField, IntegerField,PasswordField, SearchField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
# from app import Person


class RegistrationForm(FlaskForm):
    id = IntegerField('id', validators=[(DataRequired())])
    name = StringField('name', validators=[(DataRequired())])
    yearCompleted= SelectField('yearCompleted', choices=[(2021,2021)])
    nationality = StringField('nationality',validators=[DataRequired()] )
    contact= StringField('contact',validators=[ DataRequired(), Length(min=10, max=10, message="Your number shouldn't be less than 10")])
    email = StringField('email',validators=[(DataRequired() )])
    faculty = SelectField('faculty',  choices=[('Faculty/School','Faculty/School'),('Joy Otabil', 'Joy Otabil'), ('Faith','Faith'), ('Freedom','Freedom'), ('Kathryl Kuhlman ', 'Kathryl Kuhlman '), ('Justice','Justice'), ('Billy Graham','Billy Graham'),('Billy Graham','Billy Graham'),  ('Chancellor', 'Chancellor'),('Integerity','Integerity'), ], default=None )
    hallofresidence = SelectField('hallofresidence',  choices=[('Halls','Halls'),('Joy Otabil', 'Joy Otabil'), ('Faith','Faith'), ('Freedom','Freedom'), ('Kathryl Kuhlman ', 'Kathryl Kuhlman '), ('Justice','Justice'), ('Billy Graham','Billy Graham'),('Billy Graham','Billy Graham'),  ('Chancellor', 'Chancellor'),('Integerity','Integerity'), ], default=None )
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Register')

class Adduser(FlaskForm):
    fullname = StringField('fullname')
    indexnumber= StringField('indexnumbe')
    gender= SelectField('gender', choices=[('Gender','Gender'),('Male', 'Male'), ('Female','Female') ], default=None )
    school=SelectField('school',choices=[('Select Faculty','Select Faculty'),('School of Engineering and Technology', 'School of Engineering and Technology'), ('Central Business School','Central Business School'), ('Faculty of Arts and Social Sciences','Faculty of Arts and Social Sciences'), ('Faculty of Law', 'Faculty of Law '), ('School of Architecture and Design','School of Architecture and Design'), ('School of Graduate and Research Studies','School of Graduate and Research Studies'),('School of Pharmacy','School of Pharmacy'),('School of Medicine and Health Sciences', 'School of Medicine and Health Sciences'),('Theology and Missions','Theology and Missions'),('Vision and Life','Vision and Life'), ], default=None )
    department=SelectField('department',choices=[('Select Department','Select Department'),('Computer Science Department', 'Computer Science Department'), ('Information Technology Department','Information Technology Department'), ('Civil Engineering Department','Civil Engineering Department'), ('Nursing Department ', 'Nursing Department '), ('Human Resource Department','Human Resource Department'), ('Faculty of Law','Faculty of Law'),('Communication Department','Communication Department'),  ('Environment Development Studies Department', 'Environment Development Studies Department'),('Accounting Department','Accounting Department'), ], default=None )
    program= SelectField('program',choices=[('Select Program','Select Program'),('BSc.Information Technology', 'BSc.Information Technology'), ('BSc.Computer Science','BSc.Computer Science'), ('Doctor of Pharmacy','Doctor of Pharmacy'), ('BSc.Business Administration ', 'BSc.Business Administration '), ('BSc.Nursing','BSc.Nursing'), ('BSc.Architecture','BSc.Architecture'),('BSc.Planning','BSc.Planning'),  ('BSc.Environment and Development Studies', 'BSc.Environment and Development Studies'),('BSc. Environmental Engineering','BSc. Environmental Engineering'), ], default=None )
    completed= SelectField('completed',choices=[(2000,2000),(2001,2001),(2002,2002),(2003,2003),(2004,2004),(2005,2005),(2006,2006),(2007,2007),(2008,2008),(2009,2009),(2010,2010),(2011,2011),(2012,2012),(2013,2013),(2014,2014),(2015,2015),(2016,2016),(2017,2017),(2018,2018),(2019,2019),(2020,2020),(2021,2021), (2022,2022)])
    admitted=SelectField('admitted',choices=[(2000,2000),(2001,2001),(2002,2002),(2003,2003),(2004,2004),(2005,2005),(2006,2006),(2007,2007),(2008,2008),(2009,2009),(2010,2010),(2011,2011),(2012,2012),(2013,2013),(2014,2014),(2015,2015),(2016,2016),(2017,2017),(2018,2018),(2019,2019),(2020,2020),(2021,2021), (2022,2022)])
    email= StringField('email')
    telephone= StringField('telephone')
    hall= SelectField('hall', choices=[('Faculty/School','Faculty/School'),('Joy Otabil', 'Joy Otabil'), ('Faith','Faith'), ('Freedom','Freedom'), ('Kathryl Kuhlman ', 'Kathryl Kuhlman '), ('Justice','Justice'), ('Billy Graham','Billy Graham'),('Billy Graham','Billy Graham'),  ('Chancellor', 'Chancellor'),('Integerity','Integerity'), ], default=None )
    nationality= SelectField('nationality',choices=[('Ghanaian','Ghanaian'),('Nigerian', 'Nigerian'), ('Togolese','Togolese'), ('Beninese','Beninese'), (' Burkinabe ', 'Burkinabe'), ('Angolan','Angolan'), ('Cameroonian','Cameroonian'),('Central African','Central African'),  ('Guinean', 'Guinean'),('Kenyan','Kenyan'), ], default=None )
    address= StringField('address')
    work= StringField('work')
    guardian= StringField('guardian')
    marital= SelectField('Marital',  choices=[('Marital Status','Marital Status'),('Married', 'Married'), ('Divored','Divored') ], default=None )
    picture = FileField('Add a picture', validators=[ FileAllowed(['jpg', 'png','jpeg'])])
    extra= StringField('extra')
    submit = SubmitField('Register')
    image_file = FileField('image_file', validators=[FileAllowed(['jpg', 'png'])])
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
 
class Registration(FlaskForm):
    #indexNumber= StringField('indexNumber', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    
    submit = SubmitField('SignUp')  
    
    # el4 = SelectField('el4', default='None', choices=[(user.lastname, user.lastname) for user in Person.query.all()])
  
    
    #Program = SelectField('programs', choices=[("one", "one"),("two", "two"),("three", "three")])
    submit =SubmitField('submit')
    
# create a search form
class Search(FlaskForm):
    searched = StringField('Searched', validators=[DataRequired()])
    submit = SubmitField('Search') 
    
    
    
class Alumni(FlaskForm):
    email= StringField('email', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    submit = SubmitField('SignUp')  
    

class AlumniSignin(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    indexnumber = StringField('indexnumber', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    
    submit = SubmitField('SignUp')  
    