from datetime import datetime as dt

class Logger: 
    def logger(text):
        time = dt.now()
        with open('s9/log.txt','a') as file:
            file.write(f'{time}: {text}\n')