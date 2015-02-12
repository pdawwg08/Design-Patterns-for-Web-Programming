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
        <title>Simple Form</title>'''
        home_style = '''
        <style>
            body {
                background:#77c4d3;
                font-family: verdana, arial, sans-serif;
                font-weight: 200;
            }
            h1 {
                background: #ea2e49;
                display: inline-block;
                margin-bottom: 1em;
                padding: 0.5em 1em;
                color:#fff;
            }
            h2 {
                font-weight:normal;
                color: #fff;
            }
            form {
                background: rgba(246,247,146,0.9);
                padding: 0.5em 1em;
            }
        </style>
    </head>
    <body>'''
        signed_up_style = '''
        <style>
            body {
                background:#77c4d3;
                font-family: verdana, arial, sans-serif;
                font-weight: 200;
            }
            h1 {
                background: #ea2e49;
                display: inline-block;
                margin-bottom: 1em;
                padding: 0.5em 1em;
                color:#fff;
            }
            h2 {
                font-weight:normal;
                color: #fff;
            }
            p {
                background: rgba(246,247,146,0.9);
                padding: 0.5em 1em;
            }
        </style>
    </head>
    <body>'''
        home_body = '''
        <h1>Sign up form</h1>
        <h2>Sign up here to recieve information relevant to you and your primary interest.</h2>'''
        signed_up_body = '''
        <h1>Thanks for signing up!</h1>
        <h2>Below is the information that you put in the form when you signed up:</h2>'''
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
        </form>'''
        page_close = '''
    </body>
</html>'''
        if self.request.GET:
            user = self.request.GET['user']
            email = self.request.GET['email']
            sex = self.request.GET['sex']
            age = self.request.GET['age']
            interest = self.request.GET['interest']
            self.response.write(page_head + signed_up_style + signed_up_body + '''
            <p>Name: ''' + user + '''</br>
            Email: ''' + email + '''</br>
            Gender: ''' + sex + '''</br>
            Age: ''' + age + '''</br>
            Interest: ''' + interest + '''</p>''' + page_close)
        else:
            self.response.write(page_head + home_style + home_body + page_form + page_close)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
