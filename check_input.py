from random import randint


def user(user_input, name=False):
    if user_input == 'q':
        print('Program will be terminated')
        exit(0)
    else:
        try:
            user_input = int(user_input)
            if user_input > 0:
                return user_input
            else:
                print('Number must be positive, press Enter (code1)')
                input()
                if name:
                    return 0
                else:
                    return ''
        except TypeError:
            print('Input must be a number, press Enter (code2)')
            input()
            if name:
                return 0
            else:
                return ''
        except ValueError:
            print('Input must be a number, press Enter (code3)')
            input()
            if name:
                return 0
            else:
                return ''


def input_(*args):
    try:
        if (user(el) is int for el in args):
            return list(map(int, args))
    except ValueError:
        return False
    except TypeError:
        return False


def gen_list(len_arr):
    return [randint(0, 100) for i in range(user(len_arr, True))]