class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {"+","-","*","/"}
        st = []
        for t in tokens:
            print(t)
            if st and t in op:
                y = st.pop()
                x = st.pop()
                if t == "+":
                    z = x+y
                elif t == "-":
                    z = x-y
                elif t == "*":
                    z = x*y
                elif t == "/":
                    z = int(x/y)
                st.append(z)
            else:
                st.append(int(t))
        return st[-1]
          