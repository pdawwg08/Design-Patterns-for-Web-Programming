import webapp2

from pages import Page, CreatePage

class MainHandler(webapp2.RequestHandler):
    def get(self):
        if self.request.GET:
            title = self.request.GET['title']
        else:
            title = "Welcome"
        
        p = CreatePage(title)
            
        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
