def count_string(str1, str2):
    same_list = []
    for i in str1:
        for j in str2:
            if i == j:
                same_list.append(i)
    same_list = ' '.join(same_list).split()
        
    same_list = set(same_list)
    print(f"your common letters are {same_list}")
    num = len(same_list)
    print(f"Your words have {num} of the same letters and characters")

str1 = input("Type here -> ")
str2 = input("Type here as well -> ")
count_string(str1, str2)