#!/usr/bin/env python3
import os, time, subprocess

say = subprocess.Popen
saypoem = subprocess.run

def add_nums(iterable):
    newlist = []
    for poem in iterable:
        newlist.append(str(iterable.index(poem)+1) +' '+poem)
    return newlist

def read_poem(path):
    with open(path, 'r') as poem:
        lines = poem.readlines()
        for poem_line in lines:
            if poem_line != '\n':
                print(poem_line + '\n')
                saypoem('say "{}"'.format(poem_line).split())
                time.sleep(0.5)
            else:
                print()

def main():
    import time, os
    file_path = os.path.dirname(os.path.abspath(__file__))+'/Catalog'
    while True:
        os.system('clear')
        while True:

            if os.path.isdir(file_path):
                print_list = os.listdir(file_path)
                for item in print_list:
                    print_list[print_list.index(item)] = print_list[print_list.index(item)].replace('.txt', '')
                try: print_list.remove('.DS_Store')
                except: pass
                if file_path != os.path.dirname(os.path.abspath(__file__))+'/Catalog':
                    print_list.insert(0, 'Back')

                if file_path == os.path.dirname(os.path.abspath(__file__))+'/Catalog':
                    _ = say('say pick a number to enter that section of the catalog from 1 to {second}'.format(second=len(print_list)).split())
                    print('Pick a number to enter that section of the catalog')

                for i in add_nums(print_list):
                    print(i)
                print()
                subject = 'a'
                while not subject.isnumeric():
                    subject = input()
                    print()
                os.system('clear')
                for i in add_nums(print_list):
                    if i[:len(subject)] == subject:
                        if i == '1 Back':
                            file_path = '/' + '/'.join(file_path.split('/')[:-1])
                        else:
                            file_path = file_path + '/' + i[len(subject)+1:]
            elif os.path.isfile(file_path + '.txt'):
                read_poem(file_path + '.txt')
                file_path = '/'.join(file_path.split('/')[:-1])
                break
            else:
                print('It seems there is an error')
                file_path = '/'.join(file_path.split('/')[:-1])
        os.system('clear')
        _ = say('say would you like to hear more? yes or no'.split())
        contin = input('Would you like to hear more? yes or no? ')
        if contin == 'no':
            break


if __name__ == '__main__':
    main()
    os.system('clear')
