import time
print("Hello there and welcome to the pressure meansure!\nThis calculator will help you find the pressure applied on a object if you know the force and the area over which the force is appied over.")
time.sleep(3)
print("Instructions to use this calcualtor are:\n1. Enter the force applied (the unit will be Newton)\n2. Enter the area over which the pressure is applied (the unit will be metre squared)\n3. Wait and watch for the magic that s going to happen after you folow the above instructions.")
time.sleep(3)
print("Sorry to disappoint you but no magic will occur you will just get what you came here for.")
time.sleep(3)
print("Enough of talking, let us do the main purpose!")
time.sleep(3)
print("Secret easter egg: Copy paste this text in force, 'CBSE boards result' and in area '10th and 12th class kids'. ")
force = input ("Enter the force applied: ")
area = input ("Enter the area of the force applied over: ")
if force in ['CBSE boards result']:
	
    print("Aunties: KITNA AAYA?")
    time.sleep(4)
    print("Students in mind: *chuppo salo chootiyo*")
    time.sleep(4)
    print("Students irl: Aunty ji, aap chai paani kuch le lijiye na.")
    time.sleep(4)
    print("Auntie: wo sabh to thik hai leken kitnei aayae?")
    time.sleep(4)
    print("Creator: Absose wo student auntie ji ke jangool se bach nahi paya.")
else:
    result = float(force) / float(area)
    print ("Therefore, the pressure applied on the object is: " + str(result) + " Pa.") 
    