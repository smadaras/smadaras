import os
import js
from js import document
     
def main():
    msg = document.getElementById("msg")
    msg.innerHTML = 'Hello world with param'
    print(f"Current working directory: {os.getcwd()}")
    print(f"Environment: {os.getenv('ENV_VAR')}")
    print(f"Static: {os.getenv('url')}")
       
main()
