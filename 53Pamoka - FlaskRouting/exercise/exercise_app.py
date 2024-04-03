from flask import Flask

app = Flask(__name__)

@app.route('/') #exercise 1
def home():
    return 'Welcome to the Home Page!'

@app.route('/products/<category>') # exercise 1 
def products(category):
    return f'You selected the {category} category.'

user_profiles = {
    'john': ["Reading"],
    'mantas': ["Teaching", "Basketball"]
}

@app.route('/profile/<username>') # exercise 2
def profile(username):
    if username in user_profiles:
        hobbies = ', '.join(user_profiles[username])
        return f'Hello {username}, your hobbies are: {hobbies}.'
    else: 
        return "User not found!"

if __name__ == '__main__':
    app.run(debug=True)
