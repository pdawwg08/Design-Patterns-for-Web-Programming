class ResultsPage(object):
    def __init__(self):
        self.__title ="Welcome"
        self.css ="css/styles.css"
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Enter your information:</title>
        <link href="styles.css" rel="stylesheet" type"text/css" />
    </head>
    <body>
        """
        self.body = ""
        self.__error = ""
        self.__close = """
    </body>
</html>
        """
    def print_out_results(self):
        all = self.__head + self.body + self.__error + self.__close
        return all
    
class FormPage(object):
    def __init__(self):
        self.title ="Welcome"
        self.css ="css/styles.css"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
        <link rel="stylesheet" type="text/css" href="home.css">
    </head>
    <body>
        <h1>Sign up form</h1>
        <h2>Sign up here to recieve information relevant to you and your primary interest.</h2>
        <form method="GET">
            <label>Series Title: </label><input type="text" name="series_title"/></br>
            <label>Issue Number: </label><input type="number" name="issue_number"/></br>
            <label>Issue Title: </label><input type="text" name="issue_title"/></br>
            <label>Month: </label><input type="month" name="month"/></br>
            <input type="submit" value="Submit" />
        </form>
        """
        self.body = ""
        self.error = ""
        self.close = """
    </body>
</html>"""
    def print_out_form(self):
        all = self.head + self.body + self.error + self.close
        return all