def speed():
    distance = float(input("distance is? "))
    time = float(input("time is? "))
    print("speed", distance/time, "m/s")

def force():
    mass = float(input("mass is? "))
    acceleration = float(input("acceleration is? "))
    print("force", mass*acceleration, "N")

def work():
    force = float(input("force is? "))
    distance = float(input("distance is? "))
    print("work", force*distance, "joules")

def simple_interest():
    principle = float(input("principle is? "))
    interest_rate = float(input("interest_rate is? "))
    constant = float(input("constant is? "))
    time = float(input("time is? "))
    print("simple_Interest", principle*constant+interest_rate*time, "Naira")

def acceleration():
    change_in_velocity = float(input("change_in_velocity is? "))
    Change_in_time = float(input("CHange_in_time is? "))
    print("acceleration", change_in_velocity/change_in_time)

menu = int(input(
    "type 1 to calculate speed\n"
    "type 2 to calculate force\n"
    "type 3 to calculate work\n"
    "type 4 to calculate simple_interest\n"
    "type 5 to calculate acceleration\n"
))

if menu == 1:
    speed()
elif menu == 2:
    force()
elif menu == 3:
    work()
elif menu == 4:
    simple_interest()
elif menu == 5:
    acceleration()

else:
    ("incorrect input, try again")