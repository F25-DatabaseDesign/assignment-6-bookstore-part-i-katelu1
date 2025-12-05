from flask import Flask, render_template, request, redirect, url_for, make_response


# instantiate the app
app = Flask(__name__)

# Create a list called categories. The elements in the list should be lists that contain the following information in this order:
#   categoryId
#   categoryName
#   An example of a single category list is: [1, "Biographies"]

categories = [
    [1, "Fantasy"],
    [2, "Dystopian"],
    [3, "Romance"],
    [4, "Mystery"]
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
    [1, 1, "Twilight", "Stephenie Meyer", "13-9780316015844", 9.99, "twilight.png", 1],
    [2, 1, "Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "13-9780590353427", 7.99, "harry_potter_sorcerers_stone.png", 1],
    [3, 1, "The Lightning Thief", "Rick Riordan", "13-9780786838653", 8.99, "the_lightning_thief.png", 0],
    [4, 1, "The Lord of the Rings", "J.R.R. Tolkien", "13-9780618640157", 15.99, "the_lord_of_the_rings.png", 1],
    [5, 2, "The Hunger Games", "Suzanne Collins", "13-9780439023481", 10.99, "the_hunger_games.png", 1],
    [6, 2, "The Maze Runner", "James Dashner", "13-9780385737951", 9.49, "the_maze_runner.png", 0],
    [7, 2, "Divergent", "Veronica Roth", "13-9780062024039", 8.99, "divergent.png", 1],
    [8, 2, "The Handmaid's Tale", "Margaret Atwood", "13-9780385490818", 12.99, "the_handmaids_tale.png", 0],
    [9, 3, "Pride and Prejudice", "Jane Austen", "13-9781503290563", 6.99, "pride_and_prejudice.png", 1],
    [10, 3, "The Fault in Our Stars", "John Green", "13-9780142424179", 9.99, "the_fault_in_our_stars.png", 1],
    [11, 3, "It Ends with Us", "Colleen Hoover", "13-9781501110368", 11.99, "it_ends_with_us.png", 0],
    [12, 3, "Love Hypothesis", "Ali Hazelwood", "13-9781250812570", 14.99, "the_love_hypothesis.png", 1],
    [13, 4, "A Good Girl's Guide to Murder", "Holly Jackson", "13-9781984896360", 12.99, "a_good_girls_guide_to_murder.png", 1],
    [14, 4, "One of Us Is Lying", "Karen M. McManus", "13-9781524714680", 10.99, "one_of_us_is_lying.png", 0],
    [15, 4, "The Silent Patient", "Alex Michaelides", "13-9781250301697", 14.99, "the_silent_patient.png", 1],
    [16, 4, "The Housemaid", "Freida McFadden", "13-9781250171671", 13.99, "the_housemaid.png", 0]
]

# set up routes
@app.route('/')
def home():
    #Link to the index page.  Pass the categories as a parameter
    return render_template("index.html", categories=categories)

@app.route('/category')
def category():
    # Store the categoryId passed as a URL parameter into a variable
    category_id = request.args.get("categoryId", type=int)

    # Create a new list called selected_books containing a list of books that have the selected category
    selected_books = [b for b in books if b[1] == category_id]

    # Link to the category page.  Pass the selectedCategory, categories and books as parameters
    return render_template(
       "category.html",
       selectedCategory=category_id,
       categories=categories,
       books=selected_books
    )

# we'll link this for project 2 to an sqlite3 database using flask's get_db() function
@app.route('/search')
def search():
    #Link to the search results page.
    return render_template()

@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template('error.html', error=e) # render the edit template


if __name__ == "__main__":
    app.run(debug = True)
