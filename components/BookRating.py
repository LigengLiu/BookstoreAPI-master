from __main__ import db, ma, app

# product Class/model
class Rating(db.Model):
    # Rating Schema
    class ProductSchema(ma.Schema):
        class Meta:
            fields = ( 'name', 'rate', 'comment', 'book', 'time')

    # Create DB fields
    Book = db.Column(db.String)
    Name = db.Column(db.String)
    Rate = db.Column(db.Integer)
    Comment = db.Column(db.String)
    Time = db.Column(db.String)

# Product schema for single and multiple items
product_schema = ProductSchema()
products_schema = productSchema(many=True)

def __init__(self, Book, Name, Rate, Comment):
    self.Book = Book
    self.Name = Name
    self.Rate = Rate
    self.Comment = Comment
    self.Time = time.asctime






