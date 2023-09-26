# using the requests library to access internet data

#import the requests library
import requests

def main():
    # TODO: Use requests to issue a standard HTTP GET request
    url = "http://httpbin.org/xml"
    result = requests.get(url)
    printResults(result)

    
    # TODO: Send some parameters to the URL via a GET request
    # Note that requests handles this for you, no manual encoding
    url = "http://httpbin.org/post"
    dataV = {
        "key1": "value1",
        "key2": "value2"
    }
    request = requests.post(url, params=dataV)
    printResults(request)

    # TODO: Pass a custom header to the server
    url = "http://httpbin.org/get"
    headerV = {
        "header_key1": "header_value1",
        "header_key2": "header_value2"
    }
    request = requests.get(url, headers=headerV)
    printResults(request)
    

def printResults(resData):
    print("Result code: {0}".format(resData.status_code))
    print("\n")

    print("Headers: ----------------------")
    print(resData.headers)
    print("\n")

    print("Returned data: ----------------------")
    print(resData.text)

if __name__ == "__main__":
    main()
