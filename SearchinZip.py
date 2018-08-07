# Python code to parse through zip files

import zipfile
import os
import re
import glob

__author__  = "Sai Krishna Pavan Suryatej, Meda"
__twitter__ = "@SuryaMskp"


class SearchinZip(object):
    def __init__(self, searchWord, searchPath):
        self.searchWord = searchWord
        self.searchPath = searchPath
    def search_in_path(self):
        for ffile in glob.glob(self.searchPath + '/*.zip'):
            with zipfile.ZipFile(ffile) as z:
                for filename in z.namelist():
                    if not os.path.isdir(filename):
                        with z.open(filename) as f:
                            counter = 1
                            for line in f:
                                m = re.search(self.searchWord, line.decode('utf-8'))
                                if m:
                                    print("Found {0} at line {1}".format(self.searchWord, counter))
                                    print("{}".format(line.decode("utf-8").replace('\n', '')))
                                counter += 1
if __name__ == '__main__':
    # Enter the path in which you wanna search
    path = ""
    ## Ex: path = r"C:\Users\user"

    # Enter the Search key word
    search = ""
    ## Ex: search = "Apple"
    
    obj = SearchinZip(search, path)
    obj.search_in_path()