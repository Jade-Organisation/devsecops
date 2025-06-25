import os 
import hashlib
import subprocess

user_input = input("Enter a file name")
os.system(f"cat {user_input}")

password = "supersecret"
hash = hashlib.md5(password.encode()).hexdigest()

subprocess.call("ls " + user_input, shell=True)