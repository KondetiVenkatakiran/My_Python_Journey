from turtledemo.penrose import start

command = " "
started = False
while command != "quit":
    command =  input("> ").lower()
    if command == "start":
        if started:
            print("car is already started! ")
        else:
            started =True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("car is already stopped!")
        print("Car Stopped...")
    elif command == "help":
        print("""
        Start - to start the car
        stop - to stop the car
        quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry I don't understand that: ")