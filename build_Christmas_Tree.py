# Works with Python 3

def build_Christmas_tree(rows):
    for i in range(0, rows):
        for j in range(0, rows*2+1):
            if (j<rows-i) or (j>rows+i):
                print (" ", end="")
            else:
                print(".",end="")
        print("\n")
    
    for i in range(0, 3):
        for j in range(0, rows*2+1):
            if (j<rows-1) or (j>rows+1):
                print (" ",end="")
            else:
                print ("|",end="")
        print ("\n")

build_Christmas_tree(10)

"""
# Output

>>> build_Christmas_tree(10)
          .

         ...

        .....

       .......

      .........

     ...........

    .............

   ...............

  .................

 ...................

         |||

         |||

         |||

>>>




"""