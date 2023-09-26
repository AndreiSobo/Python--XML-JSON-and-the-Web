# using the requests library to access internet data

#import the requests library
import requests
import json


def main():
    # Use requests to issue a standard HTTP GET request
    url = "http://httpbin.org/json"
    result = requests.get(url)
    # print(type(result))
    # print(result.text)
    

    # TODO: Use the built-in JSON function to return parsed data
    data_object = result.json()
    print(data_object)
    print(type(data_object))
    print(json.dumps(data_object, indent=4))
    # TODO: Access data in the python object
    print(data_object["slideshow"]["author"])



if __name__ == "__main__":
    main()
