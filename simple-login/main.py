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
        <title>Simple Form</title>
    </head>
    <body>'''
        page_form = '''<form method="GET">
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
            <input type="submit" value="Submit" />'''
        page_close = '''
        </form>
    </body>
</html>'''
        if self.request.GET:
            user = self.request.GET['user']
            email = self.request.GET['email']
            sex = self.request.GET['sex']
            age = self.request.GET['age']
            interest = self.request.GET['interest']
            self.response.write(page_head + '''
            <p>Name: ''' + user + '''</p>
            <p>Email: ''' + email + '''</p>
            <p>Gender: ''' + sex + '''</p>
            <p>Age: ''' + age + '''</p>
            <p>Interest: ''' + interest + '''</p>''' + page_close)
        else:
            self.response.write(page_head + page_form + page_close)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
