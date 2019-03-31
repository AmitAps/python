#Add "render_template" to the list of technologies imported from the "flask" module.
from flask import Flask, render_template, request, redirect
#You need to import the "search4letters" function from the "vlsearch" module before you call it.
from vlsearch import search4letters

app = Flask(__name__)

@app.route('/')
#Adjust the annotation to more clearly indicate what's beingg returned by this function. Recall that HTTP
#status codes in the 300-399 range are redirections, and 302 is what Flask sends back to your browser when "redirect" is invoked.

def hello() -> '302':
    #Call Flask's "redirecct" function to instruct the browser to request an alternative URL (in this case, "/entry")
    return redirect('/entry')

#A second decorator sets op the "/search" URL

@app.route('/search4', methods=['POST'])
#The "do_search" function invokes "search4letters", then returns any results as a string.
def do_search() -> 'html': #Change the annotation to indicate that this function now returns HTML, not a plain-text string.
    #Create two new variables and assign the HTML form's data to the newly created variables.
    phrase = request.form['phrase']
    letters = request.form['letters']
    #Create a Python variable called "title" and assigned a string to "title".
    title = 'Here are your results:'
    #Create another Python variable called "results" and assign the results of the call to "search4letters tp "results".
    results = str(search4letters(phrase, letters))
    #Then use the variables in the call to "search4letters".
    #Each of Python variable is assigned to its corresponding Jinja2 argument . In this way, data from our program code is passed into the template.
    #This extra comma looks a little strange , but is perfectly fine(though optional) Python syntax.
    return render_template('results.html', the_phrase=phrase, the_letters=letters, the_title=title, the_results=results,)

#Underneath the "do_search" function, but before the "app.run()" line, insert this line to add a ne URL to the webapp.
@app.route('/entry')
#Add this function directly underneath the new "@app.route" line.
#Provide the name of the template to render.
#Provide a value to asssociate with the "the_title" argument.
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


app.run(debug=True)