from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    
	blog_name = "Flask Blog"
    
	owner = "Mohsan and Arslan"
    
	total_posts = 3

	posts =[
		"introdution to flask",
		"Understanign Routes",
		"Learning Jinjia2 Templates"
	]
	
	return render_template(
		"index.html", 
		blog_name = blog_name,
		owner = owner,
		total_posts = total_posts,
        posts = posts
	)

@app.route("/open")
def about_page():
	return render_template(
		"about.html "
	)
 
@app.route("/consss")
def content_page():
	return render_template(
		"contect.html "
	)
 
 
@app.errorhandler(404)
def page_not_found(error):

    return render_template(

        "404.html",

        blog_name="Flask Blog"

    ), 404


@app.route("/error")
def error():
    
    number=10/0
    
    return str(number)


@app.errorhandler(500)
def internal_server_error(error):

    return render_template(

        "500.html",

        blog_name="Flask Blog"

    ), 500
 
@app.route("login")
def login_page():
    
    return render_template(
		"login.html"
	)
    
if __name__ == "__main__":
	app.run(debug=False)

	
	