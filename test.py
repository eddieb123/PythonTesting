'''
def descending_order(num):
    rev = ""
    sorted_num = sorted(num)
    for letter in sorted_num:
        rev = letter + rev
    print(rev)


descending_order(str(input("Enter a number: ")))

'''

'''
def alphabet_position(text):
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in text:
        if letter.lower() in "abcdefghijklmnopqrstuvwxyz":
            result = result + str(((alphabet.index(letter.lower())))+1) + " "
        else:
            result = result
    print(result)

alphabet_position(input("Enter text: "))
'''
'''
def is_triangle(a, b, c):
    if (a+b > c) and (a+c > b) and (b+c > a):
        return True
    else:
        return False


print(is_triangle(7,5,10))
'''
'''
def get_middle(s):
    middle = ""
    if 1 > len(s) % 2:
        middle_number = int(len(s) / 2)
        middle = str(s[middle_number-1]) + str(s[middle_number])
    else:
        middle_number = int((len(s) + 1) / 2)
        middle = str(s[middle_number-1])
    print(middle)

get_middle("hello")
'''

'''
def binary_array_to_number(arr):
    arr = arr[::-1]
    result = 0
    # length = int(len(arr))
    position = 1
    for number in arr:
        result += ((int(number))*position)
        position = position * 2
    print(result)


list = [0, 1, 0, 1]

def binary_array_to_number(arr):
    arr = arr[::-1]
    result = 0
    position = 1
    for number in arr:
        result += ((int(number))*position)
        position = position * 2
    print(result)


binary_array_to_number([0, 0, 0, 1])


binary_array_to_number(list)
'''
'''
def binary_array_to_number(arr):
    result = 0
    position = 1
    for number in reversed(arr):
        result += ((int(number))*position)
        position = position * 2
    print(result)


binary_array_to_number([0, 0, 1, 1])

def binary_array_to_number(arr):
    arr.reverse()
    result = 0
    position = 1
    for number in arr:
        result += ((int(number))*position)
        position = position * 2
    print(result)


binary_array_to_number([0, 0, 1, 1])
'''
'''
def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)


print(binary_array_to_number([1,1,1,1]))
'''
'''
def to_jaden_case(string):
    result = ""
    capitalise = True
    for letter in string:
        if capitalise and letter != " ":
            result += letter.upper()
            capitalise = False
        elif not capitalise and letter != " ":
            result += letter.lower()
        elif not capitalise and letter == " ":
            result += letter.lower()
            capitalise = True
    print(result)

to_jaden_case("how can mirrors be real if our eyes aren't real")

#look at this jaden case challenge! use of a boolean to change the behaviour of for loop dependent on the previous item!!!

'''
'''
import math

print(math.sqrt(4))


def is_square(n):
    try:
        sqrt = math.sqrt(n)
        if float(sqrt % 1) > 0:
            return False
        else:
            return True
    except ValueError as err:
        return err


print(is_square(-5))

print(float(6.5 % 1))
'''
'''

def is_square(n):
    if n < 0:
        return False
    elif int(n**.5)**2 == n:
        return True
    elif int(n**.5)**2 != n:
        return False


print(is_square(26))
'''
'''
# Using "Is Instance"

integer1 = 5
float1 = 5.5

print(isinstance(float1, (int)))
print(isinstance(float1, (float)))

# therefore another way to do the previous problem

def is_square(n):
    sqrt = n**0.5
    if isinstance(sqrt, int):
        return True
    else:
        return False

print(is_square(25))
'''
'''
def is_valid_walk(walk):
    if len(walk) == 10:
        n = walk.count("n")
        e = walk.count("e")
        s = walk.count("s")
        w = walk.count("w")
        if n == s and e == w:
            return True
        else:
            return False
    elif len(walk) != 10:
        return False


print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']))
'''
'''
def getCount(inputStr):
    num_vowels = 0
    for letter in inputStr:
        if letter in "aeiouAEIOU":
            num_vowels += 1
    return num_vowels

print(getCount("abracadabra"))

'''
'''
class coordinates:

    def __init__(self, x, y):
        self.x = x
        self.y = y

coordinate1 = coordinates(0,0)

print(coordinate1.x)

coordinate_list = [
    coordinates(0, 0),
    coordinates(0, 1),
    coordinates(0, 2),
    coordinates(1, 0),
    coordinates(1, 1),
    coordinates(1, 2),
    coordinates(1, 3),
    coordinates(2, 0),
    coordinates(2, 1),
    coordinates(2, 2),
    coordinates(2, 3)
]

def find_rects(points):
    number = len(points)
    count = 0
    for i in range(number):
        start_point = points[i]
        for j in range(number):
            if points[j].x > start_point.x and points[j].y > start_point.y:
                for k in range(number):
                    potential = False
                    if points[k].x == start_point.x and points[k].y == points[j].y:
                        potential = True
                        for l in range(number):
                            if points[l].x == points[j].x and points[l].y == start_point.y and potential:
                                count += 1
    return count

print(find_rects(coordinate_list))
'''
'''

point1 = 1
point2 = 2

hypopoint = coordinates(point1, point2)

for i in range(9):
    if coordinate_list[i].x == 1 and coordinate_list[i].y == 1:
        print("yes")
    else:
        print("no")

print(coordinate_list[1].x)

start_point = coordinate_list[1]

print(start_point.x)

#print(any(coordinates.x == 1 in coordinate_list))

find_rects(coordinate_list)

'''

