calls = 0
string = input('Введите слово: ')
list1 = []
def count_calls():
    global calls
    calls += 1
def string_info(string):
    global list1
    size = len(string)
    list1.append(size)
    string1 = string.upper()
    string2 = string.lower()
    list1.append(string1)
    list1.append(string2)
    print(tuple(list1))
    count_calls()
string_info(string)
list_to_search = input('Введите список для поиска: ').split()
def is_contains(string, list_to_search):
    if any(substring in string for substring in list_to_search):
        is_contains = True
        print(is_contains)
        count_calls()
    else:
        is_contains = False
        print(is_contains)
        count_calls()
is_contains(string, list_to_search)
print(calls)

