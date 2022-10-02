import os                # This is used for system function
import math          # The math library
import random     # For random numbers
import smtplib      # For email functions
import socket

num = "0123456789"
val = ""
for i in range(0,6):
    val = val + num[math.floor(random.random()*10)]
OTP = val + " is your One-Time-Password for verification"
message = OTP
socket.getaddrinfo('localhost',25)
email = smtplib.SMTP('smtp.gmail.com', 587)  # To call the gmail account client
email.starttls()
email.login("crypt.text.11022@gmail.com", "ssjokvljlgcywfsl")  # To login into your account successfully
id = input("Enter your email address : ")
email.sendmail('&&&&&&&&&&&', id, message)  # Sending the OTP email
x = input("Enter your One-Time-Password ~~> :  ")
if x == val :
    print(" Your account has been successfully verified  ")
else:
    print("Please check your OTP once again ")