'''
def digital_root(n):
    result = []
    n = str(n)
    digs = len(n)
    if digs > 1:
        for i in range(digs):
            result = result
    else:
        return result

def digital_root2(n):
    res = n
    res = str(res)
    digs = len(res)
    for i in range(digs):
        res2 = int(res) + int(res[i])
    if len(str(res2)) > 1:
        digital_root2(res2)
    else:
        return res2




print(digital_root(456))

print(digital_root2(456))
'''


'''
def digital_root(n):
    result = 0
    n = str(n)
    digs = len(n)
    list = []
    for i in range(digs):
        list.append(int(n[i]))
    if len(list) == 1:
        return list
    elif len(list) > 1:
        digital_root(sum(list))


print(digital_root(4561))
'''
'''
def digital_root(n):
    if len(str(n)) == 1:
        return n
    else:
        sum = 0
        for i in str(n):
            sum += int(i)
        n = sum
        return digital_root(n)

print(digital_root(4561))

def digital_root(n):
    return n % 9 or n and 9

print(digital_root(-1))
'''
#def increment_by_one(n):
 #   n += 1
  #  return n

#result = map(increment_by_one, [1, 2, 3, 4, 5, 6])

#print(list(result))

#def adder(n):
#    result = sum(map(int, str(n)))
#    return result

#print(adder(456))

#print(sum([1, 2], 3))

