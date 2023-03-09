from flask import Flask, render_template,request,redirect

app = Flask(__name__)

# Define routes for our e-commerce application
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/products')
def products():
    # Get all the products from our database (or wherever they are stored)
    products = [
        {'id': 1, 'name': 'Product 1', 'description': 'Description 1', 'price': 10},
        {'id': 2, 'name': 'Product 2', 'description': 'Description 2', 'price': 20},
        {'id': 3, 'name': 'Product 3', 'description': 'Description 3', 'price': 30},
    ]
    return render_template('products.html', products=products)

@app.route('/product/<int:id>')
def product(id):
    # Get the product with the given ID from our database (or wherever it is stored)
    product = {'id': id, 'name': 'Product {}'.format(id), 'description': 'Description {}'.format(id), 'price': 10*id}
    return render_template('product.html', product=product)

@app.route('/cart')
def cart():
    # Get the current user's cart items and total from our database (or wherever they are stored)
    cart_items = [
        {'product': {'id': 1, 'name': 'Product 1', 'description': 'Description 1', 'price': 10}, 'quantity': 2},
        {'product': {'id': 3, 'name': 'Product 3', 'description': 'Description 3', 'price': 30}, 'quantity': 1},
    ]
    total = sum(item['product']['price']*item['quantity'] for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total=total)
@app.route('/add-product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        # Get the form data from the request
        name = request.form['name']
        description = request.form['description']
        price = float(request.form['price'])

        # Create a new product object
        new_product = {
            'name': name,
            'description': description,
            'price': price
        }

        # Add the new product to the list of products
        products.append(new_product)

        # Redirect the user back to the home page
        return redirect('/')
    else:
        return render_template('add_product.html')
if __name__ == '__main__':
    app.run(debug=True)
