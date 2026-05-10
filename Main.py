import time
import sched
s = sched.scheduler(time.time, time.sleep)
import turtle
# times = open('traveltimes', 'w')
planets = ['Sun', 'Mercury', 'Venus','Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto', 'test']

######### THIS IS A DICTIONARY - READ YOU IDIOT
distances = {'Sun': 0, 'Mercury':0.000006123880620837039, 'Venus': 0.000011397222266557821, 'Earth': 0.00001582002493716235, 'Mars': 0.000024155306893301653, 'Jupiter': 0.00008233217279125351, 'Saturn': 0.0001505453985955772, 'Uranus': 0.0003027918751413869, 'Neptune': 0.00047460074811487044, 'Pluto': 0.000456308, 'test': 1.0}
#########

lastinput = []
# , 'Mercury to Venus': 46550000, 'Mercury to Earth': 137000000, 'Mercury to Mars': 180300000, 'Mercury to Jupiter': 458900000, 'Mercury to Saturn': 913100000, 'Mercury to Uranus': 1878000000, 'Mercury to Neptune': 2797000000, 'Mercury to Pluto': 3139000000}
seconds = 0
Time = 0
hours = 0
minutes = 0
with open("traveltimes.txt", 'a+') as times:
    times.write('You have traveled to: ')
    times.close()
