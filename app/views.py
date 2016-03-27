from flask import render_template, request, redirect, flash, url_for
from app import app, db, models
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Welcome')

@app.route('/chapOnly')
def cFom():
    return render_template('conly.html',
                           title='Welcome')

@app.route('/list')
def list():
    users = models.User.query.all()
    return render_template('list.html',
                           title='List',
                           users=users)

@app.route('/chaplist')
def chaplist():
    users = models.Chap.query.all();
    return render_template('chaperones.html',
                           title='List',
                           users=users)


@app.route('/register', methods=['POST'])
def login():
    error = None
    n=1
    chapText = ""
    UserList=[]
    chapList=[]
    if request.method == 'POST':
        while(request.form['name'+str(n)]!=''):
            print(n)
            UserList.append(models.User(name=request.form['name'+str(n)], age = int(request.form['age'+str(n)]), parent = request.form['parent'], lunch = (request.form['lunch']!="false")
            , chaperone = (request.form['chap']!="false"), chapName = request.form['chapn'], notes = request.form['notes'+str(n)]))
            db.session.add(UserList[n-1])
            chapText+=request.form['name'+str(n)]+" Age:"+request.form['age'+str(n)]+", "
            n+=1
        if(request.form['chap']!="false"):
            chap= models.Chap(name  = request.form['chapn'], parent = request.form['parent'], kids = chapText)
            db.session.add(chap)
            chapList.append(chap)
        db.session.commit()
        flash('You registered')
        return render_template('thanks.html',
                               title='Thank You For Registering',
                               users=UserList, chaps=chapList)
    return redirect(url_for('index'))

@app.route('/registerC', methods=['POST'])
def regC():
    error = None
    UserList=[]
    chapList=[]
    if request.method == 'POST':
        chap= models.Chap(name  = request.form['chapn'], parent = request.form['chapn'], kids = '')
        db.session.add(chap)
        chapList.append(chap)
        db.session.commit()
        flash('You registered')
        return render_template('thanks.html',
                               title='Thank You For Registering',
                               users=UserList, chaps=chapList)
    return redirect(url_for('index'))
