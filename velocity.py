print ("Hello there and welcome to the velocity calcualtor!\nIn this calculator you will be asked to insert the direction of displacement, magnitude of displacement and the time taken to cover that displacement so basically what you learnt in physics in prbably 7th grade or so(actually the person making this is still in 8th grade only so he can think of do this much only but).\nAnyways now without wasting time let us find some velocities!")
direction_of_displacement = input ("Enter the direction of displacement over here (like north, south, upwards, etc): ")
unit_of_displacement = input ("Enter the unit of displacement over here(like metre, kilometre, mile, etc): ")
unit_of_time = input ("Enter the unit of time(like second, minutes, etc): ")
magnitude_of_displacement = input ("Enter the magnitude(value) of displacement over here: ")
time = input ("Enter the time taken to cover the displacement over here: ")
result = float(magnitude_of_displacement) / float(time)
print ("The velocity of the object is " + str(result) + " " + unit_of_displacement + " per " + unit_of_time + " " + direction_of_displacement + ".\nThank you for using this calculator.")