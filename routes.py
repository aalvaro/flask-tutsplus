from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask.ext.mail import Message, Mail

mail = Mail()

app = Flask(__name__)

app.secret_key = 'development key'  # Puede ser cualquier cosa (un string)

app.config["MAIL_SERVER"] = "mail.riverdots.com"
app.config["MAIL_PORT"] = 25
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = "pruebas@riverdots.com"
app.config["MAIL_PASSWORD"] = "123456"

mail.init_app(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            msg = Message(form.subject.data,
                          sender=(form.name.data, form.email.data),
                          recipients=['alvarosanchez@riverdots.com',
                                      'pruebas@riverdots.com',
                                      form.email.data])

            msg.body = form.message.data

            mail.send(msg)

            return "Form posted."

    elif request.method == 'GET':
        return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
