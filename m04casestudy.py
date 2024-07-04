from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)



app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integar, primary_key=True)
    book_name = db.Column(db.String(25))
    author = db.Column(db.String(30))
    publisher = db.Column(db.String(30))

    def __repr__(self):
        return f"{self.book_name} - {self.author}"

@app.route('/')
def index():
    return 'Hello!'


    @app.route('/book')
    def get_book();
        book = book.query.all()

        output = []
        for book in book:
            book_data = {'book_name':book.name, 'author': book.author, 'publisher':book.publisher}

            output.append(book_data)

        return {"book": output}

@app.route('/book/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return ({"book_name": book.name, "author": book.author, "publisher": book.publisher})

    @app.route('/book', methods=['POST'])
    def add_book():
        book = book(book_name=request.json['book_name'], author=request.json['author'], publisher=request.json['publisher])
        db.session.add(book)
        db.session.commit()
        return {'id': book.id}

@app.route('/book/<id>', methods=['DELETE"])
    def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"}
    db.session.delete(book)
    de.session.commit()
    return {"message":"yeet!"}