with open('day9_encoding_error.txt', 'r') as f:
    all_numbers = [int(i.replace('\n', '')) for i in f.readlines()]


def is_correct(n, nums):
    for i in range(len(nums)):
        for j in nums[:i] + nums[i+1:]:
            if nums[i]+j == n:
                return True
    return False


def find_contiguous(n, nums):
    for i in range(len(nums)):
        print(i)
        current_n = nums[i]
        for j in range(i+1, len(nums)):
            current_n += nums[j]
            if current_n > n:
                print(f"\t{current_n}")
                break
            elif current_n == n:
                return nums[i:j+1]
    return [nums[-1]]


for i in range(25, len(all_numbers)):
    if not is_correct(all_numbers[i], all_numbers[i-25:i]):
        n = all_numbers[i]
        break

print(n)
contiguous = find_contiguous(n, all_numbers)
print(contiguous)
print(min(contiguous) + max(contiguous))
