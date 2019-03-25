from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('pages/index_page.html', title='Главная', active_page='index')


@app.route('/history')
def history():
    return render_template('pages/history_page.html', title='История', active_page='history')


@app.route('/work')
def work():
    return render_template('pages/work_page.html', title='Принципы работы', active_page='work')


@app.route('/services')
def services():
    return render_template('pages/services_page.html', title='Услуги', active_page='services')


@app.route('/sources')
def sources():
    return render_template('pages/sources_page.html', title='Список источникв', active_page='sources')
