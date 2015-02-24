class ComicData(object): #data object
    def __init__(self):
        self.series_title =""
        self.month = ""
        self.issue_title = ""
        self.issue_number = 0
        self.writer = ""
class ComicCollection(object):
    def __init__(self):
        self.__comic_list = []
    def add_comic(self,a):
        self.__comic_list.append(a)
        print a.issue_title
    def compile_list(self):
        output = ""
        for comic in self.__comic_list:
            output += "<p>Issue: " + comic.issue_title + " (" + comic.month +")<br />" + comic.series_title + " " + str(comic.issue_number) + ", " + comic.writer + "</p>"
        return output