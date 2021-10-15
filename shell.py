import wonkmy

while True:
    text=input('basic > ')
    
    result,error=wonkmy.run('<shell.py>',text)

    if error:print(error.as_string())
    else: print(result)