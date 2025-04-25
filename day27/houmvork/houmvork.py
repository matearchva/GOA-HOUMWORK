#1) 
def to_uppercase(string):
    return string.upper()


# 2) მომხმარებელს შემოატანინეთ თავისი სახელი და გამოიტანეთ ამ სახელის პირველი ასო upper_case'ში
name = input("შეიყვანეთ თქვენი სახელი: ")
first_letter_upper = name[0].upper()


# 3) მომხმარებელს შემოატანინეთ თავისი გვარი და გამოიტანეთ ამ გვარის ბოლო ასო upper_case'ში
sentence = input("შეიყვანეთ წინადადება: ")
word_to_find = input("შეიყვანეთ სიტყვა, რომლის მოძებნაც გსურთ: ")
if word_to_find in sentence:
    print(f"სიტყვა '{word_to_find}' იპოვეს წინადადებაში!")
else:
    print(f"სიტყვა '{word_to_find}' არ არის ამ წინადადებაში.")



#4)
def transform_and_concatenate(arg1, arg2):
    arg1_upper = arg1.upper()
    arg2_lower = arg2.lower()
    
    result = arg1_upper + arg2_lower
    
    return result