'''
def is_isogram(string):
    string = string.lower()
    isogram = True
    rewrite = ""
    for i in string:
        if i not in rewrite:
            rewrite += i
        elif i in rewrite:
            isogram = False
    return isogram


print(is_isogram("Dermatoglyphics"))
print(is_isogram("aba"))
'''
'''
def persistence(n):
    count = 0
    n = str(n)
    while len(str(n)) > 1:
        result = 1
        for i in str(n):
            result = result * int(i)
        count += 1
        n = result
    return count



print(persistence(999))
print(persistence(4))


letters = ['A', 'B', 'C']
def lower_case(string):
    string = string.lower()
    return string


lower_map = map(lower_case, letters)
print(letters)
lower = list(lower_map)
print(list(lower))

def adder(n):
    result = 0
    for i in n:
        result += i
    return result


numbers = [1, 2, 3]
number = 1234
print(sum(map(int, str(number))))

print(adder(numbers))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)
temp = [36.5, 37, 37.5,39]

F = map(fahrenheit, temp)
Ftemp = list(F)
C = map(celsius, Ftemp)

print(Ftemp)
print(list(C))

fib = [0,1,1,2,3,5,8,13,21,34,55]
result = list(filter(lambda x: x % 2, fib))
print(result)

result = filter(lambda x: x % 2 == 0, fib)
print(list(result))

from functools import reduce

sum = reduce(lambda x,y: x+y, [47,11,42,13])

print(sum)

pythags = [(x, y, z) for x in range(1, 30) for y in range(x, 30) for z in range(y, 30) if x**2 + y**2 == z**2]

print(pythags)

'''
'''
x = (x**2 for x in range(20))

print(x)

x = list(x)

print(x)

#Sieve of Eratosthenes

#sieve = (for i in range(2, n+1) )

no_primes = [j for i in range(2, 10) for j in range(i*2, 100, i)]
primes = [x for x in range(2, 100) if x not in no_primes]
print(no_primes)
print(primes)

#for i in range(1, 6):
#    print(i, "o")
'''
'''
from math import sqrt

#def primes(n):
#    if n == 0:
#        return []
#    elif n == 1:
#        return []
#    else:
#        p = int(sqrt(n))
#        no_p = {j for i in range(2, p) for j in range(i*2, n+1, i)}
#        p = [x for x in range(2, n + 1) if x not in no_p]
#    return p

def primes2(n):
    if n == 0:
        return []
    elif n == 1:
        return []
    else:
        p = primes2(int(sqrt(n)))
        no_p = {j for i in p for j in range(i*2, n+1, i)}
        p = [x for x in range(2, n + 1) if x not in no_p]
    return p

#NB NOT SURE WHY ABOVE USE OF RECURSION WORKS! REVISIT!

for i in range(1, 50):
    print(i, primes2(i))

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name)

'''
'''
expertises = ["Python Beginner", "Python Intermediate", "Python Proficient", "Python Advanced"]
expertises_iterator = iter(expertises)

print(next(expertises_iterator))

next(expertises_iterator)

next(expertises_iterator)

next(expertises_iterator)

capitals = {"France":"Paris", "Netherlands":"Amsterdam", "Germany":"Berlin", "Switzerland":"Bern", "Austria":"Vienna"}
for country in capitals:
    print("The capital city of " + country + " is " + capitals[country])

def fibonacci(n):
    a = 0
    b = 1
    counter = 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)

for x in f:
    print(x, " ", end="")
'''
'''
def infinite_looper(objects):
    count = 0
    while True:
        if count >= len(objects):
            count = 0
        try:
            message = yield objects[count]
        except Exception:
            print("index: " + str(count))
        if message != None:
            count = 0 if message < 0 else message
        else:
            count += 1

looper = infinite_looper("Python")

print(next(looper))



print(next(looper))

looper.throw(Exception)

print(next(looper))


't'
>>> next(looper)
'h'
'''
'''
from functools import wraps


def get_ready(gen):
    """
    Decorator: gets a generator gen ready
    by advancing to first yield statement
    """
    @wraps(gen)
    def generator(*args, **kwargs):
        g = gen(*args, **kwargs)
        next(g)
        return g

    return generator


@get_ready
def infinite_looper(objects):
    count = -1
    message = yield None
    while True:
        count += 1
        if message != None:
            count = 0 if message < 0 else message
        if count >= len(objects):
            count = 0
        message = yield objects[count]


x = infinite_looper("abcdef")
print(next(x))
print(x.send(4))
print(next(x))
print(next(x))
print(x.send(5))
print(next(x))

def concatenate(**words):
    result = ""
    for arg in words:
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))

def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result

list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]

print(my_sum(*list1, *list2, *list3))
'''
'''
def accum(string):
    count = 1
    result = ""
    for letter in string:
        additions = 1
        while additions-1 < count:
            if additions == 1 and count == additions:
                result = result + letter.upper() + "-"
                additions += 1
            elif 1 < additions < count-1:
                result = result + letter.lower()
                additions += 1
            elif additions-1 == count-1:
                result = result + letter.lower() + "-"
                additions += 1
        count += 1
    return result
'''
'''
def accum(string):
    length = len(string)
    result = ""
    count = 1
    additions = 0
    for letter in string:
        while additions < length:
            if letter == string[0]:
                result = result + letter.upper() + "-"
        additions += 1

    return result
'''
'''from functools import reduce
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

print(accum("abcd"))
'''
'''

def solution(number):
    set = {i, j for i in range(0, number, 3)j in range(0, number, 5)}
    result = sum(set)
    return result

print(solution(10))

def solution(number):
    set = {i for i in range(0, number, 3)}
    set1 = {j for j in range (0, number, 5)}
    set2 = {*set, *set1}
    result = sum(set2)
    return result

print(solution(10))
'''
'''
def comp(array1, array2):
    same = False
    c = list(map(lambda a: a**2, array1))
    c.sort()
    array2.sort()
    if c == array2:
        same = True
    return same


a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

print(comp(a, b))
'''
'''
def find_even_index(arr):
    result = -1
    length = len(arr)
    for index in range(0, length):
        l = arr[:index]
        r = arr[index+1:]
        if sum(l) == sum(r):
            result = index
        if result != -1:
            break
    return result
'''

