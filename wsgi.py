from werkzeug.security import generate_password_hash

from blog.app import create_app, db

app = create_app()


@app.cli.command('init-db')
def init_db():
    """
    Run in your terminal:
    flask init-db
    """
    db.create_all()


@app.cli.command('create-users')
def create_users():
    """
    Run in your terminal:
    flask create-users
    > done! created users: <User #1 'admin'> <User #2 'james'>
    """
    from blog.models import User

    db.session.add(
        User(email='name@email.com', password=generate_password_hash('test123'))
    )
    db.session.commit()
