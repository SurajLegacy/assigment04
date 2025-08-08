correctPassword = "Secret"
attemptsLeft = 3
userAttempt = ""
while (attemptsLeft > 0) and (userAttempt != correctPassword):
    userAttempt = str(input(f"Enter Password(Attempts Left : {attemptsLeft}:)"))
    attemptsLeft -= 1
if(userAttempt == correctPassword):
    print("Access Granted")
else:
    print("Access Denied")    