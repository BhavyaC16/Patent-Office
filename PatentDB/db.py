from flask import Flask, render_template, request,redirect,url_for
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'siddharth18'
app.config['MYSQL_DB'] = 'patentdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		details = request.form
		firstName = details['username']
		lastName = details['password']
		cur = mysql.connection.cursor()
		# cur.execute("SELECT Password FROM users WHERE Username=(%s)",(firstName))
		# result=cur.fetchone()
		# if result[0]['Password']==NULL:
		# 	print("hello")
		# elif result[0]['Password']==lastName:
		# 	print("wow")
		mysql.connection.commit()
		cur.close()

		return redirect(url_for('dashA'))
	return render_template('index.html')

@app.route('/dash_applicant',methods=['GET','POST'])
def dashA():
		return render_template('dash_applicant.html')


if __name__ == '__main__':
	app.run()