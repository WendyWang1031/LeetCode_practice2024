"""
Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, 
peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. 
You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 

Example 1:

Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
 

Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.
"""
class MyQueue(object):
    """
    push(x)：將元素 x 添加到隊列末尾。
    pop()：刪除並返回隊列最前面的元素。
    peek()：返回隊列最前面的元素。
    empty()：判斷隊列是否為空。

    """

    def __init__(self):
        self.stack_in = [] # 用來處理 push
        self.stack_out = [] # 用來處理 pop 和 peek

    def push(self,x):
        self.stack_in.append(x)
    def pop(self,x):
        """
        從 stack_out 彈出元素，若 stack_out 為空，則將 stack_in 的元素倒入 stack_out。
        :return: 隊列最前面的元素。
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()
    def peek(self,x):
        """
        返回隊列最前面的元素，若 stack_out 為空，則將 stack_in 的元素倒入 stack_out。
        :return: 隊列最前面的元素。
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out[-1]
    def empty(self,x):
        return not self.stack_in and not self.stack_out