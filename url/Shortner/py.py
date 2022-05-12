import pyshorteners
a = input("x")
shor = pyshorteners.Shortener()
print (shor.tinyurl.short(a))