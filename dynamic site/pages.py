class Page(object):
    def __init__(self):
        self._head = """
<!doctype html>
<html>
    <head>
        <title>{self.title}</title>
        <link href="css/style.css" rel="stylesheet" type="text/css">
    </head>
    <body>"""
        
        self._body = ""
        self._close = """
    </body>
</html>"""
        
    def print_out(self):
        return self._head + self._body + self._close
class FormPage(Page):
    def __init__(self):
        super(FormPage, self).__init__()
        self._form_open = '<form method="GET">'
        self._form_close = "</form>"
        self.__inputs = []
        self._form_inputs = ""
    @property
    def inputs(self):
        pass
    @inputs.setter
    def inputs(self, arr):
        self.__inputs = arr
        for item in arr:
            self._form_inputs += '<input type="' + item[1] +'" name ="' + item[0]
            try:
                self._form_inputs += '"placeholder="' + item[2] +'" />'
            except:
                self._form_inputs += '" />'
    def print_out(self):
        return self._head + self._body + self._form_open + self._form_inputs + self._form_close + self._close