num_true = 0
with open('day2_password_philosophy.txt') as f:
    for line in f:
        mini = line.replace('\n', '').split('-')[0]
        maxi, letter, password = line.replace('\n', '').split('-')[1].split(' ')
        if int(mini) <= password.count(letter[0]) <= int(maxi):
            num_true += 1

print(num_true)


num_true = 0
with open('day2_password_philosophy.txt') as f:
    for line in f:
        mini, maxi, letter, password = line.replace('\n', '').replace('-', ' ').replace(':', '').split(' ')
        mini, maxi = int(mini), int(maxi)
        if (password[mini-1]==letter and password[maxi-1]!=letter) or (password[mini-1]!=letter and password[maxi-1]==letter):
            num_true += 1

print(num_true)