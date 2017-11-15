import sys
import morseTranslator
# import argparse
#
# parser = argparse.ArgumentParser(description='Morse translator')
# parser.add_argument('-f', '--file', help='read from file', action='store_true')
# parser.add_argument('filename')
# parser.add_argument('-o', '--output', help='write to output file', action='store_true')
# args = parser.parse_args()

if __name__ == '__main__':
    if len(sys.argv) > 1 and len(sys.argv) == 2:
        sentence = sys.argv[1]
    else:
        sentence = 'Hello, world.'

    print morseTranslator.translate_to_Morse(sentence)
