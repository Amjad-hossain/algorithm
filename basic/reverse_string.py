# /**
#  * Reverse a string without affecting special characters
#  * Given a string, that contains special character together with alphabets
#  * (‘a’ to ‘z’ and ‘A’ 'Z’), reverse the string in a way that special characters are not affected.
#  *
#  * Examples:
#  *
#  * Input:   str = "a,b$c"
#  * Output:  str = "c,b$a"
#  * Note that $ and , are not moved anywhere.
#  * Only subsequence "abc" is reversed
#  * Write the function in such a way can be easily shared
#  *
#  * Input:   str = "Ab,c,de!$"
#  * Output:  str = "ed,c,bA!$"
#  **/

def reverse(string):
    reverse_string = ""
    count = len(string) - 1
    for index, val in enumerate(string):
        if not val.isalpha():
            reverse_string = reverse_string + val
        else:
            while count >= 0:
                count -= 1
                if string[count + 1].isalpha():
                    reverse_string = reverse_string + string[count + 1]
                    break
    return reverse_string


assert reverse("!!$!!,,,,!!!,,!") == "!!$!!,,,,!!!,,!"
assert reverse("abcd") == "dcba"
assert reverse("a,b$c") == "c,b$a"
assert reverse("Ab,c,de!$") == "ed,c,bA!$"
assert reverse("ab,c,d!") == "dc,b,a!"
assert reverse("$ab,c,d!") == "$dc,b,a!"
