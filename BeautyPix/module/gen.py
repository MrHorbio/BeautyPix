#This file will generate otps 6 digit,4 digit,5 digit, 8 digit also alphanumeric 
import random


def length_of_file(file):
     # Read the file and count the number of lines using len()
        with open(file, "r") as f:  # Open the file in read mode
            otp_lines = f.readlines()  # Read all lines into a list
            otp_count = len(otp_lines)  # Use len() to count the number of lines
        print(f"Total OTPs generated and stored in {file}: {otp_count}")




def gen():
    print("Number of digits: \n 1. 4 digit \n 2. 5 digit \n 3. 6 digit \n 4. 8 digit  \n [press 1 ,2 ,3 or 4 ] ")
    num = input("Enter the number: ")
    print(f"YOU INPUT IS  {num}")

    if num == "1" :
        file="4_digit_OTP"
        for i in range(0000,10000):
            padded_number = str(i).zfill(4) 
            print(padded_number)
            with open(file,"a") as f:
                f.write(padded_number + "\n")
        length_of_file(file)
        print(f"OTP STORE IN {file}")

    elif num == "2": 
        file="5_digit_OTP"
        for i in range(00000,100000):
            padded_number = str(i).zfill(5) 
            print(padded_number)
            with open(file,"a") as f:
                f.write(padded_number + "\n")
        length_of_file(file)
        print(f"OTP STORE IN {file}")
                
    elif num == "3": 
        file="6_digit_OTP"
        for i in range(000000,1000000):
            padded_number = str(i).zfill(6) 
            print(padded_number)
            with open(file,"a") as f:
                f.write(padded_number + "\n")
        length_of_file(file)
        print(f"OTP STORE IN {file}")    


    elif num == "4": 
        file="8_digit_OTP"
        for i in range(00000000,10000000):
            padded_number = str(i).zfill(8) 
            print(padded_number)
            with open(file,"a") as f:
                f.write(padded_number + "\n")
        length_of_file(file)
        print(f"OTP STORE IN {file}")
        
    else:
        print("Enter right number")
        


gen()