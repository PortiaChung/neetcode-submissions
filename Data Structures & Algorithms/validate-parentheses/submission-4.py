class Solution:
    def isValid(self, s: str) -> bool:
        valid = {")":"(", "}":"{", "]":"["}
        st = []
        for x in s:
            if x in valid:
                if st and st[-1] == valid[x]:
                    st.pop()
                else:
                    return False
            else:
                st.append(x)
        return len(st)==0