while True:
    turtle.register_shape('lightspeed.gif')
    coordinates = input('''
Where would you like to go? 
Use proper case please.
Type Orbit to exit. ''')
    if coordinates == 'Orbit':
        with open ('traveltimes.txt', 'a+') as times:
            times.write('\n')
            times.close
        break
    def seconds(seconds):
        seconds = Time()
        seconds -= 1
        return seconds
    def Time():
        Time = 50855.08 * distances[coordinates] * 10
        return Time
    def hours():
        hours = Time()/24
        return hours
    def minutes():
        minutes = hours/60
        return minutes
    def exit():
        while True:
            while timeses >= 1:
                if timeses > 10:
                    skip = input("That will take longer than 60 seconds, would you like to skip to the end? ")
                    if skip == 'Yes':
                        space.setup(500,500)
                        turtle.shape("lightspeed.gif")
                        time.sleep(0.5)
                        space.setup(470,330)
                        turtle.shape('Mercury.gif')
                        print(f"You have arrived at {coordinates}")
                        break
                    elif skip == 'No':
                        continue
                turtle.shape('lightspeed.gif')
                space.setup(500,500)
                timeses -= 1
                time.sleep(1)
                while timeses < 1:
                    exit = input('Would you like to exit hyperspace? ')
                    if exit == 'Yes':
                        space.setup(600,530)
                        turtle.shape('Mercury.gif')
                        print(f"You have arrived at {coordinates}")
                        break
                    elif exit == 'No':
                        while timeses < 1:
                            print("You've reached your destination, you must exit now")
                            exit
                            break
                else:
                    print("Approaching destination")
                    print(f'{round(timeses, 3)} seconds left' )
                    continue
            break
    if planets.count(coordinates) > 0:
        hours = hours()
        # def exit():
        #   timeses = Time()
        timeses = Time()
        # hours = hours()
        if coordinates == planets[0]:
            space = turtle.Screen()
            turtle.register_shape('Sun.gif')
            space.setup(500,500)
            print(f'That will take {Time()} seconds')
            time.sleep(round(Time(), 3))
            turtle.shape('Sun.gif')
            with open ('traveltimes.txt', 'a+') as times:
                times.write(coordinates)
                times.write(',')
                times.close()
        elif coordinates == planets[1]:
            with open ('traveltimes.txt', 'a+') as times:
                times.write(coordinates)
                times.write(',')
                times.close()
            millennium_falcon = turtle.Turtle()
            lastinput.append(coordinates)
            space = turtle.Screen()
            turtle.register_shape('Mercury.gif')
            lightspeed = turtle.Turtle()
            print(f'That will take {round(Time(), 3)} seconds')
            while True:
                while timeses >= 1:
                    if timeses > 10:
                        skip = input("That will take longer than 60 seconds, would you like to skip to the end? ")
                        if skip == 'Yes':
                            space.setup(500,500)
                            turtle.shape("lightspeed.gif")
                            time.sleep(0.5)
                            space.setup(470,330)
                            turtle.shape('Mercury.gif')
                            print(f"You have arrived at {coordinates}")
                            break
                        elif skip == 'No':
                            continue
                    turtle.shape('lightspeed.gif')
                    space.setup(500,500)
                    timeses -= 1
                    time.sleep(1)
                    while timeses < 1:
                        exit = input('Would you like to exit hyperspace? ')
                        if exit == 'Yes':
                            space.setup(600,530)
                            turtle.shape('Mercury.gif')
                            print(f"You have arrived at {coordinates}")
                            break
                        elif exit == 'No':
                            while timeses < 1:
                                print("You've reached your destination, you must exit now")
                                exit
                                break
                    else:
                        print("Approaching destination")
                        print(f'{round(timeses, 3)} seconds left' )
                        continue
                break
                # lightspeed.hideturtle()
                # millennium_falcon.hideturtle()
        elif coordinates == planets[2]:
            with open ('traveltimes.txt', 'a+') as times:
                times.write(coordinates)
                times.write(',')
                times.close()
            turtle.register_shape('Venus.gif')
            millennium_falcon = turtle.Turtle()
            space = turtle.Screen()
            print(f'That will take {round(Time(), 3)} seconds')
            while True:
                while timeses >= 1:
                    if timeses > 10:
                        skip = input("That will take longer than 60 seconds, would you like to skip to the end? ")
                        if skip == 'Yes':
                            space.setup(500,500)
                            turtle.shape("lightspeed.gif")
                            time.sleep(0.5)
                            space.setup(470,330)
                            turtle.shape('Venus.gif')
                            print(f"You have arrived at {coordinates}")
                            break
                        elif skip == 'No':
                            continue
                    turtle.shape('lightspeed.gif')
                    space.setup(500,500)
                    timeses -= 1
                    time.sleep(1)
                    while timeses < 1:
                        exit = input('Would you like to exit hyperspace? ')
                        if exit == 'Yes':
                            space.setup(600,530)
                            turtle.shape('Venus.gif')
                            print(f"You have arrived at {coordinates}")
                            break
                        elif exit == 'No':
                            while timeses < 1:
                                print("You've reached your destination, you must exit now")
                                exit
                                break
                    else:
                        print("Approaching destination")
                        print(f'{round(timeses, 3)} seconds left' )
                        continue
                break
        elif coordinates == planets[3]:
            with open ('traveltimes.txt', 'a+') as times:
                times.write(coordinates)
                times.write(',')
                times.close()
            millennium_falcon = turtle.Turtle()
            space = turtle.Screen()
            turtle.register_shape('Earth.gif')
            print(f'That will take {round(Time(), 3)} seconds')
            while True:
                while timeses >= 1:
                    if timeses > 10:
                        skip = input("That will take longer than 60 seconds, would you like to skip to the end? ")
                        if skip == 'Yes':
                            space.setup(500,500)
                            turtle.shape("lightspeed.gif")
                            time.sleep(0.5)
                            space.setup(470,330)
                            turtle.shape('Earth.gif')
                            print(f"You have arrived at {coordinates}")
                            break
                        elif skip == 'No':
                            continue
                    turtle.shape('lightspeed.gif')
                    space.setup(500,500)
                    timeses -= 1
                    time.sleep(1)
                    while timeses < 1:
                        exit = input('Would you like to exit hyperspace? ')
                        if exit == 'Yes':
                            space.setup(600,530)
                            turtle.shape('Earth.gif')
                            print(f"You have arrived at {coordinates}")
                            break
                        elif exit == 'No':
                            while timeses < 1:
                                print("You've reached your destination, you must exit now")
                                exit
                                break
                    else:
                        print("Approaching destination")
                        print(f'{round(timeses, 3)} seconds left' )
                        continue
                break
        elif coordinates == planets[4]:
            with open ('traveltimes.txt', 'a+') as times:
                times.write(coordinates)
                times.write(',')
                times.close()
            turtle.register_shape('Mars.gif')
            millennium_falcon = turtle.Turtle()
            space = turtle.Screen()
            # print('Attempt_at_lightspeed.gif')
            space.setup(500,500)
            turtle.shape('lightspeed.gif')
            print(f'That wil take {round(Time(), 3)} seconds')
            while True:
                while timeses >= 1:
                    if timeses > 60:
                        skip = input("That will take longer than 60 seconds, would you like to skip to the end? ")
                        if skip == 'Yes':
                            space.setup(500,500)
                            turtle.shape("lightspeed.gif")
                            time.sleep(0.5)
                            space.setup(470,330)
                            turtle.shape('Mars.gif')
                            print(f"You have arrived at {coordinates}")
                            break
                        elif skip == 'No':
                            continue
                    turtle.shape('lightspeed.gif')
                    space.setup(500,500)
                    timeses -= 1
                    time.sleep(1)
                    while timeses < 1:
                        exit = input('Would you like to exit hyperspace? ')
                        if exit == 'Yes':
                            space.setup(600,530)
                            turtle.shape('Mars.gif')
                            print(f"You have arrived at {coordinates}")
                            break
                        elif exit == 'No':
                            while timeses < 1:
                                print("You've reached your destination, you must exit now")
                                exit
                                break
                    else:
                        print("Approaching destination")
                        print(f'{round(timeses, 3)} seconds left' )
                        continue
                break
        elif coordinates == planets[5]:
            with open ('traveltimes.txt', 'a+') as times:
                times.write(coordinates)
                times.write(',')
                times.close()
            millennium_falcon = turtle.Turtle()
            space = turtle.Screen()
            turtle.register_shape('Jupiter.gif')
            print(f'That will take {round(hours, 3)} hours')
            # print('Attempt_at_lightspeed.gif')
            while hours > 1:
                if hours > 1:
                    skip = input("That will take longer than an hour, would you like to skip to the end? ")
                    if skip == 'Yes':
                        space.setup(500,500)
                        turtle.shape("lightspeed.gif")
                        time.sleep(0.5)
                        space.setup(600,530)
                        turtle.shape('Jupiter.gif')
                        print(f"You have arrived at {coordinates}")
                        break
                    elif skip == 'No':
                        while True:
                            while hours >= 1:
                                turtle.shape('lightspeed.gif')
                                space.setup(500,500)
                                hours -= 1
                                time.sleep(1)
                                while hours < 1:
                                    exit = input('Would you like to exit hyperspace? ')
                                    if exit == 'Yes':
                                        space.setup(600,530)
                                        turtle.shape('Jupiter.gif')
                                        print(f"You have arrived at {coordinates}")
                                        break
                                    elif exit == 'No':
                                        while hours < 1:
                                            print("You've reached your destination, you must exit now")
                                            exit
                                            break
                                else:
                                    print("Approaching destination")
                                    print(f'{round(hours, 3)} seconds left' )
                                    continue
                            break
                    else:
                        print("That is not a valid response, please try again.")
                        skip
                        continue
                break
        elif coordinates == planets[6]:
            with open ('traveltimes.txt', 'a+') as times:
                times.write(coordinates)
                times.write(',')
                times.close()
            turtle.register_shape('Saturn.gif')
            millennium_falcon = turtle.Turtle()
            space = turtle.Screen()
            print(f'That will take {round(hours, 3)} hours')
            # print('Attempt_at_lightspeed.gif')
            while True:
                if hours > 1:
                    skip = input("That will take longer than 20 seconds, would you like to skip to the end? ")
                    if skip == 'Yes':
                        space.setup(500,500)
                        turtle.shape("lightspeed.gif")
                        time.sleep(0.5)
                        space.setup(600,530)
                        turtle.shape('Saturn.gif')
                        print(f"You have arrived at {coordinates}")
                        break
                    elif skip == 'No':
                        while True:
                            while hours >= 1:
                                turtle.shape('lightspeed.gif')
                                space.setup(500,500)
                                hours -= 1
                                time.sleep(1)
                                while hours < 1:
                                    exit = input('Would you like to exit hyperspace? ')
                                    if exit == 'Yes':
                                        space.setup(600,530)
                                        turtle.shape('Saturn.gif')
                                        print(f"You have arrived at {coordinates}")
                                        break
                                    elif exit == 'No':
                                        while timeses < 1:
                                            print("You've reached your destination, you must exit now")
                                            exit
                                            break
                                else:
                                    print("Approaching destination")
                                    print(f'{round(hours, 3)} hours left' )
                                    continue
                            break
                    break
        elif coordinates == planets[7]:
            with open ('traveltimes.txt', 'a+') as times:
                times.write(coordinates)
                times.write(',')
                times.close()
            turtle.register_shape('Uranus.gif')
            millennium_falcon = turtle.Turtle()
            space = turtle.Screen()
            print(f'That will take {round(hours, 3)} seconds')
            # print('Attempt_at_lightspeed.gif')
            while hours > 1:
                if hours > 1:
                    skip = input("That will take longer than hour, would you like to skip to the end? ")
                    if skip == 'Yes':
                        space.setup(500,500)
                        turtle.shape("lightspeed.gif")
                        time.sleep(0.5)
                        space.setup(800,320)
                        turtle.shape('Uranus.gif')
                        print(f"You have arrived at {coordinates}")
                        break
                    elif skip == 'No':
                        while True:
                            while hours >= 1:
                                turtle.shape('lightspeed.gif')
                                space.setup(500,500)
                                hours -= 1
                                time.sleep(1)
                                while hours < 1:
                                    exit = input('Would you like to exit hyperspace? ')
                                    if exit == 'Yes':
                                        space.setup(800,320)
                                        turtle.shape('Uranus.gif')
                                        print(f"You have arrived at {coordinates}")
                                        break
                                    elif exit == 'No':
                                        while hours < 1:
                                            print("You've reached your destination, you must exit now")
                                            exit
                                            break
                                else:
                                    print("Approaching destination")
                                    print(f'{round(hours, 3)} hours left' )
                                    continue
                            break
                    break
        elif coordinates == planets[8]:
            with open ('traveltimes.txt', 'a+') as times:
                times.write(coordinates)
                times.write(',')
                times.close()
            turtle.register_shape('Neptune.gif')
            space = turtle.Screen()
            minutes = minutes()
            print(f'That will take {round(hours, 3)} hours')
            # print('Attempt_at_lightspeed.gif')
            while True:
                if hours > 1:
                    skip = input("That will take longer than 20 seconds, would you like to skip to the end? ")
                    if skip == 'Yes':
                        space.setup(500,500)
                        turtle.shape("lightspeed.gif")
                        time.sleep(0.5)
                        space.setup(600,530)
                        turtle.shape('Neptune.gif')
                        print(f"You have arrived at {coordinates}")
                        break
                    elif skip == 'No':
                        while True:
                            while hours >= 1:
                                turtle.shape('lightspeed.gif')
                                space.setup(500,500)
                                hours -= 1
                                time.sleep(1)
                                while hours < 1:
                                    exit = input('Would you like to exit hyperspace? ')
                                    if exit == 'Yes':
                                        space.setup(600,530)
                                        turtle.shape('Neptune.gif')
                                        print(f"You have arrived at {coordinates}")
                                        break
                                    elif exit == 'No':
                                        while timeses < 1:
                                            print("You've reached your destination, you must exit now")
                                            exit
                                            break
                                else:
                                    print("Approaching destination")
                                    print(f'{round(hours, 3)} hours left' )
                                    continue
                            break
                    break
        elif coordinates == planets[9]:
            with open ('traveltimes.txt', 'a+') as times:
                times.write(coordinates)
                times.write(',')
                times.close()
            # distance()
            turtle.register_shape('Pluto.gif')
            millennium_falcon = turtle.Turtle()
            space = turtle.Screen()
            print(f'That will take {round(hours,3)} hours')
            while True:
                if hours > 1:
                    skip = input("That will take longer than an hour, would you like to skip to the end? ")
                    if skip == 'Yes':
                        space.setup(500,500)
                        turtle.shape("lightspeed.gif")
                        time.sleep(0.5)
                        space.setup(470,340)
                        turtle.shape('Pluto.gif')
                        print(f"You have arrived at {coordinates}")
                        break
                    elif skip == 'No':
                        while hours >= 1:
                            turtle.shape('lightspeed.gif')
                            space.setup(500,500)
                            hours -= 1
                            time.sleep(1)
                            while hours < 1:
                                exit = input('Would you like to exit hyperspace? ')
                                if exit == 'Yes':
                                    space.setup(470,340)
                                    turtle.shape('Pluto.gif')
                                    print(f"You have arrived at {coordinates}")
                                    break
                                elif exit == 'No':
                                    while hours < 1:
                                        print("You've reached your destination, you must exit now")
                                        exit
                                        break
                            else:
                                print("Approaching destination")
                                print(f'{round(hours, 3)} hours left' )
                                continue
                            break
    else:
        print('Error, invalid input')
        continue