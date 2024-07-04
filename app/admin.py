from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required

admin = Blueprint('admin', __name__)

@admin.route('/dashboard')
@login_required
def dashboard():
    if not current_user.is_admin:
        return redirect(url_for('views.home'))
    return render_template('admin/admin.html')

@admin.route('/create_product', methods=['GET', 'POST'])
@login_required
def create_product():
    if not current_user.is_admin:
        return redirect(url_for('views.home'))
    # Add product creation logic here
    return render_template('admin/create_product.html')

@admin.route('/upload_products', methods=['GET', 'POST'])
@login_required
def upload_products():
    if not current_user.is_admin:
        return redirect(url_for('views.home'))
    # Add product upload logic here
    return render_template('admin/upload.html')
