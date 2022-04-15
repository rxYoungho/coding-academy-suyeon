s = "23four5six7"

def solution(s):
    one = s.replace("one", '1')
    two = one.replace("two", '2')
    three = two.replace("three", '3')
    four = three.replace("four", '4')
    five = four.replace("five", '5')
    six = five.replace("six", '6')
    seven = six.replace("seven", '7')
    eight = seven.replace("eight", '8')
    nine = eight.replace("nine", '9')
    zero = nine.replace("zero", '0')
    print(s)
    answer = int(zero)

    return answer

print(solution(s))