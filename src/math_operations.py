def my_function():
    print('Hello, linting!')
    x=1  # Intentional missing space around '=' (E225)
    y = [1,2,3]  # Intentional missing whitespace after ',' (E231)
    if x==1:  # Intentional comparison to literal (C0121)
        print("x is 1")
    return None  # Intentional use of 'None' instead of 'return' (R1716)

my_function()  # Missing blank line after function definition (C0303)
