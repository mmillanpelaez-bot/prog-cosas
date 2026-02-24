x = 20

match x:
  case 10:
    print('X is 10')
  case 20:
    print('X is 20')
  case 30:
    print('X is 30')
  case _: # The symbol "_" implies every other option, like an "else".
    print('X is not one of the options (10, 20, 30)')

match x:
  case 10|20|30:
    print(f'X is {x}')
  case _:
    print('X is not one of the options (10, 20, 30)')

y = 20
match x:
  case 10 if x % 2 == 0:
    print('X is 10 and Y is not a prime number')
  case 10:
    print('X is 10 and Y is a prime number'')
  case _:
    print('Unknown option')
