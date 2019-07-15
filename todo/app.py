from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    status = db.Column(db.String(100))

class Users(db.Model):
    usernames = db.Column(db.String(100), primary_key=True)
    passwords = db.Column(db.String(100))

@app.route('/')
def login():
    users = Users.query.all()
    #password = Users.query.all()
    return render_template('loginpage.html')

@app.route('/logout')
def logout():
    return render_template('loginpage.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    user = Users(usernames=request.form['userinput'], passwords=request.form['passwordinput'])
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('login'))

@app.route('/auth_user', methods=['POST'])
def auth_user():
    login_user = request.form['userinput']
    login_password = request.form['passwordinput']
    userpassword=db.session.query(Users).filter(Users.usernames==login_user, Users.passwords==login_password).all()
    print db.session.query(Users).all()
    print 'OO',userpassword
    # print len(userpassword)
    if len(userpassword)>0:
        print "User CLEAR"
        return redirect(url_for('index'))
    else:
        print "Not User"
        return render_template('reloginpage.html')

@app.route('/index')
def index():
    incomplete = Todo.query.filter_by(status='incomplete').all()
    complete = Todo.query.filter_by(status='complete').all()
    completing = Todo.query.filter_by(status='completing').all()

    return render_template('index.html', incomplete=incomplete, complete=complete, completing = completing)

@app.route('/add', methods=['POST'])
def add():
    todo = Todo(text=request.form['todoitem'], status='incomplete')
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/complete/<id>')
def complete(id):

    todo = Todo.query.filter_by(id=int(id)).first()
    todo.status = 'complete'
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/completing/<id>')
def completing(id):

    todo = Todo.query.filter_by(id=int(id)).first()
    todo.status = 'completing'
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/delete/<id>', methods=['POST'])
def delete_entry(id):
    #if not db.session.get('logged_in'):
        #abort(401)
    #db = get_db()
    db.session.query(Todo).filter(Todo.id == id).delete()
    #db.session.delete(request.form[todo.id])
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
