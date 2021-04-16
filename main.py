from flask import Flask, render_template
from scrapers import RT
app = Flask(__name__)

data = {
    'name': 'Dima',
    'last': 'Kapitan'
}

names = ['Lauren', 'Dima', 'Laurima']

rt_data = RT.get_front_page()

@app.route('/sup')
def main():
    return render_template('main.html', h_names=names, h_rt=rt_data)

if __name__ == '__main__':
    app.run(host='192.168.1.248', port=80)
    