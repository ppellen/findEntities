#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        PUNITHELP_find_HTML_TextInChm.py
# Purpose:     Find text in html files.
#
# Author:      Administrateur
#
# Created:     2017
# Copyright:   (c) Administrateur 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------


from HTMLParser import HTMLParser

import os
import pickle
import utils_load_pickle

dbg = False

path_here = os.path.dirname(os.path.abspath(__file__))


class myParserClass(HTMLParser):

    def __init__(self, chm_name, string_to_find):
        self.chm_name = chm_name
        self.string_to_find = string_to_find.lower()
        self.currentHtmFile= None
        self.text_found_in = {}
        return HTMLParser.__init__(self)

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
        if self.string_to_find in data.lower():
            if not self.currentHtmFile in self.text_found_in.keys():
                self.text_found_in[self.currentHtmFile] = 1
            else:
                self.text_found_in[self.currentHtmFile] += 1

            if dbg: print "found in %s" % (self.currentHtmFile,)
        return HTMLParser.handle_data(self, data)

    def handle_charref(self, name):
        return HTMLParser.handle_charref(self, name)

    def handle_entityref(self, name):
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


def removeFromCHMFileList( myCHMFileList, *theseCHM ):
    for thisCHM in theseCHM:
        try:
            myCHMFileList.remove(thisCHM)
        except:
            pass


def main():

    for text_to_find in ["M580","X80"]:  # ["socollaborative", "M340", "struxure", "Plant", "Unity" ]:
        find_string_in_html_files(r'C:\pytmp\UnitySource',text_to_find)


def find_string_in_html_files(source_dir, string_to_find):
    _space = r' '

    dir_ = source_dir

    print dir_
    chdir(dir_)

    all_found = []

    myModulesList=[]
    i = 0

    dirList = listdir( dir_ )
    for d in dirList:
        if isdir(d) : # os.path.
            if d <> 'PUnit' and d <> 'symax':
                myModulesList.append(d.lower())

    removeFromCHMFileList ( myModulesList,  # "trending",
                            "PMESE", "PMEMSTR", "1000", "1001", "1002",
                            "atv6xxprog", "atv6xxdtm", "atv6xx")

    scans = 0

    for myModule in myModulesList:

        myHtmFilesList=[]

        i = 0
        for root, dirs, files in walk('.\\'+myModule):
            for name in files:
                if (name.split('.')[-1] in ["htm", "html"]):
                    myHtmFilesList.append(name)
                    i = i+1

        # if dbg : myHtmFilesList=['140NOC77101_D-NA-0013949.htm']

        myParser =  myParserClass(myModule, string_to_find)

        for thisHtmFile in myHtmFilesList:
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

                try:
                    myParser.feed(ff.read())
                except:
                    print 'error parsing !!! ',thisHtmFile,'\\',ff


                ff.close()
                # print '---------------------------'
                pass

            if dbg:
                for found in myParser.text_found_in.keys():
                    print "found in %s : %d time(s)." % ( found , myParser.text_found_in[found] )

        scans += 1

        all_found.append( (myModule,myParser.text_found_in) )
        try:
            myParser.close()
        except:
            pass

        if scans == 10:  # TODO for dbg
            pass
            # break

    pass
    chdir(path_here)

    temp_pickle_file = string_to_find + "_found.pck"
    pickle.dump( { 'Character string searched' : string_to_find , 'found_in': all_found}, open( temp_pickle_file, "wb" ) )

    utils_load_pickle.print_result_from_pickle_file(temp_pickle_file) # creates a txt file

    #  #####################################################################################

if __name__ == '__main__':
    main()
