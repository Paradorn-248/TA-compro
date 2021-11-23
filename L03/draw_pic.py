"""
2
* * *
 **
 **
*  *

3
*     *
 *   *
  ***
  * *
  ***
 *   *
*     *

4
*   **   *
 *  **  *
  * ** *
   ****
   *  *
   *  *
   ****
  * ** *
 *  **  *
*   **   *
"""

def draw(n) :
    for i in range(n-1) :
        print(" "*i + "*" + " "*(((3*(n-2))+2)-2*i) + "*")
    print(" "*(n-1) + "*"*n)
    for i in range(n-2) :
        print(" "*(n-1) + "*" + " "*(n-2) + "*")
    print(" "*(n-1) + "*"*n)
    for i in range(n-1) :
        print(" "*(n-2-i) + "*" + " "*(n+(2*i)) + "*")

n = int(input())
draw(n)

####################check function
# ::elab:begincode hidden=True
# check = input()
# if check == '01':
#     draw(8)
# ::elab:endcode