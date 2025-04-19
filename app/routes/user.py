# app/routes/users.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from app.extensions import db
from app.models import User
from werkzeug.utils import secure_filename
import os

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/')
def list_users():
    users = User.query.all()
    return render_template('users/list.html', users=users, users_json=[user.to_dict() for user in users])


@users_bp.route('/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        text = request.form.get('text')
            
        image_file = request.files.get('image')
        
        filename = None
        if image_file and image_file.filename:
            filename = secure_filename(image_file.filename)
            upload_path = os.path.join(current_app.root_path, 'static', 'uploads')
            os.makedirs(upload_path, exist_ok=True)
            image_file.save(os.path.join(upload_path, filename))

        new_user = User(username=username, email=email, password=password, image=filename, text=text)
        db.session.add(new_user)
        db.session.commit()
        flash('User created successfully!')
        return redirect(url_for('users.list_users'))

    return render_template('users/create.html')

@users_bp.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)

    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        
        # Update password if provided (otherwise keep the current one)
        password = request.form['password']
        if password:
            user.password = password
        
        # Update text/bio if provided
        user.text = request.form['text']
        
        # Handle file upload
        if 'image' in request.files:
            image_file = request.files['image']
            if image_file:
                # Save image
                filename = secure_filename(image_file.filename)
                upload_path = os.path.join(current_app.root_path, 'static', 'uploads')
                image_file.save(os.path.join(upload_path, filename))
                user.image = filename

        db.session.commit()
        flash('User updated successfully!')
        return redirect(url_for('users.list_users'))
    
    return render_template('users/edit.html', user=user)


@users_bp.route('/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted!')
    return redirect(url_for('users.list_users'))
