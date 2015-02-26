class ComicData(object): #data object
    def __init__(self):
        self.__series_title =""
        self.__month = ""
        self.__issue_title = ""
        self.__issue_number = 0
        self.__writer = ""
        
    @property
    def series_title(self):
        return self.__series_title
    @series_title.setter
    def series_title(self, y):
        self.__series_title = y
        
    @property
    def month(self):
        return self.__month
    @month.setter
    def month(self, y):
        self.__month = y

    @property
    def issue_title(self):
        return self.__issue_title
    @issue_title.setter
    def issue_title(self, y):
        self.__issue_title = y

    @property
    def issue_number(self):
        return self.__issue_number
    @issue_number.setter
    def issue_number(self, y):
        self.__issue_number = y

    @property
    def writer(self):
        return self.__writer
    @writer.setter
    def writer(self, y):
        self.__writer = y
        
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
    def average_comic_number(self):
        average = 0
        total = 0
        comics = 0
        for comic in self.__comic_list:
            total += comic.issue_number
            comics += 1
        average = total / comics
        return average