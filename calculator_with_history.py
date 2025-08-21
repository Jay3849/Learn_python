History_file="history.txt"


def show_history():
    
    file=open(History_file,'r')
    lines=file.readlines()
    if len(lines)==0:
        print("history not found file was empty ")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()
    
def history_clear():
    file=open(History_file,'w')
    file.close()
    print("History cleared...")
    
def save_history(equatiuon,result):
    file=open(History_file,'a')
    file.write(equatiuon + "=" + str(result)+"\n")
    file.close()
    
def calculate(user_input):
    parts=user_input.split()
    if len(parts)!=3:
        print("Invalid Input use Formate : num operator num [2 + 2 ]")
        return
    
    num1=float(parts[0])
    op=parts[1]
    num2=float(parts[2])
    
    if op=="+":
        result=num1+num2
    elif op=="-":
        result=num1-num2
    elif op=="*":
        result=num1*num2
    elif op=="/":
        if num2==0:
            print("can not divided by zero")
            return
        result=num1/num2
           
    else:
        
        print("Invalid operation try againn!!!")
        return
    if int(result)==result:
        result=int(result)
        
    print("Result : ",result)

    save_history(user_input,result)
    
def main ():
    print("----simple calculator----")
    
    while True:
        
        user_input=input("Enter calculation(+,-,*,/) or command [exit,history,clear]: ")
        
        if user_input=="exit":
            print("good by hava a nice day ")
            
        elif user_input=="clear":
            history_clear()
        
        elif user_input=="history":
            show_history()
        else :
            calculate(user_input)
        
        
main()
    
        
            
            
    
    
    