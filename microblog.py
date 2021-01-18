"""import app package"""
from app import app, db
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    """function to make shell context"""
    return {'db': db, 'User': User, 'Post': Post}
