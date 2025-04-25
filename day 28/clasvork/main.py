1.
def to_appercase(string):
    return string.apper()


# 2) მომხმარებელს შემოატანინეთ თავისი სახელი და გამოიტანეთ ამ სახელის პირველი ასო upper_case'ში 


name = input("გთხოვთ მიუტითეთ თქვენი სახალი")
first_upper=name[0].upper()


#3) შექმენით ცვლადი სადაც შეიყვანთ რაღაც წინადადებას შემდეგ კი ამ წინდადებაში მოძებნდეთ თქვენთვის სასურველი სიტყვა 

sentence = input("შეიყვანეთ წინადადება: ")
word_to_find = input("შეიყვანეთ სიტყვა, რომლის მოძებნაც გსურთ: ")
if word_to_find in sentence:
    print(f"სიტყვა '{word_to_find}' იპოვეს წინადადებაში!")
else:
    print(f"სიტყვა '{word_to_find}' არ არის ამ წინადადებაში.")




4.


    def transform_and_concatenate(arg1, arg2):
    arg1_upper = arg1.upper()
    arg2_lower = arg2.lower()
    
    result = arg1_upper + arg2_lower
    
    return result