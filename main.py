import parse
import collate
import compose


def main():
    print("Downloading partial images")
    parse.main()
    print("Collating parts into full pages")
    collate.main()
    print("Composing images into PDF")
    compose.main()
    print("Done!")


if __name__ == "__main__":
    main()
