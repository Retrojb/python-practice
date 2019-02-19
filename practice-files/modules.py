import webbrowser
from random import choice
from time import time as time_now

#just opens this website from inside the code. could be useful when wanting to launch a webpage on the opening of
#an application.
#webbrowser.open('https://google.com')

shapes = choice(['square', 'circle', 'trapazoid', 'triangle', 'rectangle', 'rhombus'])

current_time = time_now()
print(f'At {current_time}, there is a {shapes} siting on the door step')