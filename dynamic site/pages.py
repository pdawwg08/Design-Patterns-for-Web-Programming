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
    <body>"""
        
        self._body = ""
        self._close = """
    </body>
</html>"""
        
    def print_out(self):
        return self._head + self._body + self._close
class CreatePage(Page):
    def __init__(self,title):
        super(CreatePage, self).__init__()
        self.title = title
        d = PageData()
        if self.title == "Welcome":
            self._body = d.header + d.home
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
            print "Title Error"
        
        self.css = "css/style.css"

    def print_out(self):
        all = self._head + self._body + self._close
        all = all.format(**locals())
        return all