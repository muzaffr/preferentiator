from sys import argv
from os.path import splitext

class Item:

    def __init__(self, name):
        self.name = str(name)

    def __repr__(self):
        return self.name

    def __lt__(self, item):
        while True:
            res = input("{} vs. {}?\n(L or R): ".format(self, item)).upper()
            if res == 'L':
                return False
            elif res == 'R':
                return True
            else:
                print("\nInvalid selection.")


def merge_sort(l):
    
    def merge(l1, l2):
        n, m = len(l1), len(l2)
        i, j = 0, 0
        merged = []
        while i < n and j < m:
            if l1[i] < l2[j]:
                merged.append(l1[i])
                i += 1
            else:
                merged.append(l2[j])
                j += 1
        while i < n:
            merged.append(l1[i])
            i += 1
        while j < m:
            merged.append(l2[j])
            j += 1
        return merged

    p = len(l)//2
    if p == 0:
        return l
    return merge(merge_sort(l[:p]), merge_sort(l[p:]))


def main():

    if len(argv) != 2:
        print("Usage: python main.py <filename>")
        return
    try:
        with open(argv[1], 'r') as f:
            l = [line.rstrip('\n') for line in f]
    except FileNotFoundError:
        print("File not found.")
        return

    s = merge_sort([Item(x) for x in l])[::-1]
    print()
    with open(splitext(argv[1])[0] + '.out.txt', 'w') as f:
        for i, item in enumerate(s):
            f.write(str(i+1) + ' ' + str(item) + '\n')
            print(i+1, item)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated.")
    except EOFError:
        print("Input terminated.")
