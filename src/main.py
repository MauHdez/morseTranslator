import morseTranslator
import argparse
import os

parser = argparse.ArgumentParser(description='Morse translator')
to_group = parser.add_mutually_exclusive_group(required = True)
to_group.add_argument('-m','--toMorse',help = 'Translate to morse', action = 'store_true')
to_group.add_argument('-a','--toAlpha',help = 'Translate to normal text', action = 'store_true')

in_group = parser.add_mutually_exclusive_group(required = True)
in_group.add_argument('-f', '--file', help='read from file', dest="filename")
in_group.add_argument('-s', '--string', help='read string from terminal', dest="string")

parser.add_argument('-o', '--output', help='write to output file', action='store_true')
args = parser.parse_args()

if __name__ == '__main__':
    if args.toAlpha:

        exit('Not implemented')

    elif args.filename:

        with open(args.filename, 'r') as f:
            lines = f.readlines()
            sentence = ''
            for l in lines:
                sentence += l
    elif args.string:
        sentence = args.string

    res = morseTranslator.translate_to_Morse(sentence)

    if args.output:

        path = 'output/'
        if not os.path.exists(os.path.dirname(path)):
            try:
                os.makedirs(os.path.dirname(path))
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
        with open(path + str(args.filename) + '.out', 'a+') as o:
            o.write(res)
    else:
        print res
