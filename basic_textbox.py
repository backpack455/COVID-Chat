from flask import Flask, flash, request, url_for, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'verysecretkey'

class MessageStore():
    def __init__(self):
        self.data = []
    
    def flash_all(self):
        for i in self.data:
            flash(i)
    
    def reset(self):
        self.data = []


class QNABox(FlaskForm):
    question = StringField('What is your question?', validators=[DataRequired(), Length(min=4)])
    submit = SubmitField('Ask')

def get_answer(question):
    return 'Look it up.'

with app.app_context():
    ms = MessageStore()

@app.route('/qa', methods=['GET', 'POST'])
def ask():
    form = QNABox()
    if form.validate_on_submit():
        if form.question.data.lower() == 'restart':
            ms.reset()
        else:
            ms.data.append('YOU: ' + form.question.data)
            ms.data.append('CHATBOT: ' + get_answer(form.question.data))
    
    ms.flash_all()
    return render_template('textbox.html', title='LALLALA', form=form)

# @app.route('/<question>')
# def answer_question(question):
#     return get_answer(question)



