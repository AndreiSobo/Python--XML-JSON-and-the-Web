# parse XML data using the SAX parser

import requests
import xml.sax

# TODO: define the ContentHandler subclass for our content
class MyContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.slideCount = 0
        self.itemCount = 0
        self.isInTitle = False

    #TODO: Handle startElement
    def startElement(self, tagname, attrs):
        if tagname == "slideshow":
            print("Slideshow title is: " + attrs["title"])
        elif tagname == "item":
            self.itemCount += 1
        elif tagname == "slide":
            self.slideCount += 1
        elif tagname == "title":
            self.isInTitle = True
    #TODO: Handle endElement
    def endElement(self, tagname):
        if tagname == "title":
            self.isInTitle = False

    #TODO: Handle text data
    def textData(self, chars):
        if self.isInTitle:
            print("title" + chars)

    #TODO: Handle startDocument
    def startDocument(self):
        print("We starting now!!")

    #TODO: Handle endDocument
    def endDocument(self):
        print("We finishing up!1")


def main():
    # create a new content handler for the SAX parser
    handler = MyContentHandler()

    # use the Requests lib to get XML data from the server
    # remember that Requests auto-decodes our content
    url = "http://httpbin.org/xml"
    result = requests.get(url)
   
    

    # TODO: call the parseString method on the XML text content received
    xml.sax.parseString(result.text, handler)
    

    # when we're done, print out some interesting results
    print("There were {0} slide elements".format(handler.slideCount))
    print("There were {0} item elements".format(handler.itemCount))


if __name__ == "__main__":
    main()
