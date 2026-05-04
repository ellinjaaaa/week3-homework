from utils2 import generate_number, check_guess
from validators2 import is_valid_guess
from main import run_game

print(generate_number())
print(check_guess(20,25)) #high
print(check_guess(30,30)) #correct
print(check_guess(25,20)) #low
print(is_valid_guess("30")) #True
print(is_valid_guess("are")) #False
run_game()