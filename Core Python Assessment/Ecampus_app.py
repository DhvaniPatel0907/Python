import random

# Storing events in tuple
events = []

# storing participants in dictionary
event_participants = {}


# function to add event
def add_events():
    event_id = random.randint(20,50)
    print(f"Event ID is: {event_id}")

    name = input("Enter event name: ")
    date = input("Enter date (DD-MM-YYYY) of event: ")
    age_limit = int(input("Enter age limit: "))
    club = input("Enter name of club: ")

    event = (event_id, name, date, age_limit, club)
    events.append(event)

    print(f"Event {name} added successfully")


# function to register participants
def register_participnats():
    event_id = int(input("Enter event ID to register: "))

    # to find event
    event = None
    for e in events:
        if e[0] == event_id:
            event = e
            break

    if event is None:
        print("Event not found")
        return
    
    name = input("Enter name of participant: ")
    age = int(input("Enter age of participant: "))

    # checking age limit
    if age < event[3]:
        print(f"Sorry, you are not eligible to participate for {event[1]}")
        return
    
    # creating participant
    participant = {"name": name, "age": age, "event": event_id, "present": False}

    # storing participant in dictionary
    if event_id not in event_participants:
        event_participants[event_id] = []

    event_participants[event_id].append(participant)
    print(f"{name} is registered for {event[1]}")


# function to mark attendance
def mark_attendance():
    event_id = int(input("Enter event ID: "))

    if event_id not in event_participants:
        print("no participant found")
        return
    
    name = input("Enter name of participant to mark attendance: ")

    for p in event_participants[event_id]:
        if p["name"] == name:
            p["present"] = True
            print(f"Attendance marked for {name}")
            return
    
    print("no participant found in this event")


# function for report
def attendance_report():
    event_id = int(input("Enter event ID for report: "))

    if event_id not in event_participants:
        print("Data not found")
        return

    participants = event_participants[event_id]
    total = len(participants)
    attended = 0
    for p in participants:
        if p["present"]:   
            attended += 1
    missed = total - attended

    # find event name
    event_name = ""
    for e in events:
        if e[0] == event_id:
            event_name = e[1]

    print(f"Event report: {event_name} (ID: {event_id})")
    print(f"Total participants: {total}")
    print(f"Total attendance: {attended}")
    print(f"Total missed: {missed}")


while True:
    menu = """
            press 1 to add Event
            press 2 to register participant
            press 3 to mark attendance
            press 4 to view report
            press 5 to Exit
"""
    print(menu)

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_events()
    
    elif choice == 2:
        register_participnats()
    
    elif choice == 3:
        mark_attendance()
    
    elif choice == 4:
        attendance_report()
    
    elif choice == 5:
        print("Thank you for Participating, Bye bye")
        break
    
    else:
        print("Invalid choice, please try again")