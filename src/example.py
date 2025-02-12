from PyBWT import BWT_Container

s = "banana"

bwt_container = BWT_Container(s)

bwt_str = bwt_container.encode_BWT()
print(f"BWT of '{s}': {bwt_str}")

decoded_str = bwt_container.decode_BWT()
print(f"Decoded BWT: {decoded_str}")

number_occurences = bwt_container.count_occurrences("a")
print(f"Number of occurrences: {number_occurences}")


