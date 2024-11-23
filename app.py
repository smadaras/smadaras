import os
import js
from js import document
     
def main():
    msg = document.getElementById("msg")
    msg.innerHTML = 'Hello world alert secret'
    print(f"Current working directory: {os.getcwd()}")
    print(f"Environment: {os.getenv('ENV_SEC')}")
    print(f"Static: {os.getenv('url')}")
       
main()
