import sys


def main():
    lines = sys.stdin.readlines()

    lines.sort()

    sys.stdout.writelines(lines)


if __name__ == '__main__':
    main()
