from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
import config  # Import database config
from models import db
from routes import init_routes  # Import route initialization function

# Initialize Flask App
app = Flask(__name__)

# ✅ Properly Configure CORS
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow requests from all domains

# Load Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Register database with Flask app
db.init_app(app)

# Initialize API
api = Api(app)

# Register API Routes
init_routes(api)

# Ensure tables exist
with app.app_context():
    db.create_all()

# Run the App
if __name__ == "__main__":
    app.run(debug=True)