'''
def find_even_index(arr):
    for index in range(0, len(arr)):
        if sum(arr[:index]) == sum(arr[index+1:]):
            return index
    return -1




print(find_even_index([10,-80,10,10,15,35,20])) # = 6
print(find_even_index([20,10,-80,10,10,15,35])) # = 0
'''
'''
def high(x):
    values = enumerate("abcdefghijklmnopqrstuvwxyz")
    words = x.split(" ")
    for word in words:
        for letter in word:
            result = 
        
        



print(high('man i need a taxi up to ubud'))
print(high('what time are we climbing up the volcano'))

values = list(enumerate("abcdefghijklmnopqrstuvwxyz", 1))

print(num for value in values if value == 'a')
'''
'''
alpha = ['a', 'b', 'c', 'd']

print(alpha[1])

# : ;      - ~      )D

# for each item: if  1<length<4 -> if item[0] in [':', ';'] and
'''
'''
def count_smileys(arr):
    count = 0
    for item in arr:
        if len(item) == 2:
            if item[0] in [':', ';'] and item[1] in [')', 'D']:
                count += 1
        elif len(item) ==3:
            if item[0] in [':', ';'] and item[1] in ['-', '~'] and item[2] in [')', 'D']:
                count += 1
    return count

print(count_smileys([':)',':(',':D',':O',':;']))
'''
'''
def anagrams(word, words):
    sorted_word = sorted(word)
    list = []
    for item in words:
        item_sorted = sorted(item)
        if item_sorted == sorted_word:
            list.append(item)
    return list




print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))


def decodeMorse(morse_code):
    return " ".join(lambda x: MORSE_CODE[x], words
    for words in list(morse_code.split('   ')) for letters in list(words.split(' ')) for x in letters)
    
def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))
'''
'''
translation = ""
        words = morse_code.split('   ')
        for word in words:
            letters = word.split(' ')
            for letter in letters:
                translation = translation + MORSE_CODE[letter]
            translation = translation + " "
        length = len(translation)
        if length < 2:
            return translation
        else:
            translation = translation[:length-1]
            return translation
'''
'''
def find_outlier(integers):
    
    if len(evens.append(integer) if integer % 2 == 0) for integer in integers





    solution = 0
    for integer in integers:
        if integer % 2 == 0:
            e += 1
        else:
            o += 1
    for integer in integers:
        if e > o:
            if integer % 2 != 0:
                solution += integer
        if o > e:
            if integer % 2 == 0:
                solution += integer
    return solution

print((find_outlier([2, 4, 6, 8, 10, 3])))
'''
'''

def score(dice):
    sum = 0
    counter = [0, 0, 0, 0, 0, 0]
    points = [1000, 200, 300, 400, 500, 600]
    extra = [100, 0, 0, 0, 50, 0]
    for die in dice:
        counter[die - 1] += 1

    for (i, count) in enumerate(counter):
        sum += (points[i] if count >= 3 else 0) + extra[i] * (count % 3)

    return sum


def score(dice):
    score_list3 = []
    score_list1 = []
    for number in dice:
        if dice.count(number) >= 3 and score_list3.count(number) < 3:
            score_list3.append(number)
        elif dice.count(number) >= 3 and score_list3.count(number) == 3:
            score_list1.append(number)
        elif number == 5 or number == 1 and dice.count(number) < 3:
            score_list1.append(number)
    scoring3 = {1: 1000, 6: 600, 5: 500, 4: 400, 3: 300, 2: 200}
    scoring1 = {1: 100, 5: 50}
    score = 0
    if len(score_list3) == 3:
        score += scoring3.get(score_list3[0])
    for single in score_list1:
        if single == 5 or single == 1:
            score += scoring1.get(single)
    return score

'''
'''
def first_non_repeating_letter(string):
    singles = [i for i in string if string.lower().count(i.lower()) == 1]
    return singles[0] if singles else ''


def first_non_repeating_letter(string):
    result = ""
    lower_version = string.lower()
    for letter in string:
        if lower_version.count(letter.lower()) == 1 and len(result) < 1:
            result = result + letter
        elif len(result) == 1:
            break
    return result
'''

#  ['t','u','p'],
#  ['w','h','i'],
#  ['t','s','u'],
#  ['a','t','s'],
#  ['h','a','p'],
#  ['t','i','s'],
#  ['w','h','s']

