from flask import render_template, request, redirect, flash, url_for
from app import app, db, models
@app.route('/')
@app.route('/index')
def index():
    users = models.User.query.all() # fake user
    return render_template('index.html',
                           title='Welcome')

@app.route('/list')
def list():
    users = models.User.query.all()
    return render_template('list.html',
                           title='List',
                           users=users)

@app.route('/chaperone')
def chaperone():
    users = models.Chap.query.all();
    return render_template('chaperones.html',
                           title='List',
                           users=users)


@app.route('/register', methods=['POST'])
def login():
    error = None
    n=1
    chapText = ""
    if request.method == 'POST':
        while(request.form['name'+str(n)]!=''):
            print(n)
            db.session.add(models.User(name=request.form['name'+str(n)], age = int(request.form['age'+str(n)]), parent = request.form['parent'], lunch = (request.form['lunch']!="false")
            , chaperone = (request.form['chap']!="false"), chapName = request.form['chapn'], notes = request.form['notes'+str(n)]))
            chapText+=request.form['name'+str(n)]+" Age:"+request.form['age'+str(n)]+", "
            n+=1
        db.session.add(models.Chap(name  = request.form['chapn'], parent = request.form['parent'], kids = chapText))
        db.session.commit()
        flash('You registered')
        return redirect(url_for('list'))
    return redirect(url_for('index'))
