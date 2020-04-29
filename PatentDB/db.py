from flask import Flask, render_template, request,redirect,url_for,flash
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'siddharth18'
app.config['MYSQL_DB'] = 'patentdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
app.secret_key='yippi k yay'

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		details = request.form
		firstName = details['username']
		password = details['password']
		cur = mysql.connection.cursor()
		cur.execute('''SELECT * FROM users WHERE Username=(%s) AND Password=(%s)''',(firstName,password))
		result=cur.fetchone()
		print(result)
		if result==None:
			flash(" Try Again!")
			return render_template('index.html')
		else:
			role=result['designation']
			if role=="Attorney":
				return redirect(url_for('dashAtt'))
			elif role=="Applicant":
				return redirect(url_for('dashApp'))
			elif role=="Patentee":
				return redirect(url_for('dashPat'))
			elif role=="Examiner":
				return redirect(url_for('dashExa'))
		mysql.connection.commit()
		cur.close()
		return render_template('index.html')
	return render_template('index.html')

@app.route('/dash_applicant',methods=['GET','POST'])
def dashApp():
		return render_template('dash_applicant.html')

@app.route('/dash_attorney',methods=['GET','POST'])
def dashAtt():
		return render_template('dash_attorney.html')

@app.route('/dash_examiner',methods=['GET','POST'])
def dashExa():
		return render_template('dash_examiner.html')

@app.route('/dash_patentee',methods=['GET','POST'])
def dashPat():
		return render_template('dash_patentee.html')


if __name__ == '__main__':
	app.run()