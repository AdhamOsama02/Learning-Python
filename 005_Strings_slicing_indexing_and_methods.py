# 1) Indexing ( Access Single Item )
My_String = "I Love Python"
print(My_String[0]) #1st item (I)
print(My_String[7]) #7th item (P) 
print(My_String[-1]) #1st item from the end (n)
print(My_String[-5]) #5th item from the end (y)

# 2) Slicing ( Access Multiple Sequence Items )
# [start:end] end not included
# [start:end:steps]
print(My_String[0:4]) # (I Lo)
print(My_String[0:]) # (I Love Python)
print(My_String[:7]) #(I Love)
print(My_String[:]) #(I Love Python)
print(My_String[0::2]) #(ILv yhn)

# 3) String Methods
# a)len [the number of characters]
A = "adham osama"
print(len(A))
# b) strip(),rstrip(),lstrip()    [remove the spaces]
B = "     adham osama      "
print(B.strip())  ;print(B.rstrip())  ;print(B.lstrip()) 
# c) titel [make the fist letter of each word in upper case]
C = "i love 2d graphics and 3d graphics and python"
print(C.title())
# d) capitalize [make the 1st word in sentence in upper case]
D = "real madrid"
print(D.capitalize())
# e) upper [make all letters in upper case]
E = "adham"
print(E.upper())
# f) lower [make all letters in lower case]
F = "OSAMA"
print(F.lower())
# g) zfill
G = "1"   ;print(G.zfill(3))
