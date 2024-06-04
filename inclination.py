def calculate_final_speed(initial_speed, inclinations):
    final_speed  = initial_speed
    for inclination in inclinations:
    	if ( inclination < final_speed):
    		final_speed -= inclination
    	else:
    		final_speed = 0

    return final_speed

print(calculate_final_speed(60, [0, 30, 0, -45, 0]))