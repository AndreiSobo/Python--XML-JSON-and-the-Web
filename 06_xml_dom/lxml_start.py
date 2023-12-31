# Use the lxml library to parse a document in memory

import requests
from lxml import etree


def main():
    # retrieve the XML data using the requests library
    url = "http://httpbin.org/xml"
    result = requests.get(url)

    # TODO: build a doc structure using the ElementTree API
    doc = etree.fromstring(result.content)

    # TODO: Access the value of an attribute
    print(doc.tag)
    print(doc.attrib('title'))

    # TODO: Iterate over tags

    # TODO: Create a new slide

    # TODO: Count the number of slides


if __name__ == "__main__":
    main()
