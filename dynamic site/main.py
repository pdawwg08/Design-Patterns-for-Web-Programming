import webapp2

from pages import Page, CreatePage

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = CreatePage()
        p.inputs = [["first_name","text","First Name"],["last_name","text","Last Name"],["Submit","submit"]]
        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
