def sol(gr):
    global dx, dy
    for i in range(5):
        for j in range(5):
            if gr[i][j] == "P":
                for h in range(12):
                    nx=i+dx[h]
                    ny=j+dy[h]
                    if nx<0 or nx>=5 or ny<0 or ny>=5:
                        continue
                    if gr[nx][ny] == "P":
                        if h<4:
                            return 0
                        elif h<8:
                            if gr[nx][j] == "O" or gr[i][ny] == "O":
                                return 0
                        else:
                            if gr[(nx+i)//2][(ny+j)//2] == "O":
                                return 0
    return 1

def solution(places):
    global dx, dy
    dx=[-1,1,0,0,1,1,-1,-1,2,-2,0,0]
    dy=[0,0,-1,1,1,-1,1,-1,0,0,2,-2]
    li=[]
    for g in places:
        li.append(sol(g))
    return li
