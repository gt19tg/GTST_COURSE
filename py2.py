code = [2313, 2314 ,4325, 6546]
errors = 0

while True:
    if errors <= 5:
        user = int(input(f"Enter The captcha correctly {code[0]}:\n>>"))
        if user != int(code[0]):
            print(int(code[0]))
            print(f"trail {errors}: incorrect!, try again")
            errors += 1
        elif user == int(code[0]):
            print("wellDone!")
            break
    else:
        print("try again, next time.")
        break