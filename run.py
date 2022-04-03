from app import app
from app.models import db, User

#shell context processor
@app.shell_context_processor
def shell_context():
    return {'db': db, 'User': User}