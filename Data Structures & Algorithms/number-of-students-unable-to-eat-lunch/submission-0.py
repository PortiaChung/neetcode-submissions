class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s = deque(students)
        n = len(students)
        res = n
        for sw in sandwiches:
            cnt = 0
            while cnt < n and s[0]!= sw:
                cnt+=1
                s.append(s.popleft())
            if s[0] == sw:
                res-=1
                s.popleft()
            else:
                break
        return res            
        