import webapp2

from pages import Page, CreatePage

class MainHandler(webapp2.RequestHandler):
    def get(self):
        if self.request.GET: #if there is a get
            title = self.request.GET['title']
        else:
            title = "Welcome" #if not use the home page title
        
        p = CreatePage(title) #pass in the value of the title
            
        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
