class ResultsPage(object):
    def __init__(self):
        self.title ="Welcome"
        self.css ="css/style.css"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link rel="stylesheet" type="text/css" href="{self.css}">
    </head>
    <body>
    <h1>My comics list:</h1>
        """
        self.body = ""
        self.error = ""
        self.close = """
    </body>
</html>
        """
    def print_out_results(self):
        all = self.head + self.body + self.error + self.close
        all = all.format(**locals())
        return all
    
class FormPage(object):
    def __init__(self):
        self.title ="Welcome"
        self.css ="css/style.css"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link rel="stylesheet" type="text/css" href="{self.css}">
        <script src="js/form.js"></script>
    </head>
    <body>
        <h1>Add Comics</h1>
        <h2>Input the information of each comic you have in your collection:</h2>
        <form method="GET" onsubmit="return formValidate(this);">
            <label>Series Title: </label><input type="text" name="series_title"/></br>
            <label>Issue Number: </label><input type="number" name="issue_number"/></br>
            <label>Issue Title: </label><input type="text" name="issue_title"/></br>
            <label>Month: </label><input type="month" name="month"/></br>
            <label>Writer: </label><input type="text" name="writer"/></br>
            <input type="submit" value="Submit" />
        </form>
        <h2>My comics list:</h2>
        """
        self.body = ""
        self.error = ""
        self.close = """
    </body>
</html>"""
    def print_out_form(self):
        all = self.head + self.body + self.error + self.close
        all = all.format(**locals())
        return all