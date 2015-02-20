'''
Preston Cain
2/19/15
reusable library
'''
import webapp2
from library import ComicData

class MainHandler(webapp2.RequestHandler):
    def get(self):
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