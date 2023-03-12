# from werkzeug.security import generate_password_hash

from blog.app import app
from blog.models.database import db


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
    )


# @app.cli.command("create-users")
# def create_users():
#     """
#     Run in your terminal:
#     flask create-users
#     > done! created users: <User #1 'admin'> <User #2 'james'>
#     """
#     from blog.models import User
#     admin = User(username="admin", is_staff=True, email='admin@email.com', password=generate_password_hash('test123'))
#     james = User(username="james", email='james@email.com', password=generate_password_hash('test456'))
#     db.session.add(admin)
#     db.session.add(james)
#     db.session.commit()
#     print("done! created users:", admin, james)

@app.cli.command("create-tags")
def create_tags():
    """
    Run in your terminal:
    flask create-tags
    > done! created tags: <flask> <django> <python> <gb> <sqlite>
    """
    from blog.models import Tag

    tags = ('flask', 'django', 'python', 'gb', 'sqlite')
    for item in tags:
        db.session.add(Tag(name=item))
    db.session.commit()
    print(f"done! created tags: {', '.join(tags)}")
