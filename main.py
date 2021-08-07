from math import pi, sqrt
from time import sleep
from system_functions import clear_screen, get_float_value_from_user


# feet, feet;  returns gallons
def get_cylinder_volume(height, diameter):

    volume = (pi * (diameter**2) * height) / 4
    volume *= 7.4805    # Convert to gallons
    return volume


# gallons, feet;  returns feet
def get_cylinder_height(volume, diameter):

    volume /= 7.4805    # Convert from gallons

    if diameter != 0:

        height = (4 * volume) / (pi * (diameter**2))
        return height

    return 'diameter cannot be 0'


# gallons, feet;  returns feet
def get_cylinder_diameter(volume, height):

    volume /= 7.4805    # Convert from gallons

    if height != 0:

        diameter = (2 * sqrt(volume) * sqrt(pi * height)) / (pi * height)
        return diameter

    return 'height cannot be 0'


def main_menu():

    print("""Welcome to the cylinder gallon calculator!
Select what aspect of the cylinder you're trying to find:

volume (v)
height (h)
diameter (d)
""")
    selection = input('> ')

    if selection == 'volume' or selection == 'v':

        height = get_float_value_from_user('Height in feet: ')
        diameter = get_float_value_from_user('Diameter in feet: ')

        volume = get_cylinder_volume(height, diameter)
        print(f'The volume of a cylinder with a height of {height}ft and diameter of {diameter}ft is:\n{volume} gallons')

    elif selection == 'height' or selection == 'h':

        volume = get_float_value_from_user('Volume in gallons: ')
        diameter = get_float_value_from_user('Diameter in feet: ')

        height = get_cylinder_height(volume, diameter)
        print(f'The height of a cylinder with a volume of {volume}gal and diameter of {diameter}ft is:\n{height} feet')

    elif selection == 'diameter' or selection == 'd':

        volume = get_float_value_from_user('Volume in gallons: ')
        height = get_float_value_from_user('Height in feet: ')

        diameter = get_cylinder_diameter(volume, height)
        print(f'The diameter of a cylinder with a volume of {volume}gal and height of {height}ft is:\n{diameter} feet')

    else:

        print(f'{selection} is not valid, please try again.\n')
        sleep(1)

        main_menu()


if __name__ == '__main__':

    clear_screen()
    main_menu()
