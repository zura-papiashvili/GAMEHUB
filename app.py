from myproject import app,Post
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    posts = Post.query.all()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)