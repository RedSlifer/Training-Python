def main():
    try:
        number_1, number_2 = eval(input('Enter two numbers separated by a comma: '))
        result = number_1 / number_2
        print(f'Result is {result}')
    except ZeroDivisionError:
        print('division by zero!')
    except SyntaxError:
        print('A comma may be missing in the input')
    except:
        print('Something ins wrong i the input')
    finally:
        print('The finally clause is executed')


main()
