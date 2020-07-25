from flask import Flask
from flask import render_template

# archivo principal
app = Flask(__name__)

# creamos las rutas
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# activamos el servidor
if __name__ == '__main__':
    app.run(debug=True,port=3000)