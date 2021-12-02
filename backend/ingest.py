import json
import sys


def parse(pathToJson):
    try:
        with open(pathToJson) as jsonFile:
            input = json.load(jsonFile)
    except json.decoder.JSONDecodeError :
        raise Exception("JSONDecodeError : No valid JSON file was provided")

    return input


if __name__ == "__main__":
    path = sys.argv[1]
    parsedData = parse(path)
    print(parsedData)
