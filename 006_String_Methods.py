# 1) split() rsplit()
A= "i love football and-real-madrid"
print(A.split())  #['i', 'love', 'football', 'and-real-madrid']
print(A.rsplit("-",3)) #['i love football and', 'real', 'madrid']
# 2)center()
B= "Adham"
print(B.center(9,"#"))   ###Adham##
# 3)count()
C="I love real madrid and players of real madrid"
print(C.count("real"))    # 2
# 4)swapcase()
D= "AdHam OsAmA"
print(D.swapcase())  #aDhAM oSaMa
# 5)stareswith
E= "my name is adham osama"
print(E.startswith("m")) #True
print(E.startswith("n")) #False
# 6)endswith
F= "Hala madrid"
print(F.endswith("r")) #False
# 6)index(subString,start,end)
G= "adham osama"
print(G.index("a",1,9)) # 3
# 7)find(subString,start,end)
a="adham"
print(a.find("h"))  #2
# 8)rjust() ljust()
b="adham"
print(b.rjust(6,"#")) # [#adham]
print(b.ljust(6,"#")) #[adham#]
# 9)splitlines()
c="""1st line
2nd line
3rd line"""
print(c.splitlines())  #['1st line', '2nd line', '3rd line']
# 10)expandtabs()
d="adham\tosama\trashad"
print(d.expandtabs(5))  #adham     osama     rashad
# 11)istitle()
e="Adham Osama Rashad"
print(e.istitle())   #True
e="adham Osama Rashad"
print(e.istitle())  #False
