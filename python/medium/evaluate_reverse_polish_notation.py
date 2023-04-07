class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if token == "+":
                st.append(st.pop() + st.pop())
            elif token == "-":
                v1 = st.pop()
                v2 = st.pop()
                st.append(v2 - v1)
            elif token == "*":
                st.append(st.pop() * st.pop())
            elif token == "/":
                v1 = st.pop()
                v2 = st.pop()
                st.append(int(v2 / v1))
            else:
                st.append(int(token))
        return st[-1]
