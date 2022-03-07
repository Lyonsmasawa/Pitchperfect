from flask import render_template, request, redirect, url_for, abort #takes in the name of a template file as an argument and automatically searches for the template file
#in our app/templates/subdirectory and loads it
from .forms import UpdateProfile
from flask import render_template, request, redirect, url_for
from . import main
from ..models import Review, User
from flask_login import login_required, current_user #will intercept a request and check if user is authenticated and if not the user is directed to the login page
from .. import db, photos
import markdown2

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/what')
def what():
    return render_template('what.html')

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if User is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update', methods = ['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname = user.username))
    return render_template('profile/update.html', form = form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files: #request checks if any file with the name photo has been passed
        filename = photos.save(request.files['photo']) # the save method saves the file in our application
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))