from flask import render_template, request, redirect, flash, url_for
from app import app, db, models, mail
from flask_mail import Message

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
            print(request.form['name'+str(n)])
            if(models.User.query.filter(models.User.name == request.form['name'+str(n)], models.User.parent == request.form['parent']).count()==0):
                UserList.append(models.User(name=request.form['name'+str(n)], age = int(request.form['age'+str(n)]), parent = request.form['parent'], parent_email = request.form['parent_email'], lunch = (request.form['lunch']!="false")
                , chaperone = (request.form['chap']!="false"), chapName = request.form['chapn'], notes = request.form['notes'+str(n)]))
                db.session.add(UserList[n-1])
                chapText+=request.form['name'+str(n)]+" Age:"+request.form['age'+str(n)]+", "
            else:
                return 'Error, '+request.form['name'+str(n)]+' is already registered.  Please email Shivam at smevawala@lgsinnovations.com for assistance'
            n+=1
        if(request.form['chap']!="false"):
            if(models.Chap.query.filter(models.Chap.name == request.form['chapn'], models.Chap.parent == request.form['parent']).count()==0):
                chap= models.Chap(name  = request.form['chapn'], parent = request.form['parent'], parent_email = request.form['parent_email'], kids = chapText)
                db.session.add(chap)
                chapList.append(chap)
            else:
                return 'Error, '+request.form['chapn']+' is already registered as a chaperone.  Please email Shivam at smevawala@lgsinnovations.com for assistance'

        db.session.commit()
        flash('You registered')
        msg=Message("Thanks for registering for LGS's Bring Your Child to Work Day!", sender="smevawala@lgsinnovations.com", recipients=[UserList[0].parent_email])
        #mail.send(msg)
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
        if(models.Chap.query.filter(models.Chap.name == request.form['chapn'], models.Chap.parent == request.form['chapn']).count()==0):
            print("got here")
            chap= models.Chap(name  = request.form['chapn'], parent = request.form['chapn'], parent_email = "" ,kids = '')
            db.session.add(chap)
            chapList.append(chap)
            db.session.commit()
            flash('You registered')
            return render_template('thanks.html',
                                   title='Thank You For Registering',
                                   users=UserList, chaps=chapList)
        else:
            print("got here else")
            return 'Error, '+request.form['chapn']+' is already registered as a chaperone.  Please email Shivam at smevawala@lgsinnovations.com for assistance'
    return redirect(url_for('index'))
