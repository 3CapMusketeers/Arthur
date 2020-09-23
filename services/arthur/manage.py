from flask.cli import FlaskGroup

from project import create_app, db
from project.app.models import User, Playlist, AdminUser


app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command('seed_db')
def seed_db():
    """Seeds the database."""

    # Sample
    # db.session.add(Users(
    #     id=3,
    #     display_name = 'testuser'
    # ))

    db.session.commit()


if __name__ == '__main__':
    cli()