# {'t', 'u', 'p', 'w', 'h', 'i', 's', 'a', }
'''
def recoverSecret(triplets):
    res = ''
    while triplets != []:
        non_firsts = [num for t in triplets for num in t[1:]]
        firsts = [t[0] for t in triplets]
        for f in firsts:
            if f not in non_firsts:
                res += f
                for t in triplets:
                    if t[0] == f:
                        t.pop(0)
                break
        triplets = [t for t in triplets if t != []]
    return res
'''
'''
def recoverSecret(triplets):
    res = ''
    while triplets != []:
        non_firsts = [num for t in triplets for num in t[1:]]
        firsts = [t[0] for t in triplets]
        for f in firsts:
            if f not in non_firsts:
                res += f
                for t in triplets:
                    if t[0] == f:
                        t.pop(0)
                break
        triplets = [t for t in triplets if t != []]
    return res

print(recoverSecret([['t','u','p'],
                    ['w','h','i'],
                     ['t','s','u'],
                    ['a','t','s'],
                      ['a','u','p'],
                     ['t','i','s'],
                    ['w','h','s']]))


h = "hello"

print(h.find("h", 1, 4))
'''
'''

import math


class Pagehelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        self.local = locals()

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        return int(math.ceil(1.0 * self.item_count() / self.items_per_page))

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if (page_index + 1) * self.items_per_page <= self.item_count():
            return self.items_per_page
        if page_index * self.items_per_page < self.item_count() and (
                page_index + 1) * self.items_per_page > self.item_count():
            return self.item_count() % self.items_per_page
        return -1

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index < self.item_count() and item_index >= 0:
            return item_index / self.items_per_page
        return -1


#collection = range(1, 25)
collection = ['a', 'b', 'c', 'd', 'e', 'f']
helper = Pagehelper(collection, 4)

print(helper.page_count())
print(helper.item_count())
print(helper.page_item_count(0))
print(helper.page_item_count(1))
print(helper.page_item_count(2))
print(helper.page_index(5))
print(helper.page_index(2))
print(helper.page_index(20))


list = ['a','b','c','d','e','f']

new_list = [list[0:3], list[3:5]]

print(int(7/4))



collection = ['a', 'b', 'c', 'd', 'e', 'f']
helper = Pagehelper(collection, 4)

print(helper.page_count())
print(helper.item_count())
print(helper.page_item_count(0))
print(helper.page_item_count(1))
print(helper.page_item_count(2))
print(helper.page_index(5))
print(helper.page_index(2))
print(helper.page_index(20))

'''

#dict_args = enumerate(args, 1)
'''
def solution(args):
    prev_num = args[0]
    prev_num2 = args[0]
    prev_num3 = args[0]
    string = ""
    for j in args:
        if j - prev_num != 1 and prev_num - prev_num2 == 1:
            string += "-" + str(prev_num) + "," + str(j)
        elif j - prev_num != 1 and prev_num - prev_num2 != 1 and prev_num3 - prev_num2 != 1:
            string += "," +str(prev_num2) + "," + str(prev_num)
        elif j - prev_num != 1 and prev_num - prev_num2 != 1 and prev_num3 - prev_num2 == 1:
            string += "," + str(j)
        elif j - prev_num == 1:
            string = string
        prev_num3 = prev_num2
        prev_num2 = prev_num
        prev_num = j
    if string[len(string)-1] != args[len(args)-1]:
        string += "-" + str(prev_num)
    return string[1:]
'''
'''
def solution(args):
    prev_num = args[0]
    prev_num2 = args[0]
    prev_num3 = args[0]
    string = ""
    for j in args:
        if j - prev_num != 1:
            if prev_num - prev_num2 == 1:
                if prev_num2 - prev_num3 == 1:
                    string += "-" + str(prev_num) + "," + str(j)
                elif prev_num2 - prev_num3 != 1:
                    string += "," + str(prev_num) + "," + str(j)
            elif prev_num - prev_num2 != 1:
                string += "," + str(j)
        elif j - prev_num == 1:
            string = string
        prev_num3 = prev_num2
        prev_num2 = prev_num
        prev_num = j
    fdl = len(str(args[len(args)-1]))
    if string[len(string)-fdl:] != str(args[len(args)-1]):
        if int(str(args[len(args)-1])) - int(string[len(string)-fdl:]) == 1:
            string += "," + str(prev_num)
        else:
            string += "-" + str(prev_num)
    return string[1:]
'''
'''
def solution(args):
    out = []
    beg = end = args[0]

    for n in args[1:] + [""]:
        if n != end + 1:
            if end == beg:
                out.append(str(beg))
            elif end == beg + 1:
                out.extend([str(beg), str(end)])
            else:
                out.append(str(beg) + "-" + str(end))
            beg = n
        end = n

    return ",".join(out)

print(solution([-6, -5, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))

print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20, 23, 25, 26]))

'''
'''
def cakes(recipe, available):
    plausible = True
    ratios = []
    for ingredient in recipe:
        if ingredient not in available:
            plausible = False
    if not plausible:
        return 0
    elif plausible:
        for ingredient in recipe:
            ratios.append(int(available.get(ingredient) / recipe.get(ingredient)))
    ratios.sort()
    return ratios[0]

#def cakes(recipe, available):
#    return min(available.get(k, 0)/recipe[k] for k in recipe)



recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print((cakes(recipe, available)))


recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
print((cakes(recipe, available)))
'''

