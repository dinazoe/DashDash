from flask import Flask, render_template
from scrapers import RT
app = Flask(__name__)


rt_data = RT.get_front_page()

@app.route('/movies')
def main():
    return render_template('movies.html', h_rt=rt_data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    