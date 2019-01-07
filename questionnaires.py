from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, IntegerField, StringField
from wtforms.fields.html5 import DecimalRangeField
from wtforms.validators import DataRequired, NumberRange, InputRequired


class demographicsForm(FlaskForm):
    gender = RadioField(
                        'Gender',
                        choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')],
                        validators=[InputRequired()]
                        )
    age = IntegerField(
                        'Age',
                        validators=[InputRequired(), NumberRange(min=18, max=65, message='You must be between 18 and 65 years old to participate in the study')]
                        )
    nationality = StringField(
                        'Nationality',
                        validators=[InputRequired()]
                        )
    submit = SubmitField(
                        'Next'
                        )


class controlAndDeliberationForm(FlaskForm):
    perceivedControlQ1 = DecimalRangeField(
                        '1. How much control did you feel the consent form gave you over the amount of your personal information collected by the company?',
                        default=50,
                        validators=[InputRequired()]
                        )
    perceivedControlQ2 = DecimalRangeField(
                        '2. How much control did you feel the consent form gave you over who can get access your personal information?',
                        default=50,
                        validators=[DataRequired()]
                        )
    perceivedControlQ3 = DecimalRangeField(
                        '3. How much control did you feel the consent form gave you over your personal information that has been released?',
                        default=50,
                        validators=[DataRequired()]
                        )
    perceivedControlQ4 = DecimalRangeField(
                        '4. How much control did you feel the consent form gave you over how your personal information is being used by the company?',
                        default=50,
                        validators=[DataRequired()]
                        )
    perceivedControlQ5 = DecimalRangeField(
                        '5. Overall, how much did the consent form made you feel in control over your personal information provided to the company?',
                        default=50,
                        validators=[DataRequired()]
                        )
    manipulationCheck = RadioField(
                        '1. Which option did you choose?',
                        choices=[('A', 'Agree'), ('DNA', 'Do Not Agree')],
                        validators=[InputRequired()]
                        )
    deliberation = DecimalRangeField(
                        '2. How much did you think about your decision before clicking on one option?',
                        default=50,
                        validators=[DataRequired()]
                        )
    submit = SubmitField(
                        'Next'
                        )


class privacyConcernsForm(FlaskForm):
    privacyConcernsQ1 = RadioField(
                        '1. Compared to others I’m more sensitive about the way online companies handle my personal information',
                        choices=[('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Somewhat Agree'), ('4', 'Neither Agree nor Disagree'), ('5', 'Somewhat Disagree'), ('6', 'Disagree'), ('7', 'Strongly Disagree')],
                        validators=[InputRequired()]
                        )
    privacyConcernsQ2 = RadioField(
                        '2. To me, it is the most important thing to keep my privacy intact from online companies',
                        choices=[('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Somewhat Agree'), ('4', 'Neither Agree nor Disagree'), ('5', 'Somewhat Disagree'), ('6', 'Disagree'), ('7', 'Strongly Disagree')],
                        validators=[InputRequired()]
                        )
    privacyConcernsQ3 = RadioField(
                        '3. I’m concerned about threats to my personal privacy today',
                        choices=[('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Somewhat Agree'), ('4', 'Neither Agree nor Disagree'), ('5', 'Somewhat Disagree'), ('6', 'Disagree'), ('7', 'Strongly Disagree')],
                        validators=[InputRequired()]
                        )
    submit = SubmitField(
                        'Next'
                        )
