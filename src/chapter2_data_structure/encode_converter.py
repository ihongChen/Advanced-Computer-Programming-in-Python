#! encoding:utf8

import argparse

def cp950_to_utf8(filename):
    s = open(filename,"rb").read().decode("big5").encode("utf8")
    # print(s) ##
    open(filename,'wb').write(s)
    
def utf8_to_cp950(filename):
    s = open(filename,"rb").read().decode("utf8").encode("cp950")
    open(filename,'wb').write(s)

def main():
    parser = argparse.ArgumentParser(description='This is arg parser test...',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('--input', type=str, 
        dest='inputfile', help='input filename', required=True)

    parser.add_argument('--from', type=str, dest='_from', help='decode from', required=True)
    parser.add_argument('--to', type=str, dest='_to', help='encode to', required=True)

    args = parser.parse_args()

    print('inputfile:{}'.format(args.inputfile))
    if args._from == 'cp950' and args._to == 'utf8':
        cp950_to_utf8(args.inputfile)
    elif args._from =='utf8' and args._to == 'cp950':
        utf8_to_cp950(args.inputfile)

if __name__ == '__main__':
    main()