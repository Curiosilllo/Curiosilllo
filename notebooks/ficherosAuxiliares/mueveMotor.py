from accelstepper import AccelStepper

motor = AccelStepper(1, 5, 19, 0, 0, 1)

motor.set_acceleration(200)
motor.set_max_speed(400)

for i in range(10):

    if i % 2 == 0:
        motor.move_to(1600)
    else:
        motor.move_to(0)
    print("HOLA")
    print(motor._direction)

    while motor.distance_to_go() != 0:
        motor.run()

