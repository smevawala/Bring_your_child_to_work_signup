from flask import render_template, request, redirect, flash, url_for
from app import app, db, models
@app.route('/')
@app.route('/index')
def index():
    users = models.User.query.all() # fake user
    return render_template('index.html',
                           title='Welcome',
                           users=users)

@app.route('/list')
def list():
    users = models.User.query.all() # fake user
    return render_template('list.html',
                           title='List',
                           users=users)


@app.route('/register', methods=['POST'])
def login():
    error = None
    n=1
    if request.method == 'POST':
        while(request.form['name'+str(n)]!=''):
            print(n)
            db.session.add(models.User(name=request.form['name'+str(n)], age = int(request.form['age'+str(n)]), parent = request.form['parent'], lunch = (request.form['lunch']!="false")
            , chaperone = (request.form['chap']!="false"), chapName = request.form['chapn'], notes = request.form['notes']))
            n+=1
        db.session.commit()
        flash('You registered')
        return redirect(url_for('list'))
    return redirect(url_for('index'))
