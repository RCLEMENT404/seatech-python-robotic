"""my_controller controller."""
from fighter import Fighter

robot = Fighter()
timestep = int(robot.getBasicTimeStep())

while robot.step(timestep) != -1:
    robot.run()
