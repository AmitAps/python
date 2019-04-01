#Add "render_template" to the list of technologies imported from the "flask" module.
from flask import Flask, render_template, request, redirect, escape
#You need to import the "search4letters" function from the "vlsearch" module before you call it.
from vlsearch import search4letters

app = Flask(__name__)

@app.route('/')
#Adjust the annotation to more clearly indicate what's beingg returned by this function. Recall that HTTP
#status codes in the 300-399 range are redirections, and 302 is what Flask sends back to your browser when "redirect" is invoked.

def hello() -> '302':
    #Call Flask's "redirecct" function to instruct the browser to request an alternative URL (in this case, "/entry")
    return redirect('/entry')

#This annotation may have thrown you a little. Recall that function annotations are meant to be read by oter programmers.
#They are documentation, not excutable code: the Python interpreter always ignores them, so you can use any annotation descriptor you like.
def log_request(req: 'flask_request', res: str) -> None: #This annotation uses Python's "None" value to indicate this function has no return value.
    #Note the file stream is called "log" in this code.
    #Use "with" to open "vlsearch.log" in append mode.
    with open('vlsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


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
    #Call the "log_request" function here.
    log_request(request, results)

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

#We have a brand new URL.
@app.route('/viewlog')
#And we have a brand new function, which (according to the annotation) returns a html now.
def view_the_log() -> 'html':
    #Create a new, empty list called "contents".
    contents = []
    #Open the log file for reading.
    with open('vlsearch.log') as log:
        #Loop through each line in the "log" file stream.
        for line in log:
            #Append a new, empty list to "contents".
            contents.append([])
            #Split the line (based on the vertical bar), then process each item in the resulting "split list".
            for item in line.split('|'):
                #Append the escape data to the end of list at the end of "contents".
                #Did you rember to call "escape"?
                contents[-1].append(escape(item))
    #Create a tuple of descriptive titles.
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    #Call "render_template", providing values for each of the templates's arguments.
    return render_template('viewlog.html',
                            the_title='View Log',
                            the_row_title=titles,
                            the_data=contents,)



#req.form: The data posted from the webapp’s HTML form.
#req.remote_addr: The IP address the web browser is running on.
#req.user_agent: The identity of the browser posting the data.


app.run(debug=True)


