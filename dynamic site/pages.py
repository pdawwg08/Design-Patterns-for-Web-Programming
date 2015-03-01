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
    def __init__(self):
        super(CreatePage, self).__init__()
        self.css = "css/style.css"
        self.title = "Welcome"
    def print_out(self):
        all = self._head + self._body + self._close
        all = all.format(**locals())
        return all