import random

secret_number = random.randint(1, 100)
attempts = 0

print("=== Number Guessing Game ===")
print("मैंने 1 से 100 के बीच एक नंबर सोचा है। अंदाज़ा लगाओ!")

while True:
    guess = int(input("\nअपना नंबर लिखें: "))
    attempts += 1

    if guess < secret_number:
        print("सोचा गया नंबर इससे बड़ा है! बड़ा नंबर चुनिए।")
    elif guess > secret_number:
        print("सोचा गया नंबर इससे छोटा है! छोटा नंबर चुनिए।")
    else:
        print(f"\nबधाई हो! आपने {attempts} कोशिशों में सही नंबर ({secret_number}) पहचान लिया!")
        break
