from data import PageData

class Page(object):
    def __init__(self):
        self._head = """
<!doctype html>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css">
    </head>
    <body>""" #basic html opening
        
        self._body = "" #empty body
        self._close = """
    </body>
</html>""" # basic closing
        
    def print_out(self):
        return self._head + self._body + self._close #simple print out
class CreatePage(Page):
    def __init__(self,title): #use passed in value of title
        super(CreatePage, self).__init__()
        self.title = title #use passed in title value from GET
        d = PageData() #create instance
        if self.title == "Welcome": #test which page to go to
            self._body = d.header + d.home #combine the header and the appropriate page
        elif self.title == "Results":
            self._body = d.header + d.results
        elif self.title == "Details":
            self._body = d.header + d.details
        elif self.title == "Favorites":
            self._body = d.header + d.favorites
        elif self.title == "Login":
            self._body = d.header + d.login
        elif self.title == "Sign Up":
            self._body = d.header + d.signup
        else:
            print "Title Error" #if nothing matches something went wrong in the title
        
        self.css = "css/style.css" #css for the page

    def print_out(self):
        all = self._head + self._body + self._close
        all = all.format(**locals()) #fill in title and css
        return all