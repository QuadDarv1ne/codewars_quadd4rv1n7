'''
[ Pyramid Slide Down ]

Lyrics...
Pyramids are amazing.
Both in architectural and mathematical sense.
If you have a computer, you can mess with pyramids even if you are not in Egypt at the time.
For example, let's consider the following problem.

Imagine that you have a pyramid built of numbers, like this one here:
   /3/
  \7\ 4 
 2 \4\ 6 
8 5 \9\ 3

Here comes the task...
Let's say that the 'slide down' is the maximum sum of consecutive numbers from the top to the bottom of the pyramid.
As you can see, the longest 'slide down' is 3 + 7 + 4 + 9 = 23

Your task is to write a function that takes a pyramid representation as an argument and returns its largest 'slide down'.

For example:
* With the input `[[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]`
* Your function should return `23`.
By the way...

My tests include some extraordinarily high pyramids so as you can guess, brute-force method is a bad idea unless you have a few centuries to waste.
You must come up with something more clever than that.

(c) This task is a lyrical version of Problem 18 and/or Problem 67 on ProjectEuler.

def longest_slide_down(pyramid):
    # TODO: write some code...
    pass
'''


def longest_slide_down(pyramid):
    # Start from the second-to-last row, work upwards
    for row in range(len(pyramid) - 2, -1, -1):  # From the second-last row to the top
        for col in range(len(pyramid[row])):
            # Update each element to be the sum of itself and the maximum of the two numbers below it
            pyramid[row][col] += max(pyramid[row + 1][col], pyramid[row + 1][col + 1])
    
    # The top element now contains the maximum sum
    return pyramid[0][0]


'''
def longest_slide_down(p):
    res = p.pop()
    while p:
        tmp = p.pop()
        res = [tmp[i] + max(res[i],res[i+1])  for i in range(len(tmp))] 
    return res.pop()
'''


# TODO: Заметки
## Автор: Дуплей Максим Игоревич / Dupley Maxim Igorevich
## Дата: 30.11.2024
