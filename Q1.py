def is_balanced(s:str):
    s= s.lstrip()
    s=s.rstrip()
    stack = []
    mapping = {')': '(',
               '}': '{',
               ']': '['
            }
    
 
    for bracket in s:
        
        if bracket in mapping.values():
            stack.append(bracket)
        
        elif bracket in mapping:
            if not stack or stack.pop() != mapping[bracket]:
                return "NO"
    
    return "YES" if not stack else "NO"

user_input = input("Brackets: ")
print(is_balanced(user_input))