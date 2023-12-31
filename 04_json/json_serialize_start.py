# Process JSON data returned from a server

# use the JSON module
import json


def main():
    # define a python ditcionary
    pythonData = {
        "sandwich": "Reuben",
        "toasted": True,
        "toppings": ["Thousand Island Dressing",
                     "Sauerkraut",
                     "Pickles"
                     ],
        "price": 8.99
    }

    # TODO: serialize to JSON using dumps
    json_string = json.dumps(pythonData)


    # TODO: print the resulting JSON string
    print("JSON Data: --------")
    print(json_string)
    print(type(json_string))
    print(json_string[0:4])


if __name__ == "__main__":
    main()
