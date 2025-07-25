import os
import sys

# Add the parent directory to the Python path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from src.models.user import db, bcrypt, User
from src.models.machine import Machine
from src.models.activity import Activity
from src.models.predictive_data import PredictiveData
from src.routes.user import user_bp
from src.routes.auth import auth_bp
from src.routes.machines import machines_bp
from src.routes.activities import activities_bp
from src.routes.analytics import analytics_bp

# Create Flask app
app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))

# Configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'maintai-secret-key-2024')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'maintai-jwt-secret-key-2024')

# Database configuration - Use PostgreSQL for production, SQLite for development
database_url = os.getenv('DATABASE_URL')
if database_url:
    # Production database (PostgreSQL)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
else:
    # Development database (SQLite)
    db_path = os.path.join(os.path.dirname(__file__), 'database', 'app.db')
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Enable CORS for all routes
CORS(app, origins="*", allow_headers=["Content-Type", "Authorization"])

# Initialize extensions
jwt = JWTManager(app)
bcrypt.init_app(app)
db.init_app(app)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(user_bp, url_prefix='/api/users')
app.register_blueprint(machines_bp, url_prefix='/api/machines')
app.register_blueprint(activities_bp, url_prefix='/api/activities')
app.register_blueprint(analytics_bp, url_prefix='/api/analytics')

# Initialize database and create default user
def init_db():
    """Initialize database and create default admin user"""
    try:
        db.create_all()
        
        # Create default admin user if it doesn't exist
        admin_user = User.query.filter_by(username='admin').first()
        if not admin_user:
            admin_user = User(
                username='admin',
                email='admin@maintai.com',
                role='admin'
            )
            admin_user.set_password('password')
            db.session.add(admin_user)
            db.session.commit()
            print("Default admin user created: admin/password")
    except Exception as e:
        print(f"Database initialization error: {e}")

# Initialize database within app context
with app.app_context():
    init_db()

# Static file serving
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_static_files(path):
    """Serve static files and handle SPA routing"""
    static_folder_path = app.static_folder
    if static_folder_path is None:
        return "Static folder not configured", 404

    # If it's an API route, return 404
    if path.startswith('api/'):
        return "API endpoint not found", 404

    # Check if the requested file exists
    if path and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    
    # For SPA routing, serve index.html for all other routes
    index_path = os.path.join(static_folder_path, 'index.html')
    if os.path.exists(index_path):
        return send_from_directory(static_folder_path, 'index.html')
    else:
        return "Application not found", 404

# Health check endpoint
@app.route('/api/health')
def health_check():
    """Health check endpoint for monitoring"""
    return {
        "status": "healthy",
        "message": "MaintAI Backend is running",
        "version": "1.0.0"
    }

# Error handlers
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return {"error": "Resource not found"}, 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return {"error": "Internal server error"}, 500

# For local development
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
