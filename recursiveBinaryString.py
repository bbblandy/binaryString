def calc(value, index):
    if index == len(value):
        print(''.join(value))
        return

    if value[index] == "?":

        value[index] = '0'
        calc(value, index + 1)

        value[index] = '1'
        calc(value, index + 1)

        value[index] = '?'
    else:
        calc(value, index + 1)

def main():
    value = ''.join(['0' '?' '1' '?'])
    value = list(value)
    calc(value, 0)

if __name__ == "__main__":
    main()


