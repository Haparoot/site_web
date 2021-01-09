from flask import Flask , render_template , escape
app = Flask(__name__)
print(__name__)

@app.route('/<username>/<post_id>')
def hello_world(username = None , post_id = None):
	# return render_template('index.html' , name = username , post_id = post_id )
	return 'User %s ' % escape(username)

@app.route('/blog')
def blog():
	return 'these are my blog'

@app.route('/blog/2020/rain')
def blog2():
	return 'shor shor barooon'