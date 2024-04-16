def main():
    I = int(input("n1"))
    T = int(input("n1"))
    I,T = X(I,T)
    I,T = Y(I,T)

    print(f"{X(I)}")
    print(Y(I))
def X(N,M):
    if(N < 0):
        N = 0
    elif(M<0):
        M = 0
    N += M
    return(N,M)
def Y(N,M):
    if(N < 0):
        N = 0
    elif(M<0):
        M = 0
    N *=M
    return (N,M)
main()