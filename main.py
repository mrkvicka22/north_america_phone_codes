from scraper import get_phone_code_dict
import random
from constants import Colors

phone_code_dict = get_phone_code_dict()
phone_codes = list(phone_code_dict.keys())
correct = 0
all = 0
while True:
    current_code = random.choice(phone_codes)
    area = input(f"Where is {current_code}? ")
    all+=1
    if phone_code_dict[current_code].lower() == area.lower():
        correct += 1
        print(f"{Colors.OKGREEN}Correct, your score is {round(correct/all*100,2)}%{Colors.ENDC}")
    else:
        print(f"{Colors.FAIL}Incorrect, your score is {round(correct / all * 100, 2)}%\nCorrect was {phone_code_dict[current_code]}{Colors.ENDC}")

