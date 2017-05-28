import greet

import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('name')
    args = parser.parse_args()
    greeting = greet.greet(args.name)
    print(greeting)

if __name__ == '__main__':
    main()
