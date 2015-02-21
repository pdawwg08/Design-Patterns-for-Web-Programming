class ComicData(object): #data object
    def __init__(self):
        self.series_title =""
        self.year = 0
        self.month = ""
        self.issue_title = ""
        self.issue_number = 0
class ComicCollection(object):
    def __init__(self):
        self.__comic_list = []
    def add_comic(self,a):
        self.__comic_list.append(a)
    def compile_list(self):
        output = ""
        for com in range (len (self.__comic_list)):
            output += "Issue: " + self.__comic_list[com].issue_title + " (" self.__comic_list[com].month + " " + str(self.__comic_list[com].year) + ")<br />" + self.__comic_list[com].series_title + str(self.__comic_list[com].issue_number)