from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from search_movie import get_list_of_movies, finde_movie_by_id

app = Flask(__name__)
app.config['SECRET_KEY'] = ''
Bootstrap5(app)

# SQLAlchemy database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(app)

# Movie table model
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    
    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Movie {self.title}>'

with app.app_context():
    db.create_all()

# BEGIN: 8d5f9b3d8b3c
class RatingReviewForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")
# END: 8d5f9b3d8b3c

# BEGIN: 7d2f9b3d8b3c
class SearchMovie(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Search")
# END: 7d2f9b3d8b3c

@app.route("/")
def home():
    all_movies = None
    with app.app_context():
        try:
            all_movies = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars()
            return render_template("index.html", movies=all_movies)
        except Exception as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()

@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    form = RatingReviewForm()
    movie_to_update = None
    with app.app_context():
        movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
        if form.validate_on_submit():
            movie_to_update.rating = float(form.rating.data)
            movie_to_update.review = form.review.data
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("edit.html", form=form, movie=movie_to_update)

@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    with app.app_context():
        movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
        db.session.delete(movie_to_delete)
        db.session.commit()
    return redirect(url_for("home"))

@app.route("/add", methods=["GET", "POST"])
def add():
    form = SearchMovie()
    # grab the title of the form and print it to the console
    if form.validate_on_submit():
        movie_title = form.title.data
        movies_data = get_list_of_movies(movie_title)
        return render_template("select.html", movies=movies_data)
    return render_template("add.html", form=form)



@app.route("/find/<int:movie_id>")
def find_and_add(movie_id):
    movie_details = finde_movie_by_id(movie_id)
    # create a new movie object from the form data and add to the database
    new_movie_id = None
    with app.app_context():
        new_movie = Movie(
            title=movie_details['Title'],
            year=movie_details['Year'],
            description=movie_details['Description'],
            rating=float(0),
            ranking=1,
            review="Not reviewed yet.",
            img_url=movie_details['Image URL']
        )
        db.session.add(new_movie)
        new_movie_id = db.session.execute(db.select(Movie).where(Movie.title == movie_details['Title'])).scalar()
        id_num = new_movie_id.id
        db.session.commit()
    return redirect(url_for("edit", movie_id=id_num))
    

if __name__ == '__main__':
    app.run(debug=True)
