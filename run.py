from project.config import config
from project.models import Genre, Movie, Director, User, Favorite
from project.server import create_app, db

app = create_app(config)


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
        "Movie": Movie,
        "Director": Director,
        "User": User,
        "Favorites": Favorite
    }


if __name__ == '__main__':
    app.run(debug=True)

