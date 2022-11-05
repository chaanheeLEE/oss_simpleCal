from calculate import *
import logging

#계산기록 남기는 로그파일 생성
logger_cal = logging.getLogger("calculation_history")
logger_cal.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
calculation_log = logging.FileHandler('calculation.log')
calculation_log.setFormatter(formatter)
logger_cal.addHandler(calculation_log)

#비정살 루틴 사용 기록 남기는 로그파일 생성
logger_abnoraml = logging.getLogger("abnoraml")
logger_abnoraml.setLevel(logging.DEBUG)
abnormal_log = logging.FileHandler('abnormal.log')
abnormal_log.setFormatter(formatter)
logger_abnoraml.addHandler(abnormal_log)

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
            logger_cal.debug(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
            logger_cal.debug(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
            logger_cal.debug(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice =='4':
            if(num2==0):
                print("ZeroDivisionError")
                logger_abnoraml.warning("ZeroDivisionError")
            else:
                print(num1, "/", num2, "=", divide(num1, num2))
                logger_cal.debug(f"{num1} / {num2} = {divide(num1, num2)}")

            

        # check if user wants another calculation
        # break the while loop if answer is no
        quest()

    else:
        print("Invalid Input")
        logger_abnoraml.warning("Invalid Input")
        
