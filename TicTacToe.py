board=[0,1,2,
       3,4,5,
       6,7,8]
def show():
    print(board[0],'|',board[1],'|',board[2])
    print("------------")
    print(board[3],'|',board[4],'|',board[6])
    print("------------")
    print(board[6],'|',board[7],'|',board[8])


playing =True
while playing:

    print("player1")
    x=int(input("select a spot: "))
    y=int(input("ENTER A NO.: "))
    if y==1:
        board[x]=='1'
    elif y==3:
        board[x]=='3'
    elif y==5:
        board[x]=='5'
    elif y==7:
        board[x]=='7'
    elif y==9:
        board[x]=='9'
    else:
        print("NO")
    show()


    print("player2")
    m=int(input("select a spot: "))
    n=int(input("ENTER A NO.: "))
    if n==2:
        board[m]=='2'
    elif n==4:
        board[m]=='4'
    elif n==6:
        board[m]=='6'
    elif n==8:
        board[m]=='8'
    else:
        print("NO")
    show()
    playing=False


sum1=0
for i in range(board[0],board[3]):
    sum1+=i
    if sum1==15:
        break
if i%2==0:
    print("p2 wins")
else:
    print("p1 wins")
show()

sum2=0
for j in range(board[3],board[6]):
    sum2+=j
    if sum2==15:
        break
if j%2==0:
    print("p2 wins")
else:
    print("p1 wins")
show()

sum3=0
for q in range(board[6],board[9]):
    sum3+=q
    if sum3==15:
        break
if q%2==0:
    print("p2 wins")
else:
    print("p1 wins")
show()


sum4=0
for w in range(board[0],board[7],2):
    sum4+=w
    if sum4==15:
        break
if w%2==0:
    print("p2 wins")
else:
    print("p1 wins")
show()

sum5=0
for r in range(board[1],board[8],2):
    sum5+=r
    if sum5==15:
        break
if r%2==0:
    print("p2 wins")
else:
    print("p1 wins")
show()


sum6=0
for t in range(board[2],board[9],2):
    sum6+=t
    if sum6==15:
        break
if t%2==0:
    print("p2 wins")
else:
    print("p1 wins")
show()

sum7=0
for d in range(board[0],board[9],3):
    sum7+=d
    if sum7==15:
        break
if d%2==0:
    print("p2 wins")
else:
    print("p1 wins")
show()

sum8=0
for f in range(board[2],board[7],1):
    sum8+=f
    if sum8==15:
        break
if f%2==0:
    print("p2 wins")
else:
    print("p1 wins")
show()
