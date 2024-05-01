from flask import Flask, render_template, request, redirect, url_for

books = [
    {"id": 1, "title": "book 1", "author": "author 1", "year": 1999},
    {"id": 2, "title": "book 2", "author": "author 2", "year": 2009},
    {"id": 3, "title": "book 3", "author": "author 3", "year": 2015}
]

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', books=books)


@app.route('/book/<int:book_id>')
def book(book_id):
    book = None
    for i in books:
        if i["id"] == book_id:
            book = i
            break
    return render_template('book.html', book=book)


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        new_book = {
            "id": len(books),
            "title": request.form['title'],
            "author": request.form['author'],
            "year": int(request.form['year'])
        }
        books.append(new_book)
        return redirect(url_for('home'))
    else:
        return render_template('add_book.html')


if __name__ == '__main__':
    app.run(debug=True)
