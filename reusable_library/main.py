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
        rp = ResultsPage() #results page instance
        fp = FormPage() #form page instance
        c = ComicData() #comic data instance
        lib = ComicCollection() #comic library
        
        c2 = ComicData() #comic data instance
        c2.series_title = "New Mutants"
        c2.month = "February 1991"
        c2.issue_title = "The Beginning of the End Part One"
        c2.issue_number = 98
        c2.writer = "Rob Liefeld"
        lib.add_comic(c2) #add comic to the library
        
        c3 = ComicData() #comic data instance
        c3.series_title = "The Batman Adventures"
        c3.month = "September 1993"
        c3.issue_title = "Batgirl: Day One"
        c3.issue_number = 12
        c3.writer = "Kelley Puckett"
        lib.add_comic(c3) #add comic to the library
        
        if self.request.GET: #if there is a GET
            c.series_title = self.request.GET['series_title']
            c.month = self.request.GET['month']
            c.issue_title = self.request.GET['issue_title']
            c.issue_number = self.request.GET['issue_number']
            c.writer = self.request.GET['writer']
            lib.add_comic(c)#set variables in the library to equal the GET
            rp.body = lib.compile_list() #the results page will display the compiled list in the body
            self.response.write(rp.print_out_results()) #display the results page
        else:
            fp.body = lib.compile_list() #the form page will display the compiled list in the body
            self.response.write(fp.print_out_form()) #display the form page

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)