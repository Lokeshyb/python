def isScramble(S1: str, S2: str):
 if len(S1) != len(S2):
  return False
 n = len(S1)
 if not n:
  return True
 if S1 == S2:
  return True
 if sorted(S1) != sorted(S2):
  return False
 for i in range(1, n):  
  if (isScramble(S1[:i], S2[:i])and isScramble(S1[i:], S2[i:])):
      if (isScramble(S1[-i:], S2[:i]) and isScramble(S1[:-i], S2[i:])):
          return True
 return False
S1 = input()
S2 = input()
if (isScramble(S1, S2)):
    print("true")
else:
    print("false")