# 31536000
'''
def format_duration(seconds):
    years = 0
    days = 0
    hours = 0
    minutes = 0
    r_seconds = 0
    final = []
    if seconds >= 31536000:
        years += int(seconds/31536000)
        seconds -= years * 31536000
        if years > 1:
            final.append(str(years) + " years")
        else:
            final.append(str(years) + " year")
    if seconds >= 86400:
        days += int(seconds/86400)
        seconds -= days * 86400
        if days > 1:
            final.append(str(days) + " days")
        else:
            final.append(str(days) + " day")
    if seconds >= 3600:
        hours += int(seconds / 3600)
        seconds -= hours * 3600
        if hours > 1:
            final.append(str(hours) + " hours")
        else:
            final.append(str(hours) + " hour")
    if seconds >= 60:
        minutes += int(seconds/60)
        seconds -= minutes * 60
        if minutes > 1:
            final.append(str(minutes) + " minutes")
        else:
            final.append(str(minutes) + " minute")
    if seconds > 0:
        r_seconds += seconds
        if r_seconds > 1:
            final.append(str(r_seconds) + " seconds")
        else:
            final.append(str(r_seconds) + " second")
    if len(final) == 5:
        return final[0] + ", " + final[1] + ", " + final[2] + ", " + final[3] + " and " + final[4]
    elif len(final) == 4:
        return final[0] + ", " + final[1] + ", " + final[2] + " and " + final[3]
    elif len(final) == 3:
        return final[0] + ", " + final[1] + " and " + final[2]
    elif len(final) == 2:
        return final[0] + " and " + final[1]
    elif len(final) == 1:
        return final[0]
    else:
        return "now"




times = [("year", 365 * 24 * 60 * 60), 
         ("day", 24 * 60 * 60),
         ("hour", 60 * 60),
         ("minute", 60),
         ("second", 1)]

def format_duration(seconds):

    if not seconds:
        return "now"

    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs

    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]

print(format_duration(1))
print(format_duration(62))
print(format_duration(120))
print(format_duration(3600))
print(format_duration(3662))

'''
'''
def pick_peaks(arr):
    dict_arr = [(n, arr[n-1]) for n in range(1, len(arr)+1)]
    beg = prev = dict_arr[0]
    position_list = []
    peak_list = []
    for n, a in dict_arr:
        #if n < len(dict_arr):
            if a > prev[1]:
                beg = dict_arr[n-1]
            if a < prev[1] and beg[0] > 1:
                if beg[0] == prev[0] and beg[0] == prev[0]:
                    position_list.append(prev[0] - 1)
                    peak_list.append(prev[1])
                elif beg[1] == prev[1] and beg[0] != prev[0]:
                    position_list.append(beg[0] - 1)
                    peak_list.append(beg[1])
                elif prev[1] < beg[1]:
                    position_list = position_list
            prev = dict_arr[n-1]
    return {"pos":position_list, "peaks":peak_list}

def pick_peaks(arr):
    pos = []
    prob_peak = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            prob_peak = i
        elif arr[i] < arr[i-1] and prob_peak:
            pos.append(prob_peak)
            prob_peak = False
    return {'pos':pos, 'peaks':[arr[i] for i in pos]}



# {"pos":[3,7,10], "peaks":[6,3,2]}
print(pick_peaks([3,3,2,3,6,4,1,2,3,2,1,2,2,2,1]))

'''
'''

def decode_bits(bits):
    prev = bits[0]
    count = 0
    count_list = []
    for b in bits:
        if b == prev:
            count += 1
        elif b != prev:
            count_list.append(count)
            count = 1
        prev = b
    sig_amp = sorted(count_list)[0]
    decoded = ""
    for i in range(0, len(bits) - 1, sig_amp):
        decoded += bits[i]
    dict = {"1":".",
            "111":"-"}
    return "   ".join(" ".join("".join(dict[symbol] for symbol in letter.split("0")) for letter in word.split("000")) for word in decoded.strip().split("0000000"))


print(decode_bits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'))

#print(decode_bits('10101010001000111010111011100000001011101110111000101011100011101010001'))

#print(decode_bits('1110101110111'))

'''


