import eel
 
 
@eel.expose
def return_hello():
    return "Hello!!"
 
 
def start_gui():
    eel.init('web')
    #eel.start('index.html')
    eel.start('index.html',mode='chrome-app')
 
 
if __name__ == "__main__":
    start_gui()
