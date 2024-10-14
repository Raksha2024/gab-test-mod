# app.py

from flask import Flask, jsonify, send_from_directory
import os
import subprocess

app = Flask(__name__)

# Static information about the application
APP_VERSION = "1.1"
APP_DESCRIPTION = "Simple Health Check Application"

def get_last_commit_sha():
    """Get the last commit SHA from Git."""
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"]
        ).strip().decode('utf-8')
    except Exception as e:
        return str(e)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    """Health check endpoint."""
    last_commit_sha = get_last_commit_sha()
    
    # Construct response
    response = {
        "myapplication": [
            {
                "version": APP_VERSION,
                "description": APP_DESCRIPTION,
                "lastcommitsha": last_commit_sha
            }
        ]
    }
    
    return jsonify(response)

if __name__ == '__main__':
    # Run the application
    port = os.getenv("APP_PORT", 3000)  # Default port 3000
    app.run(host='0.0.0.0', port=port)
