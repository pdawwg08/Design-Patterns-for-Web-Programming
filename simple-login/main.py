'''
Preston Cain
2/12/15
Simple Form
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page_head = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>''' #basic head
        home_style = '''
        <link rel="stylesheet" type="text/css" href="home.css">
    </head>
    <body>''' #link to home.css
        signed_up_style = '''
        <link rel="stylesheet" type="text/css" href="signed_up.css">
    </head>
    <body>''' #link to signed_up.css
        home_body = '''
        <h1>Sign up form</h1>
        <h2>Sign up here to recieve information relevant to you and your primary interest.</h2>'''#home page body
        signed_up_body = '''
        <h1>Thanks for signing up!</h1>
        <h2>Below is the information that you put in the form when you signed up:</h2>''' #signed up page body
        page_form = '''
        <form method="GET">
            <label>Name: </label><input type="text" name="user"/></br>
            <label>Email: </label><input type="email" name="email"/></br>
            <label>Male </label><input type="radio" value="Male" name="sex"/></br>
            <label>Female </label><input type="radio" value="Female" name="sex"/></br>
            <label>Age: </label><input type="number" name="age"/></br>
            <label>Interest: </label><select name="interest">
                <option value="sports">Sports</option>
                <option value="movies">Movies</option>
                <option value="music">Music</option>
            </select></br>
            <input type="submit" value="Submit" />
        </form>''' #simple form
        page_close = '''
    </body>
</html>''' #close html
        if self.request.GET: #if there is a GET
            user = self.request.GET['user']
            email = self.request.GET['email']
            sex = self.request.GET['sex']
            age = self.request.GET['age']
            interest = self.request.GET['interest'] #set variables to equal the GET
            self.response.write(page_head + signed_up_style + signed_up_body + '''
            <p>Name: ''' + user + '''</br>
            Email: ''' + email + '''</br>
            Gender: ''' + sex + '''</br>
            Age: ''' + age + '''</br>
            Interest: ''' + interest + '''</p>''' + page_close) #write the GET information to page
        else:
            self.response.write(page_head + home_style + home_body + page_form + page_close) #write home page with form

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)