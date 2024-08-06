string_input = str(input("Enter a string here !"))
sum=0
count=0
for i in string_input:
  #print(ord(string_input[i]))
  sum+=ord(i)
  count+=1
print("Sum of Characters in String :{}\nCount:{} ".format(sum,count))