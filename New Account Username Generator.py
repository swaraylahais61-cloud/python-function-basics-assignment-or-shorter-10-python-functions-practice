#New Account Username Generator
def create_username(full_name, birth_year):
    first_word = full_name.split()[0].lower()
    last_two_digits = str(birth_year)[-2:]
    return first_word + last_two_digits


