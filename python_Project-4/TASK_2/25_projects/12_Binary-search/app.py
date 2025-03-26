import random
w,h,m=10,10,15
mines={(random.randint(0,w-1),random.randint(0,h-1)) for _ in range(m)}
revealed=set()
flagged=set()

def print_board():
    for y in range(h):
        print(' '.join('F' if (x,y) in flagged else '.' if (x,y) not in revealed else '*' if (x,y) in mines else str(sum((x+i,y+j) in mines for i in[-1,0,1] for j in[-1,0,1])) for x in range(w)))

def reveal(x,y):
    if (x,y) in mines: return False
    revealed.add((x,y))
    if not sum((x+i,y+j) in mines for i in[-1,0,1] for j in[-1,0,1]):
        [reveal(x+i,y+j) for i in[-1,0,1] for j in[-1,0,1] if 0<=x+i<w and 0<=y+j<h and (x+i,y+j) not in revealed]
    return True

while True:
    print_board()
    c,*p=input("Command (r/f x y): ").split()
    x,y=map(int,p)
    (revealed.add((x,y)) if c=='r' and reveal(x,y) else flagged.add((x,y)) if c=='f' else None) or print("BOOM!" if (x,y) in mines else "Invalid")