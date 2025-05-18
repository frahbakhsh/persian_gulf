from flask import Flask, render_template, jsonify, request, abort, redirect, url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Map, Quote, OrganizationPosition, User
from flask_cors import CORS
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-dev-key-change-in-production')
app.config['JSON_AS_ASCII'] = False
domain = ""
CORS(app)

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# کلاس‌های مدیریت با محدودیت دسترسی
class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))

# تنظیم پنل ادمین
admin = Admin(app, name='پنل مدیریت', template_mode='bootstrap3')
admin.add_view(SecureModelView(Map, db.session, name='نقشه‌ها'))
admin.add_view(SecureModelView(Quote, db.session, name='نقل‌قول‌ها'))
admin.add_view(SecureModelView(OrganizationPosition, db.session, name='مواضع سازمانی'))

# ----- صفحات مدیریت و احراز هویت -----
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect('/admin')
        return render_template('login.html', error='نام کاربری یا رمز عبور اشتباه است')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# ----- صفحات وب -----
@app.route('/')
def index():
    maps = Map.query.all()
    return render_template('home.html', maps=maps)

@app.route('/documentation')
def document():
    base_url = domain
    return render_template('document.html', base_url=base_url)

# ----- API ها -----

@app.route('/api/maps', methods=['GET'])
def get_maps():
    try:
        maps = Map.query.all()
        return jsonify([
            {
                'id': m.id, 
                'title': m.title, 
                'text': m.text,
                'year': m.year, 
                'source': m.source,
                'image_url': m.image_url
            }
            for m in maps
        ])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/maps/<int:map_id>', methods=['GET'])
def get_map(map_id):
    try:
        map_item = Map.query.get(map_id)
        if not map_item:
            return jsonify({'error': 'Map not found'}), 404
            
        return jsonify({
            'id': map_item.id, 
            'title': map_item.title, 
            'text': map_item.text,
            'year': map_item.year, 
            'source': map_item.source,
            'image_url': map_item.image_url
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/quotes', methods=['GET'])
def get_quotes():
    try:
        quotes = Quote.query.all()
        return jsonify([
            {'id': q.id, 'text': q.text, 'source': q.source}
            for q in quotes
        ])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/quotes/<int:quote_id>', methods=['GET'])
def get_quote(quote_id):
    try:
        quote = Quote.query.get(quote_id)
        if not quote:
            return jsonify({'error': 'Quote not found'}), 404
            
        return jsonify({'id': quote.id, 'text': quote.text, 'source': quote.source})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/organizations', methods=['GET'])
def get_organizations():
    try:
        orgs = OrganizationPosition.query.all()
        return jsonify([
            {'id': o.id, 'organization': o.organization, 'position': o.position}
            for o in orgs
        ])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/organizations/<int:org_id>', methods=['GET'])
def get_organization(org_id):
    try:
        org = OrganizationPosition.query.get(org_id)
        if not org:
            return jsonify({'error': 'Organization not found'}), 404
            
        return jsonify({'id': org.id, 'organization': org.organization, 'position': org.position})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ایجاد جداول و کاربر ادمین در صورت نیاز
with app.app_context():
    db.create_all()
    print(1)
    admin_user = User.query.filter_by(username='admin1234').first()
    if not admin_user:
        admin_user = User(
            username='admin',
            password_hash=generate_password_hash('admin1234')
        )
        db.session.add(admin_user)
        db.session.commit()
        print("کاربر ادمین ایجاد شد")
    print(2)
    

if __name__ == '__main__':
    app.run(debug=True)