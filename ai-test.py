from fuzzywuzzy import fuzz
from fuzzywuzzy import process

diff = fuzz.ratio("this is a test", "this is a test!")

print('Distance: {}'.format(diff))

