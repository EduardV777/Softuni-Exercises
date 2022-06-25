eggs = input().split(", "); papers = input().split(", ")

eggs = [int(e) for e in eggs]
eggs.reverse()

papers = [int(e) for e in papers]

boxes = []

while(len(eggs) != 0 and len(papers) != 0):
    if eggs[-1] == 13:
        eggs.pop()

        temp = papers[0]
        papers[0] = papers.pop()
        papers.append(temp);
    
    else:
        if(eggs[-1] > 0):
            if(eggs[-1] + papers[-1] <= 50):
                boxes.append(eggs[-1])

            eggs.pop()
            papers.pop()
        
        else:
            eggs.pop()

if len(boxes) > 0:
    print(f"Great! You filled {len(boxes)} boxes.")
else:
    print('Sorry! You couldn\'t fill any boxes!')

if len(eggs) > 0:
    output = "Eggs left: ";
    
    while(len(eggs) != 0 ):
        output += str(eggs.pop())
        
        if(len(eggs) != 0):
            output += ", "

    print(output)

if len(papers) > 0:
    papers.reverse()
    output = "Pieces of paper left: ";
    
    while(len(papers) != 0 ):
        output += str(papers.pop())
        
        if(len(papers) != 0):
            output += ", "

    print(output)

"""
20, 13, -7, 7
10, 5, 20, 15, 7, 9

"""