def ask(name):
    print("\n\t",name)
    pos=int(input("Enter the position : "))
    return (pos)

def show(mat):
    for i in range(3):
        for j in range(3):
            print(mat[i][j],end= " ")
        print()
    return

def   winner(mat,i,j,player_1,player_2,s_1,s_2):
    if mat[i][j]==s_1 :
        print("\t!!!Congratulations %s win !!!! "%player_1)
    else:
        print("\t!!!Congratulations %s win !!!! " % player_2)
mat=[]
row=[]
c=1
for i in range(3):
    for j in range(3):
        row.append(c)
        c+=1
    mat.append(row)
    row=[]

player_1=input("Enter the name of player 1 : ")
player_2=input("Enter the name of player 2 : ")
s_1=input("Enter symbol of player 1 X or O : ")
s_2=input("Enter symbol of player 1 X or O : ")

show(mat)
for i in range(9):
    c=0
    while(c<1):
        if(i%2==0):
            pos=ask(player_1)
            for i in range(3):
                for j in range(3):
                    if(pos==mat[i][j]):
                        mat[i][j]=s_1
                        show(mat)
                        c+=1
                        break
                if(c==1):
                    break
            else:
                print("Invalid position \nEnter positon correctly")
                show(mat)
                c=0

        else:
            pos = ask(player_2)
            for i in range(3):
                for j in range(3):
                    if (pos ==mat[i][j]):
                        mat[i][j] = s_2
                        show(mat)
                        c += 1
                        break
                if (c == 1):
                    break
            else:
                print("Invalid Position \nEnter positon correctly")
                show(mat)
                c = 0

    win=0
    cd = 0
    rcd = 0
    for i in range (3):
        r=mat[i][0]
        c=mat[0][i]
        d=mat[1][1]
        for j in range(3):
            if(r!=mat[i][j]):
                break
        else:
            winner(mat,i,j,player_1,player_2,s_1,s_2)
            win += 1
            break

        for j in range(3):
            if (c != mat[j][i]):
                break
        else:
            winner(mat,i,j,player_1,player_2,s_1,s_2)
            win+=1
            break
        for j in range(3):
            if(i==j):
                if(d ==mat[i][j]):
                    cd+=1
                if(cd==3):
                    winner(mat, i, j, player_1, player_2, s_1, s_2)
                    win += 1
                    break
            if (i +j==2):
                if (d ==mat[i][j]):
                    rcd += 1
                if (rcd == 3):
                    winner(mat, i, j, player_1, player_2, s_1, s_2)
                    win += 1
                    break
        if (win == 1):
            break
    if(win==1):
        break
else:
    print("\t!!!DRAW!!!\n\tGAME OVER")









