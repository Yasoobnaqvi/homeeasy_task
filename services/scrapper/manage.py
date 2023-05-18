from flask.cli import FlaskGroup
from sqlalchemy.sql.elements import False_
from project import create_app, db
from project.api.models import *

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()


@cli.command()
def create_db():
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    cli()
    app.run(host='0.0.0.0', debug=True)