#def get_generation(cells, generations):
#    iterations = 0
#    surround_count = prev_cells = new_cells = cells
#    while iterations < generations:
'''
    #adding a new row and column to previous grid
        for row in prev_cells:
            row.insert(0, 0)
            row.append(0)
            length = len(row)
        new_row = [0] * length
        prev_cells.insert(0, new_row)
        prev_cells.append(new_row)
        #adding a new row and column to new grid
        for row in new_cells:
            row.insert(0, 0)
            row.append(0)
            length = len(row)
        new_row = [0] * length
        prev_cells.insert(0, new_row)
        prev_cells.append(new_row)
        # and now the process
'''
'''
        for i in range(0, (len(prev_cells)-1)):
            for j in range(0, (len(prev_cells[i])-1)):
                if i == 0:
                    if j == 0:
                        surround_count[i][j] = prev_cells[0][1] + prev_cells[1][0] + prev_cells[1][1]
                    elif 0 < j < 2:
                        surround_count[i][j] = prev_cells[0][j-1] + prev_cells[0][j+1] + prev_cells[1][j-1] + prev_cells[1][j] + prev_cells[1][j+1]
                    elif j == 2:
                        surround_count[i][j] = prev_cells[0][j-1] + prev_cells[1][j-1] + prev_cells[1][j]
                elif 0 < i < (len(prev_cells)-1):
                    if j == 0:
                        surround_count[i][j] = prev_cells[i-1][0] + prev_cells[i-1][1] + prev_cells[i][1] + prev_cells[i+1][0] + prev_cells[i+1][1]
                    elif 0 < j < (len(prev_cells[1]) - 1):
                        surround_count[i][j] = prev_cells[0][0] + prev_cells[0][1] + prev_cells[0][2] + prev_cells[1][0] + prev_cells[1][2] + prev_cells[2][0] + prev_cells[2][1] + prev_cells[2][2]
                    elif j == (len(prev_cells[1]) - 1):
                        surround_count[i][j] = prev_cells[i-1][j - 1] + prev_cells[i-1][j] + prev_cells[i][j-1] + prev_cells[i+1][j-1] + prev_cells[i+1][j]
                elif i == (len(prev_cells)-1):
                    if j == 0:
                        surround_count[i][j] = prev_cells[i][j+1] + prev_cells[i-1][j] + prev_cells[i-1][j+1]
                    elif 0 < j < (len(prev_cells[1]) - 1):
                        surround_count[i][j] = prev_cells[i][j-1] + prev_cells[i][j+1] + prev_cells[i-1][j-1] + prev_cells[i-1][j] + prev_cells[i-1][j+1]
                    elif j == (len(prev_cells[1]) - 1):
                        surround_count[i][j] = prev_cells[i][j - 1] + prev_cells[i - 1][j - 1] + prev_cells[i - 1][j]
'''
'''
                        FROM HERE
                for i in range(0, (len(prev_cells)-1)):
            for j in range(0, (len(prev_cells[1])-1)):
                if i == 0:
                    if j == 0:
                        surround_count = prev_cells[i][j + 1] + prev_cells[i + 1][j] + prev_cells[i + 1][j + 1]
                    elif 0 < j < (len(prev_cells[1]) - 1):
                        surround_count = prev_cells[i][j-1] + prev_cells[i][j+1] + prev_cells[i+1][j-1] + prev_cells[i+1][j] + prev_cells[i+1][j+1]
                    elif j == len(prev_cells[1]) - 1:
                        surround_count = prev_cells[i][j - 1] + prev_cells[i + 1][j - 1] + prev_cells[i + 1][j]
                elif 0 < i < (len(prev_cells)-1):
                    if j == 0:
                        surround_count = prev_cells[i-1][j] + prev_cells[i-1][j+1] + prev_cells[i][j+1] + prev_cells[i+1][j] + prev_cells[i+1][j+1]
                    if 0 < j < len(prev_cells[1]) - 1:
                        surround_count = prev_cells[i-1][j-1] + prev_cells[i-1][j] + prev_cells[i-1][j+1] + prev_cells[i][j-1] + prev_cells[i][j+1] + prev_cells[i+1][j-1] + prev_cells[i+1][j] + prev_cells[i+1][j+1]
                    if j == len(prev_cells[1]) - 1:
                        surround_count = prev_cells[i-1][j - 1] + prev_cells[i-1][j] + prev_cells[i][j-1] + prev_cells[i+1][j - 1] + prev_cells[i+1][j]
                elif i == (len(prev_cells)-1):
                    if j == 0:
                        surround_count = prev_cells[i][j + 1] + prev_cells[i - 1][j] + prev_cells[i - 1][j + 1]
                    elif 0 < j < (len(prev_cells[1]) - 1):
                        surround_count = prev_cells[i][j-1] + prev_cells[i][j+1] + prev_cells[i-1][j-1] + prev_cells[i-1][j] + prev_cells[i-1][j+1]
                    elif j == len(prev_cells[1]) - 1:
                        surround_count = prev_cells[i][j - 1] + prev_cells[i - 1][j - 1] + prev_cells[i - 1][j]
                        UP TO HERE
                if i == 0 and j == 0:
                    surround_count = prev_cells[i][j + 1] + prev_cells[i + 1][j] + prev_cells[i + 1][j + 1]
                elif i == 0 and j != 0 and j < len(prev_cells[1]) - 1:
                    surround_count = prev_cells[i][j-1] + prev_cells[i][j+1] + prev_cells[i+1][j-1] + prev_cells[i+1][j] + prev_cells[i+1][j+1]
                elif i == 0 and j == len(prev_cells[1]) - 1:
                    surround_count = prev_cells[i][j - 1] + prev_cells[i + 1][j - 1] + prev_cells[i + 1][j]
                elif i > 0 and i < len(prev_cells) - 1 and j == 0:
                    surround_count = prev
                elif i == len(prev_cells) - 1 and j == 0:
                    surround_count = prev_cells[i-1][j] + prev_cells[i-1][j+1] + prev_cells[i][j + 1]
                elif i == len(prev_cells) - 1 and j != 0 and j < len(prev_cells[1]) - 1:
                    surround_count = prev_cells[i - 1][j - 1] + prev_cells[i - 1][j] + prev_cells[i - 1][j + 1] + prev_cells[i][j - 1] + prev_cells[i][j + 1]
                elif i == len(prev_cells) - 1 and j == len(prev_cells[1]) - 1:
                    surround_count = prev_cells[i - 1][j-1] + prev_cells[i - 1][j] + prev_cells[i][j-1]
                else:
                    surround_count = prev_cells[i-1][j-1] + prev_cells[i-1][j] + prev_cells[i-1][j+1] + prev_cells[i][j-1] + prev_cells[i][j+1] + prev_cells[i+1][j-1] + prev_cells[i+1][j] + prev_cells[i+1][j+1]
'''
'''
                if prev_cells[i][j] == 1:
                    if surround_count < 2:
                        new_cells[i][j] = 0
                    elif surround_count > 3:
                        new_cells[i][j] = 0
                elif prev_cells[i][j] == 0:
                    if surround_count == 3:
                        new_cells[i][j] = 1
'''
#        iterations += 1
#        #prev_cells = new_cells
#        #sum = prev_cells[0][1]
#    return prev_cells


