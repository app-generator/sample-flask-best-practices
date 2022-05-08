import os
from app import create_app, db

app = create_app(config_name='development')
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    port = os.environ.get("PORT",5000)
    app.run(host='0.0.0.0', port=port, debug=False)
