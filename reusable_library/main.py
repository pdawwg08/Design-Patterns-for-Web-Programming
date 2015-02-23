'''
Preston Cain
2/19/15
reusable library
'''
import webapp2
from library import ComicData, ComicCollection
from pages import ResultsPage, FormPage

class MainHandler(webapp2.RequestHandler):
    def get(self):
        rp = ResultsPage()
        fp = FormPage()
        c = ComicData()
        lib = ComicCollection()
        if self.request.GET: #if there is a GET
            c.series_title = self.request.GET['series_title']
            c.month = self.request.GET['month']
            c.issue_title = self.request.GET['issue_title']
            c.issue_number = self.request.GET['issue_number']
            c.artist = self.request.GET['artist']
            lib.add_comic(c)#set variables to equal the GET
            rp.body = lib.compile_list()
            self.response.write(rp.print_out_results()) #write the GET information to page
        else:
            self.response.write(fp.print_out_form()) #write home page with form

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)