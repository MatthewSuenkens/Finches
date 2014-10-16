from finch import Finch
from time import sleep


finch = Finch()

print (finch.light())

while (1) :
    light = finch.light()
    average = (light[0] + light[1]) / 2
    deviation = abs(average - 0.55)

    #formula using deviation so finch could react appropriately to light
    #3 is for a stronger reaction because 1 standard deviation not enough
    finch.led(255 * 3 * deviation, 255 * 3 * (1 - deviation), 0)
    print (average)
    
