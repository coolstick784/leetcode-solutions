class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        employees = {}
        for emp, time in access_times:
            employees.setdefault(emp, []).append(int(time))
        res = []
        
        for e in employees:
            len_emp = len(employees[e])
            employees[e].sort()
            emp = employees[e]
            print("e", e)
            print("emp", emp)
            print("len", len_emp)
            if len_emp < 3:
                continue
            left = 0
            right = 2
            right_val = emp[right]
            left_val = emp[left]      
            while (right_val - left_val >= 100 or right-left < 2) and left < len_emp - 2:

                right_val = emp[right]
                left_val = emp[left]  
                if right_val - left_val >= 100:      
                    left += 1
                else:
                    right = min(right+1, len_emp-1)
                
                right_val = emp[right]
                left_val = emp[left]  
            right = min(right, len_emp -1)
            print("right", right)
            print("left", left)


            if right-left >= 2 and emp[right] - emp[left] < 100:
                res.append(e)
        return res


