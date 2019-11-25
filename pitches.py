# from datetime import datetime
from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm
# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '6f6c7e8e596878241f2d4a1237ede20f'
# app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# db = SQLAlchemy(app)


# class User(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   username = db.Column(db.string(15), unique=True, nullable=False)
#   email = db.Column(db.string(100), unique=True, nullable=False)
#   image_file = db.Column(db.string(15), nullable=False, default='default.jpg')
#   password = db.Column(db.string(60), nullable=False)
#   pitches = db.relationship('Pitch', backref='owner', lazy=True)

#   def __repr__(self):
#     return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    

# class Pitch(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   category = db.Column(db.String(100), nullable=False)
#   date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
#   content = db.Column(db.Text, nullable=False)
#   user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


#   def __repr__(self):
#     return f"Pitch('{self.category}', '{self.date}')"




pitches = [
    {
        'category':'Pickup Lines',
        'content':'I think you are an angel cause you look like have fallen from the sky',
        'owner':'Peter Kamau',
        'date':'2nd April 1905'
        
    },

      {
        'category':'Interview Pitch',
        'content':'I think you are an angel cause you look like have fallen from the sky',
        'owner':'Peter Kamau',
        'date':'2nd April 1905'
        
    },

      {
        'category':'Product Pitch',
        'content':'I think you are an angel cause you look like have fallen from the sky',
        'owner':'Peter Kamau',
        'date':'2nd April 1905'
        
    },

      {
        'category':'Promotion Pitch',
        'content':'I think you are an angel cause you look like have fallen from the sky',
        'owner':'Peter Kamau',
        'date':'2nd April 1905'
        
    },

      {
        'category':'Other',
        'content':'I think you are an angel cause you look like have fallen from the sky',
        'owner':'Peter Kamau',
        'date':'2nd April 1905'
        
    },
]


@app.route('/')
@app.route('/home')
def home():
    
    return render_template('home.html',pitches=pitches)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register',methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    flash(f'Account created successfuly for {form.username.data}!', 'success')
    return redirect(url_for('home'))
  return render_template('register.html',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
      if form.email.data == 'pet@gmail.com' and form.password.data == 'password':
        flash(f'Login successfuly ', 'success')
        return redirect(url_for('home'))
      else:
          flash(f'Login unsuccessful. Please Check username and password ', 'danger') 
  return render_template('login.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)    
