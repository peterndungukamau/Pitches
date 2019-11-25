from flask import render_template,url_for,flash,redirect
from pitches import app, db,bcrypt
from pitches.forms import RegistrationForm,LoginForm,PitchForm
from pitches.models import User, Pitch


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
    pitches = Pitch.query.all()
    return render_template('home.html',pitches=pitches)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register',methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
      hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
      user = User(username=form.username.data, email=form.email.data, password=hashed_password)
      db.session.add(user)
      db.session.commit()
      flash('Your account has been created! You are now able to log in', 'success')
      flash(f'Account created successfuly! login', 'success')
      return redirect(url_for('login'))
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

@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('home'))


@app.route('/account')
def account():
  return render_template(url_for('account.html'))


@app.route('/pitch/new',methods=['GET','POST'])
def new_pitch():
  form = PitchForm() 
  if form.validate_on_submit():
    pitch = Pitch(category=form.category.data, content=form.content.data, owner=current_user)
    db.session.add(pitch)
    db.session.commit()
    flash(f'Pitch created successfuly!', 'success')
    return redirect(url_for('home'))
  return render_template('create_pitch.html',form=form)    
  


