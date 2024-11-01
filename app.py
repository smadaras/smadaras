import js
from js import document
     
def main():
    msg = document.getElementById("msg")
    msg.innerHTML = 'Hello world'
    print("It's python.")
       
main()