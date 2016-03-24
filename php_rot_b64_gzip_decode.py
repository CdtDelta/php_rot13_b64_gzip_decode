# This script is designed to decode the following type of PHP eval statement:
#
# eval (gzinflate(base64_decode(str_rot13...
#
# Just feed it in the "encrypted string" and the code will do the rest
#
# By Tom Yarrish
# Version 0.1
#
import zlib
import base64
import codecs

# This function will take care of the base64 and the gz part
# Got this function from: http://www.php2python.com/wiki/function.gzinflate/
def gzinflate(base64_string):
    compressed_data = base64.b64decode(base64_string)
    return zlib.decompress(compressed_data, -15)

print "Make sure all the whitespace has been removed from the string you want to decode.\n"
string_to_decode = raw_input("Enter the string to decode: ")

# First we take care of the rot31 code
rot13_decoded = codecs.decode(string_to_decode, 'rot13')

decoded_string = gzinflate(rot13_decoded)

print "The decoded string is:\n{}".format(decoded_string)
