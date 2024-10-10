
# 1. WRITE A PROGRAMME TO FIND A SUM OF ALL THE EVEN NUMBER UP TO 50:
sum = 0
for i in range(1,51):
    if i %2==0:
        sum += i
print(sum)


# 2. WRITE A PROGRAM TO WRITE FIRST 20 NUMBER AND THEIR SQUARE NUMBER:
for i in range(1,21):
    print(i,i**2)


# 3. WRITE A PROGRAM TO FIND THE SUM OF FIRST 10 ODD NO USING WHILE LOOP:
sum =0
n=0
while n<=20:
    if n%2!=0:
        sum +=n
        n+=1
print(sum)

# 4. WRITE A PROGRAM TO CHECK IF A NUMBER IS DIVISIBLE BY 8 AND 12, UP TO 100 NUMBERS:
for i in range(1,101):
    if i%8==0 and i%12==0:
        print(i)

# 5. WRITE A PROGRAM TO CREATE A BILLING SYSTEM AT SUPERMARKET:
while True:
    name = input("Enter customer's name: ")
    total = 0

    while True:
        print("enter the amount and quantity")
        amount = float(input("enter amount: "))
        quantity = float(input("enter quantity: "))
        total += amount * quantity
        repeat = input("Do you want to repeat?(y/n): ")
        if repeat =="no" or repeat =="NO":
            break
    print ("-"*40)
    print ("Name: ",name)
    print("Amount to be paid: ",total)
    print("-" * 40)
    print("**********Happy Shopping**********")
    repeat1 = input("Do you want to go to next customer?(y/n): ")
    if repeat1 =="no" or repeat1 =="NO":
        break



