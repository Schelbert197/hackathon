# First program to just get feet wet
# This program should change roman nums to arabic

roman_nums = input("What roman numerals would you like converted?")
#roman_nums = "XXIV"
nums_list = ["I", "V", "X", "L", "C", "D", "M"]
nums_list2 = [1, 5, 10, 50, 100, 500, 1000]
result = any(ele in roman_nums for ele in nums_list)
nums_split = []
add_arr = []
piece = ""
for i in range(0, len(roman_nums)): # Iterate through range

    if i==0 and len(roman_nums) !=1: # Check if 0th and init piece
        piece = roman_nums[i]
        continue

    if (roman_nums[i] != roman_nums[i-1] and i != (len(roman_nums)-1)):
        nums_split.append(piece)
        piece = roman_nums[i]
    elif i != len(roman_nums)-1:
        piece = piece + roman_nums[i]
    elif i == len(roman_nums)-1 and roman_nums[i] != roman_nums[i-1]:
        nums_split.append(piece)
        nums_split.append(roman_nums[i])
    elif i == len(roman_nums)-1 and roman_nums[i] == roman_nums[i-1]:
        piece = piece + roman_nums[i]
        nums_split.append(piece)
    else:
        print("bruh idk")

for k in range(len(nums_split)): # every item in list
    local = 0
    for j in range(len(nums_split[k])): # every char in list item
        match nums_split[k][j]:
            case "I":
                local += 1

            case "V":
                local +=5

            case "X":
                local += 10

            case "L":
                local +=50

            case "C":
                local += 100

            case "D":
                local +=500
    
            case "M":
                local +=1000
    
    add_arr.append(local)

add_arr.append(0)
final = 0
for q in range(len(add_arr)-1):
    if add_arr[q] < add_arr[q+1]:
        add_arr[q] *= -1
    final = sum(add_arr)

print(add_arr)
print(final)