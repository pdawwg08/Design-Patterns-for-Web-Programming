'''
Preston Cain
2/19/15
reusable library
'''
import webapp2
from library import ComicData
from pages import ResultsPage, FormPage

class MainHandler(webapp2.RequestHandler):
    def get(self):
        r = ResultsPage()
        f = FormPage()
        c = ComicData()
        if self.request.GET: #if there is a GET
            c.series_title = self.request.GET['series_title']
            c.year = self.request.GET['year']
            c.month = self.request.GET['month']
            c.issue_title = self.request.GET['issue_title']
            c.issue_number = self.request.GET['issue_number'] #set variables to equal the GET
            self.response.write(r.print_out) #write the GET information to page
        else:
            self.response.write(f.print_out) #write home page with form

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)