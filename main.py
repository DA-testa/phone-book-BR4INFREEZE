class Query:
    def __init__(self, query):
        if len(query) > 3:
            print("INPUT-OUTPUT ERROR")
            exit()
        self.type = query[0]
        if len(query[1]) > 7:
            print("INPUT-OUTPUT ERROR")
            exit()
        if check_zeros(query[1]) and check_int(query[1]):
            self.number = int(query[1])
        if self.type == 'add':
            if len(query[2]) > 15 or query[2] == 'not found' or check_latin(query[2]):
                print("INPUT-OUTPUT ERROR")
                exit()
            self.name = query[2]


def check_latin(s):
    if s.isalpha():
        if all(ord(a) < 128 for a in s):
            return False
    return True


def check_zeros(s):
    if s.startswith('0'):
        if s == '0':
            return True
        else:
            print("INPUT-OUTPUT ERROR")
            exit()
    else:
        return True


def check_int(i):
    try:
        int(i)
        return True
    except ValueError:
        print("INPUT-OUTPUT ERROR")
        exit()


def read():
    first = input()
    if check_int(first):
        N = int(first)
        if 1<=N<=10**5:
            try:
                return [Query(input().split()) for i in range(N)]
            except (ValueError, IndexError):
                print("INPUT-OUTPUT ERROR")
                exit()
        else:
            print("INPUT-OUTPUT ERROR")
            exit()


def write(result):
    print('\n'.join(result))


def process(queries):
    result = []
    contacts = []
    for current in queries:
        if current.type == 'add':
            for contact in contacts:
                if contact.number == current.number:
                    contact.name = current.name
                    break
            else:
                contacts.append(current)
        elif current.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == current.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == current.number:
                    response = contact.name
                    break
            result.append(response)
    return result


if __name__ == '__main__':
    write(process(read()))
