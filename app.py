from flask import Flask, render_template, request, redirect, url_for, make_response


# instantiate the app
app = Flask(__name__)

# Create a list called categories. The elements in the list should be lists that contain the following information in this order:
#   categoryId
#   categoryName
#   An example of a single category list is: [1, "Biographies"]

categories = [
    {"id": 1, "name": "Fantasy"},
    {"id": 2, "name": "Dystopian"},
    {"id": 3, "name": "Romance"},
    {"id": 4, "name": "Mystery"}
]

# Create a list called books. The elements in the list should be lists that contain the following information in this order:
#   bookId     (you can assign the bookId - preferably a number from 1-16)
#   categoryId (this should be one of the categories in the category dictionary)
#   title
#   author
#   isbn
#   price      (the value should be a float)
#   image      (this is the filename of the book image.  If all the images, have the same extension, you can omit the extension)
#   readNow    (This should be either 1 or 0.  For each category, some of the books (but not all) should have this set to 1.
#   An example of a single category list is: [1, 1, "Madonna", "Andrew Morton", "13-9780312287863", 39.99, "madonna.png", 1]

books = [
    {
        "bookId": 1,
        "categoryId": 1,
        "title": "Twilight",
        "author": "Stephenie Meyer",
        "isbn": "13-9780316015844",
        "price": 9.99,
    "image": "fantasy/twilight.png",
        "readNow": 1
    },
    {
        "bookId": 2,
        "categoryId": 1,
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "isbn": "13-9780590353427",
        "price": 7.99,
    "image": "fantasy/harry_potter_sorcerers_stone.png",
        "readNow": 1
    },
    {
        "bookId": 3,
        "categoryId": 1,
        "title": "The Lightning Thief",
        "author": "Rick Riordan",
        "isbn": "13-9780786838653",
        "price": 8.99,
    "image": "fantasy/the_lightning_thief.png",
        "readNow": 0
    },
    {
        "bookId": 4,
        "categoryId": 1,
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "isbn": "13-9780618640157",
        "price": 15.99,
    "image": "fantasy/the_lord_of_the_rings.png",
        "readNow": 1
    },
    {
        "bookId": 5,
        "categoryId": 2,
        "title": "The Hunger Games",
        "author": "Suzanne Collins",
        "isbn": "13-9780439023481",
        "price": 10.99,
    "image": "dystopian/the_hunger_games.png",
        "readNow": 1
    },
    {
        "bookId": 6,
        "categoryId": 2,
        "title": "The Maze Runner",
        "author": "James Dashner",
        "isbn": "13-9780385737951",
        "price": 9.49,
    "image": "dystopian/the_maze_runner.png",
        "readNow": 0
    },
    {
        "bookId": 7,
        "categoryId": 2,
        "title": "Divergent",
        "author": "Veronica Roth",
        "isbn": "13-9780062024039",
        "price": 8.99,
    "image": "dystopian/divergent.png",
        "readNow": 1
    },
    {
        "bookId": 8,
        "categoryId": 2,
        "title": "The Handmaid's Tale",
        "author": "Margaret Atwood",
        "isbn": "13-9780385490818",
        "price": 12.99,
    "image": "dystopian/the_handmaids_tale.png",
        "readNow": 0
    },
    {
        "bookId": 9,
        "categoryId": 3,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "isbn": "13-9781503290563",
        "price": 6.99,
    "image": "romance/pride_and_prejudice.png",
        "readNow": 1
    },
    {
        "bookId": 10,
        "categoryId": 3,
        "title": "The Fault in Our Stars",
        "author": "John Green",
        "isbn": "13-9780142424179",
        "price": 9.99,
    "image": "romance/the_fault_in_our_stars.png",
        "readNow": 1
    },
    {
        "bookId": 11,
        "categoryId": 3,
        "title": "It Ends with Us",
        "author": "Colleen Hoover",
        "isbn": "13-9781501110368",
        "price": 11.99,
    "image": "romance/it_ends_with_us.png",
        "readNow": 0
    },
    {
        "bookId": 12,
        "categoryId": 3,
        "title": "Love Hypothesis",
        "author": "Ali Hazelwood",
        "isbn": "13-9781250812570",
        "price": 14.99,
    "image": "romance/the_love_hypothesis.png",
        "readNow": 1
    },
    {
        "bookId": 13,
        "categoryId": 4,
        "title": "A Good Girl's Guide to Murder",
        "author": "Holly Jackson",
        "isbn": "13-9781984896360",
        "price": 12.99,
    "image": "mystery/a_good_girls_guide_to_murder.png",
        "readNow": 1
    },
    {
        "bookId": 14,
        "categoryId": 4,
        "title": "One of Us Is Lying",
        "author": "Karen M. McManus",
        "isbn": "13-9781524714680",
        "price": 10.99,
    "image": "mystery/one_of_us_is_lying.png",
        "readNow": 0
    },
    {
        "bookId": 15,
        "categoryId": 4,
        "title": "The Silent Patient",
        "author": "Alex Michaelides",
        "isbn": "13-9781250301697",
        "price": 14.99,
    "image": "mystery/the_silent_patient.png",
        "readNow": 1
    },
    {
        "bookId": 16,
        "categoryId": 4,
        "title": "The Housemaid",
        "author": "Freida McFadden",
        "isbn": "13-9781250171671",
        "price": 13.99,
    "image": "mystery/the_housemaid.png",
        "readNow": 0
    }
]

# set up routes
@app.route('/')
def home():
    #Link to the index page.  Pass the categories as a parameter
    return render_template('index.html', categories=categories)

@app.route('/category')
def category():
    # Store the categoryId passed as a URL parameter into a variable
    # get categoryId and convert to int (handle missing/invalid safely)
    try:
        selectedCategory = int(request.args.get('categoryId', 0))
    except (TypeError, ValueError):
        selectedCategory = 0

    # Create a new list called selected_books containing books that have the selected category
    selected_books = [book for book in books if book.get('categoryId') == selectedCategory]

    # Link to the category page.  Pass the selectedCategory, categories and books as parameters
    return render_template('category.html', selectedCategory=selectedCategory, categories=categories, books=selected_books)

@app.route('/search')
def search():
    #Link to the search results page.
    return render_template('search.html', categories=categories, books=books)

@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template('error.html', error=e) # render the edit template


if __name__ == "__main__":
    app.run(debug = True)
