# Process JSON data returned from a server

# TODO: use the JSON module
import json

def main():
    # define a string of JSON code
    jsonStr = '''{
            "sandwich" : "Reuben",
            "toasted" : true,
            "toppings" : [
                "Thousand Island Dressing",
                "Sauerkraut",
                "Pickles"
            ],
            "price" : 8.99
        }'''

    # TODO: parse the JSON data using loads
    data = json.loads(jsonStr)


    # TODO: print information from the data structure
    print(data)
    print("\n")
    print(type(data))
    print("\n")
    print("Sandwich type: " + data["sandwich"])
    if data["price"] < 5:
        print("And it costs less than a fiver")
    elif data["price"] < 10:
        print("And it costs less than a tenner")
    else:
        print("it costs a fortune!")
    for x in data["toppings"]:
        print("toppings are: ", x)

if __name__ == "__main__":
    main()
