from flask import Flask
from flask import render_template

app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rising_water')
def rising_water():
    return render_template('Rising_Water.html')

@app.route('/trash_cleanup')
def trash_cleanup():
    return render_template('trash_cleanup.html')

@app.route('/Internet_on_the_Ocean')
def internet_on_the_ocean():
    return render_template('Internet_on_the_Ocean.html')

if __name__ == '__main__':
  app.run(debug=True, port=5000)  