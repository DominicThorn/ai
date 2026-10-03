from collections import Counter

def word_block(scrambled, target):
    scrambled_count = Counter(scrambled)
    target_count = Counter(target)
    if scrambled_count == target_count:
        return True
    return False

scrambled = "TCA"
target = "CAT"

print("Available letters:", scrambled)
print("Target Word: ", target)

if word_block(scrambled, target):
    print("The target word can be formed.")
    print("Solution:", target)
else:
    print("The target word cannot be formed.")