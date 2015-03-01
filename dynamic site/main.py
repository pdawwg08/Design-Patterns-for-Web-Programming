import webapp2

from pages import Page, CreatePage

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = CreatePage()
        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
