def reversing_string (string):
    string = string[::-1]
    return string

def atbash_dcoder (string):
    decoded = ""
    for char in string:
        if char.isalpha():
            if char.isupper():
                ref_pos = ord("A")
            elif char.islower():
                ref_pos = ord("a")
            char_pos = ord(char)
            scaled_pos = char_pos - ref_pos 
            new_pos = 25 - scaled_pos
            new_sym = chr(new_pos + ref_pos)
        else:
            new_sym = char

        decoded += new_sym
    return(decoded)

def caeser_cypher_dcoder (string, shift_target, direction):
    position = 0

    decoded = ""
    for char in string:
        temp = string[position]
        if temp.isupper():
            base_char_pos = ord("A") 
            end_char_pos = ord("Z") 
        elif temp.islower():
            base_char_pos = ord("a") 
            end_char_pos = ord("z") 
        

        temp_old_pos = ord(temp)

        if direction == "R":
            temp_new_pos = temp_old_pos - shift_target
            if temp_new_pos < base_char_pos:
                diff = base_char_pos - temp_new_pos
                temp_new_pos = (end_char_pos - diff) + 1
                diff = diff - 1

                
        elif direction == "L":
            temp_new_pos = temp_old_pos + shift_target
            if end_char_pos < temp_new_pos:
                diff = temp_new_pos - end_char_pos
                temp_new_pos = (base_char_pos + diff) - 1
                diff = diff - 1


        temp_new = chr(temp_new_pos)

        position = position + 1
        decoded = decoded + temp_new

    return (decoded)