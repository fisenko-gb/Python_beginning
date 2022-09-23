import operator

OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

def calc(srt):
    stack = []
    for i in srt:
        if i.isdigit():
            stack.append(i)
        else:
            if i == '~':
                cnt1 = stack.pop()
                stack.append(0 - int(cnt1))
                print('0-' + str(cnt1))
            else:
                cnt1 = stack.pop()
                cnt2 = stack.pop()
                print(str(cnt2) + i + str(cnt1))
                stack.append(OPERATORS[i](int(cnt2), int(cnt1)))


    return stack.pop()

def getoutputLine(line):
    outputLine = ''
    stack = []
    j = 0

    for i in line:
        nextOperator = ''
        if len(line) > j+2:
            nextOperator = line[j+2]

        if i.isdigit():
            outputLine +=i
        else:
            if i == '-' and \
                    (nextOperator == '('
                     or nextOperator == '+'
                     or nextOperator == '-'
                     or nextOperator == '*'
                     or nextOperator == '/') != 0:

                if len(stack) != 0:
                    lastItem = stack.pop()
                    if lastItem == '~':
                        outputLine += lastItem
                    else:
                        stack.append(lastItem)

                stack.append('+')
                stack.append('~')

            elif i == '(':
                stack.append(i)
            elif i == '-' or i == '+':

                if len(stack) != 0:
                    lastItem = stack.pop()
                    if lastItem == '*' \
                            or lastItem == '/' \
                            or lastItem == '~':
                        outputLine += lastItem
                    else:
                        stack.append(lastItem)

                stack.append(i)
            elif i == '*' or i == '/':
                if len(stack) != 0:
                    lastItem = stack.pop()
                    if lastItem == '*' \
                            or lastItem == '/' \
                            or lastItem == '~':
                        outputLine += lastItem
                    else:
                        stack.append(lastItem)
                stack.append(i)
            elif i == ')':

                for item in reversed(stack):
                    if item == '(':
                        stack.pop()
                    else:
                        outputLine += item
                        stack.pop()
        j+=1

    for item in reversed(stack):
        outputLine += item

    return outputLine

# for test
#line = '3+4*2/(1-5)'
#line = '(1-1+1)'
#line = '9-9-5-5'
#line = '2*2-1'
line = '2+3-1*((7-3)*3-6)-7*2+3*2'

print(line)
print('------------------------')

outputLine = getoutputLine(line)
print(outputLine)

result = calc(outputLine)
print('right result: ' + str(eval(line))
      + '\nalgoritm result: ' + str(result))





