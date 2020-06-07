from flask import Flask, flash, request, url_for, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'verysecretkey'

class QNABox(FlaskForm):
    question = StringField('What is your question?', validators=[DataRequired()])
    submit = SubmitField('Ask')

@app.route('/qa')
def ask():
    form = QNABox()
    return render_template('textbox.html', title='LALLALA', form=form)



