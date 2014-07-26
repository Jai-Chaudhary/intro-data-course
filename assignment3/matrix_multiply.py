import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    matrix = record[0]
    value = record[3]
    
    if matrix == 'a':
      for k in xrange(0,5):
        mr.emit_intermediate((record[1] , k), record)
    elif matrix == 'b':
      for i in xrange(0,5):
        mr.emit_intermediate((i ,record[2]), record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    emit = False
    for a in list_of_values:
      if a[0] == 'a' and a[1] == key[0]:
        for b in list_of_values:
          if b[0] == 'b' and b[2] == key[1] and a[2] == b[1]:        
            total += a[3] * b[3]
            emit = True
    if emit:
      mr.emit((key[0], key[1], total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
