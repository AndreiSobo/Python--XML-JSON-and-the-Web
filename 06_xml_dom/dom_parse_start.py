# Use the XML DOM to parse a document in memory

import xml.dom.minidom
import requests


def main():
    # retrieve the XML data using the requests library
    url = "http://httpbin.org/xml"
    result = requests.get(url)
    # print(type(result.text))
    
    # TODO: parse the returned content into a DOM structure
    domtree = xml.dom.minidom.parseString(result.text)
    root_node = domtree.documentElement

    # TODO: display some information about the content
    print("root element is: {0}".format(root_node.nodeName))
    print("title of the document is: {0}".format(root_node.getAttribute('title')))
    print("\n")

    items = domtree.getElementsByTagName('item')
    print(f"there are {len(items)} items.")
    # print([type(x) for x in items])

    # manipulate the XML content in memory
    # TODO: create a new item tag

    new_item = domtree.createElement('item')

    # TODO: add some text to the item

    new_item.appendChild(domtree.createTextNode('This is some random text but so important '))

    # TODO: now add the item to the first slide

    first_slide = domtree.getElementsByTagName('slide')[0]
    first_slide.appendChild(new_item)

    # TODO: Now count the item tags again
    print("\n")
    items = domtree.getElementsByTagName('item')
    print(f"there are {len(items)} items.")
    

if __name__ == "__main__":
    main()
