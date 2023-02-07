import configparser
import parse, collate, compose

def main():
    config = configparser.ConfigParser()
    config.read("settings.ini")
    print("Downloading partial images")
    parse.parse(config["Car"]["id"])
    print("Collating parts into full pages")
    collate.collate()
    print("Composing images into PDF")
    compose.compose()
    print("Done!")

if __name__ == "__main__":
    main()
