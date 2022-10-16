#Q1/Write a method that will remove any given character from a String?
#Ans
m=''
x=input('Enter the character that you want to remove from the String: ')
s="Hello world"
m=s.replace(x,'')
#in this example we use to remove (l) letterprint(m)
print('the original string: ',s)
print('the updated string:  ',m)
