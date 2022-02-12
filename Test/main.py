from gpiozero import Robot
from time import sleep


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    robot = Robot((17, 27), (10, 9))
    while True:
        robot.forward(speed=1, curve_right=0.5, curve_left=0)
        sleep(10)
        robot.forward(speed=1, curve_right=0, curve_left=0.5)
        sleep(10)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
