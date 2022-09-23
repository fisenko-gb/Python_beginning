import sys

def solve(vr):
    st = []
    for w in vr:
        if w.isdigit(): # если он чис
            st.append(int(w))
            continue # возвращаемся на проверку условия

        y = st.pop() # берем первое число в списке

        x = st.pop() # второе число в списке

        z = {

            '+': lambda x, y: x + y,

            '-': lambda x, y: x - y,

            '*': lambda x, y: x * y,

            '/': lambda x, y: x // y }[w](x, y)

        st.append(z)

    return st.pop()

vr = '2*2-1'

print(solve(vr))