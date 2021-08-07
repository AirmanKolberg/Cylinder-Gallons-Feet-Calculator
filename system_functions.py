from os import system


def clear_screen():

    _ = system('clear')


def get_float_value_from_user(message_prompt):

    try:

        value = float(input(message_prompt))

    except ValueError:

        print('Please try again, numbers only...')
        value = get_float_value_from_user(message_prompt)

    return value


if __name__ == '__main__':

    pass