#def surround_count(array):
    #length = len(array)
    #sublength = len(array[1])
    #surround = array[0][0] + array[0][1] + array[1][1] + array[2][0] + array[2][1]
    #return surround
    #answer = array[1][0] + array[0][0] + array[0][1] + array[1][1]
#    return surround

'''
def get_generation(cells, generations):
    prev_cells = cells
    surround_count = cells
    iterations = 0
    while iterations < generations:
        column_length = len(prev_cells)
        row_length = len(prev_cells[1])
        for i in range(column_length):
            for j in range(row_length):
                if i == 0:
                    if j == 0:
                        surround_count[i][j] = prev_cells[0][1] + prev_cells[1][0] + prev_cells[1][1]
                    elif 0 < j < 2:
                        surround_count[i][j] = prev_cells[0][j-1] + prev_cells[0][j+1] + prev_cells[1][j-1] + prev_cells[1][j] + prev_cells[1][j+1]
                    elif j == 2:
                        surround_count[i][j] = prev_cells[0][j-1] + prev_cells[1][j-1] + prev_cells[1][j]
                elif 0 < i < column_length-1:
                    if j == 0:
                        surround_count[i][j] = prev_cells[i-1][0] + prev_cells[i-1][1] + prev_cells[i][1] + prev_cells[i+1][0] + prev_cells[i+1][1]
                    elif 0 < j < row_length-1:
                        surround_count[i][j] = prev_cells[0][0] + prev_cells[0][1] + prev_cells[0][2] + prev_cells[1][0] + prev_cells[1][2] + prev_cells[2][0] + prev_cells[2][1] + prev_cells[2][2]
                    elif j == row_length-1:
                        surround_count[i][j] = prev_cells[i-1][j - 1] + prev_cells[i-1][j] + prev_cells[i][j-1] + prev_cells[i+1][j-1] + prev_cells[i+1][j]
                elif i == column_length-1:
                    if j == 0:
                        surround_count[i][j] = prev_cells[i][j+1] + prev_cells[i-1][j] + prev_cells[i-1][j+1]
                    elif 0 < j < row_length-1:
                        surround_count[i][j] = prev_cells[i][j-1] + prev_cells[i][j+1] + prev_cells[i-1][j-1] + prev_cells[i-1][j] + prev_cells[i-1][j+1]
                    elif j == row_length-1:
                        surround_count[i][j] = prev_cells[i][j-1] + prev_cells[i-1][j-1] + prev_cells[i-1][j]
        iterations += 1
    return prev_cells
'''
def clone(list):
    return list

start = [[1,0,0],
         [0,1,1],
         [1,1,0]]

#print(get_generation(start, 1))
#print(surround_count(start))

new = clone(start)

new[0][0] = start[0][1] + start[1][0] + start[1][1]
new[0][1] = start[0][0] + start[0][2] + start[1][0] + start[1][1] + start[1][2]

print(start)
print(new)