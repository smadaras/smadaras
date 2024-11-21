import os
import js
from js import document
     
def main():
    msg = document.getElementById("msg")
    msg.innerHTML = 'Hello world with workflow'
    print(f"Current working directory: {os.getcwd()}")
       
main()
