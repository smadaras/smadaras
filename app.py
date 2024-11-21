import os
import js
from js import document
     
def main():
    msg = document.getElementById("msg")
    msg.innerHTML = 'Hello world with getenv'
    print(f"Current working directory: {os.getcwd()}")
    print(f"Environment: {os.getenv('env_var')}")
       
main()
