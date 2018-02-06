def same_structure_as(original, other):
    if type(original) != list or type(other) != list:
        return False
    original = [i for i in original if type(i) != str]
    other = [i for i in other if type(i) != str]
    original = ''.join([i if i == '[' or i == ']' else '-' for i in str(original)])
    other = ''.join([i if i == '[' or i == ']' else '-' for i in str(other)])
    if original == other: return True
    else: return False