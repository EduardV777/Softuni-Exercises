from collections import deque
queue=deque([])
queue.appendleft('C1')
queue.appendleft('C2')
queue.appendleft('C3')

def ShowQueue(queue, direct='leftRight'):
    output=""
    while len(queue):
        if(direct=='leftRight'):
            output+=queue.pop()
        elif (direct=='rightLeft'):
            output+=queue.popleft()
        if(len(queue)!=0):
            output+=", "
    return output

print(queue)
print(ShowQueue(queue))

print("\n")
queue2=deque([])

queue2.append('Terry')
queue2.append('Merry')
queue2.append('Ferry')

print(queue2)
print(ShowQueue(queue2, direct='rightLeft'))
