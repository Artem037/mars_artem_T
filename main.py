from flask import render_template
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    profs = ['инженер-исследователь',
             'пилот',
             'строитель',
             'экзобиолог',
             'врач',
             'инженер по терраформированию',
             'климатолог',
             'специалист по радиационной защите',
             'астрогеолог',
             'гляциолог',
             'инженер жизнеобеспечения',
             'метеоролог',
             'оператор марсохода',
             'киберинженер',
             'штурман',
             'пилот дронов']
    if list == 'ol':
        profs = enumerate(profs, start=1)
    return render_template('list_prof.html', list=list, profs=profs)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
