import json
from json import JSONDecodeError


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

    try:
        data = json.loads(json_str)
    except JSONDecodeError as err:
        print('JSON Decoding Error:')
        print(err.msg)
        print(err.lineno, err.colno)

    print('Car: ' + data['make'])

    if data['model'] == 'Mokka':
        print('It\'s Mokka!')

    for colour in data['colours']:
        print('Colours: ' + colour)


if __name__ == '__main__':
    main()
