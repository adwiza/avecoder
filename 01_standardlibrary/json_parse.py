import json

def main():

    json_str = ''' {
        "make" : "Opel",
        "model" : "Mokka",
        "colours" : [
            "Black",
            "White",
            "Blue"
        ],
        "price" : 20000.99
    
    }'''

    data = json.loads(json_str)

    print('Car: ' + data['make'])

    if data['model'] == 'Mokka':
        print('It\'s Mokka!')

    for colour in data['colours']:
        print('Colours: ' + colour)


if __name__ == '__main__':
    main()
