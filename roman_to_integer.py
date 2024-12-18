
symbol = {"I":1,
          "V":5,
          "X":10,
          "L":50,
          "C":100,
          "D":500,
          "M":1000}

s = "MCMXCIV"


def romanToInt(s):
    n = len(s)
    total = 0
    for i in range(n):
        if i < n-1 and symbol[s[i]] < symbol[s[i+1]]:
            total -= symbol[s[i]]
        else:
            total += symbol[s[i]]
    return total 

print(romanToInt(s))

