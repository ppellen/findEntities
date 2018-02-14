#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        PUNITHELP_find_HTML_EntityRefInChm.py
# Purpose:     Find  Entity Refs in html files.
#
# Author:      Administrateur
#
# Created:     11/06/2011
# Copyright:   (c) Administrateur 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------


from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

dbg = True

class myParserClass(HTMLParser):

    def handle_starttag(self, tag, attrs):
        return HTMLParser.handle_starttag(self, tag, attrs)

    def handle_endtag(self, tag):
        return HTMLParser.handle_endtag(self, tag)

    def reset(self):
        # self.myData = ''
        HTMLParser.reset(self) #

    def feed(self, data):
        HTMLParser.feed(self, data) # some text to the parser. It is processed insofar as it consists of complete elements; incomplete data is buffered until more data is fed or close() is called.


    def close(self):
        if dbg :
            pass

        HTMLParser.close(self) # Force processing of all buffered data as if it were followed by an end-of-file mark. This method may be redefined by a derived class to define additional processing at the end of the input, but the redefined version should always call the HTMLParser base class method close().

    def getpos(self):
        return HTMLParser.getpos(self) # Return current line number and offset.

    def get_starttag_text(self):
        return HTMLParser.get_starttag_text(self)

    def handle_startendtag(self, tag, attrs):
        ##     Similar to handle_starttag(), but called when the parser encounters an XHTML-style empty tag (<a .../>). This method may be overridden by subclasses which require this particular lexical information; the default implementation simple calls handle_starttag() and handle_endtag().
        return HTMLParser.handle_startendtag(self, tag, attrs)

    def handle_data(self, data):
        # self.myData = self.myData + data
        return HTMLParser.handle_data(self, data)

    def handle_charref(self, name):
        if False:
            if name.startswith('x'):
                c = unichr(int(name[1:], 16))
            else:
                c = unichr(int(name))
            self.EntityRefsFound.append( c )
        return HTMLParser.handle_charref(self, name)

    def handle_entityref(self, name):
        self.EntityRefsFound.append(unichr(name2codepoint[name]))
        return HTMLParser.handle_entityref(self, name)


    def handle_comment(self, data):
        return HTMLParser.handle_comment(self, data)
    def handle_decl(self, decl):
        return HTMLParser.handle_decl(self, decl)
    def unknown_decl(self, data):
        return HTMLParser.unknown_decl(self, data)
    def handle_pi(self, data):
        return HTMLParser.handle_pi(self, data)


from os import chdir, walk, listdir, path
from os.path import isdir

def main():
    _space = r' '

    #  dir_ =   r'D:\TECH_PUB\Unity_V6_IPR\IR10B_delivery\Eng_1033_links_corrected' # r'D:\tmp\py_links_ref' #
    dir_ = r'D:\tmp\UPV7IR8-ALL-SOURCES'

    print dir_
    chdir(dir_)


    myModulesList=[]
    i = 0

    dirList = listdir( dir_ )
    for d in dirList:
        if isdir(d) : # os.path.
            if d <> 'PUnit' and d <> 'symax':
                myModulesList.append(d.lower())

##    for root, dirs, files in walk('.'):     # BUILD CHM LIST
##        for name in files:
##            if (name.split('.')[-1] == "chm"):
##                myCHMsList.append(name)
##                i = i+1

    # myTCTProductsList = [ 'TSXETC100','TSXETC101','u984lib','u984opmo','uloader','weighp']

    for myModule in myModulesList:

        myHtmFilesList=[]

        i = 0
        for root, dirs, files in walk('.\\'+myModule):
            for name in files:
                if (name.split('.')[-1] in ["htm", "html"]):
                    myHtmFilesList.append(name)
                    i = i+1
##                  if i==10:
##                        break
##                  del myHtmFilesList[10:]

        # if dbg : myHtmFilesList=['140NOC77101_D-NA-0013949.htm']

        myParser =  myParserClass()

        for thisHtmFile in myHtmFilesList:
            myParser.EntityRefsFound = []
            myParser.currentHtmFile= thisHtmFile

            if True:

                try:
                    ff = open(myModule+'\\'+thisHtmFile)
                    # print str(myModule+'\\'+thisHtmFile)+':'
                except:
                    try:
                        ff = open(myModule+'\\html\\'+thisHtmFile)   # symax type
                        # print str(myModule+'\\html\\'+thisHtmFile)+':'
                    except:
                        ff = open(myModule+'\\contents\\'+thisHtmFile)   # PUnit type
                        # print str(myModule+'\\contents\\'+thisHtmFile)+':'

    ##            if f=='Whatsnew_eng.html':  ms html cannot be parsed ?
    ##                pass

                try:
                    myParser.feed(ff.read())
                except:
                    print 'error parsing !!! ',thisHtmFile,'\\',ff

                if len(myParser.EntityRefsFound) <>0:
                    print 'Found in '+thisHtmFile+': ' + ', '.join(x for x in myParser.EntityRefsFound)

                    pass

                ff.close()
                # print '---------------------------'
                pass

        try:
            myParser.close()
        except:
            pass


if __name__ == '__main__':
    main()
