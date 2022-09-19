#get userr input
answer = input("greeting")

new_answer = answer.lower().strip()

#check if the answer ha "hello", print 0
if 'hello' in new_answer:
    print("$0")


#chek if answer starts with 'h', print 20
elif 'h' == new_answer[0] :
    print("$20")

#otherwise, print 100
else:
    print("$100")