#Fehrenhite = 40
#Celsuis = 5/9*(Fehrenhite - 32)
#print(Celsuis)

# seconds = 2400
# hours = seconds/3600
# minutess = seconds % 3600
# print(hours)
# minutes= hours *60
# print(minutess)
# hour =seconds/3600
# minutes = seconds/60

# num = 10000
# hour = num // 3600
# hour1 = num % 3600
# minute =  hour1 // 60
# seconds = hour % 60
# print(hour ,"hour" ,":" ,minute ,"minutes" ,":" ,seconds ,"second")




# Question1
# raduis = int(input('Enter The raduis number'))
# area = 3.14*(raduis**2)
# print('Area is:',area)




# Question 2
# ax**2+bx+c=0

# a = int(input('Enter a'))
# b = int(input('Enter b'))
# c = int(input('Enter c'))

# x1 = -b + ((b**2 - 4*a*c)*.5)/(2*a)
# x2 = -b - ((b**2 - 4*a*c)*.5)/(2*a)

# print('value 1:', x1, ',', 'value 2' , x2)









# Question 3
# length function here
# def StringLength(list):
#     counter = 0
#     for item in list:
#         counter += 1
#     return counter
# list input here
# listt = []
# list = input('Enter the List')
# list.append()
# print('The length of the list is :',StringLength([2,3,4,'amal']))
#




#print(min([2,3,-9,-5]))
#print(min(2,4,-9,-5))






# list
list1 = [0,1,2,3,4,5,6]
# list1[1:1] = [20,30]
# del list1[0]
# list1[0]=[]
# list1[:2]=[]
# list1[2]=90
# list1.append(7)
# tuple = (0,1,2,3,4,5,6)
# tuple[0]=30
# length=len(list1)
# print(list1)

dictionary = {
    'name':'amal',
    'age':20,
    'city':'Rafah',
    'jobTitle':'Developer'
}
# dict2={}
# dict2['name']='aml'
# dict2['age']= 21
# del dict2['name']
# print(dict2)
# print(dictionary.clear())



# example

# num = int(input('Enter The Number'))
# print ('Even Number')if num%2 ==0 else print('Odd Number')


# Q1
# userList = input('Enter the value')
# list = []
# len = 0
#
# while userList != 'End':
#     list.append(userList)
#     userList  = input('Enter the next value')
#     len +=1
# print(list)
# print(len)


# Q2
# num1 = int(input('Enter the first number'))
# num2 = int(input('Enter the second number'))
# num3 = int(input('Enter the third num'))
#
# if num1 == num2 or num1 == num3 or num2 == num3 :
#     print('Duplicated numbers')
# else:
#     print('unique number')


# Q3
# def smallestNum(fNum, sNum, thNum):

    # fNum = int(input('Enter the first number'))
    # sNum = int(input('Enter the second number'))
    # thNum = int(input('Enter the third num'))

    # if fNum<sNum and fNum<thNum:
    #     print('The smallest number is :', fNum)
    # elif sNum<fNum and sNum<thNum:
    #     print('The smallest number is :', sNum)
    # elif thNum<fNum and thNum<sNum:
    #     print('The smallest number is :', thNum)
    # else:
    #     print('There is at least two number equal')
#
# smallestNum(int(input('Enter the first number')), int(input('Enter the second number')), int(input('Enter the third num')))



# Q4
def averageNumber():
    number = int(input('Enter the number'))
    numbersList = []


    total =0
    negative= 0
    positive = 0
    count = 0

    while number != 0 :
        numbersList.append(number)
        if number == 0:
            continue
        elif number > 0:
            positive += 1
        elif number < 0:
            negative+=1
        count += 1
        total += number
        number = int(input('Enter the number'))

    print('The number of positive numbers are: ', positive)
    print('The number of negative numbers are:', negative)
    print('The total is:', total)
    print('The average is:', total/count)

averageNumber()




















