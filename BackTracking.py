import sys
def implementation(a):
    for i in range(4):
        a[0][i] = '0'
        for j in range(4):
            a[1][j] = '0'
            for k in range(4):
                a[2][k] = '0'
                for l in range(4):
                    a[3][l] = '0'
                    if ((j!=i) and (j != i+1) and (j != i-1) and (k!= i) and (k != j) and (k != i+2) and (k != j+1) and (k!= i-2) and (k!= j-1) and (l!= i) and (l != j) and (l != k) and (l != i+3) and (l != j+2) and (l != k+1) and (l!= i-3) and (l!= j-2) and (l!= k-1) ):
                        a[1][j] = '0'
                        a[2][k] = '0'
                        a[3][l] = '0'
                    else:
                        a[0][i] = 'x'
                        a[1][j] = 'x'
                        a[2][k] = 'x'
                        a[3][l] = 'x' 
            
    return a



if __name__ == "__main__":
    chess = [['x','x','x','x'],['x','x','x','x'],['x','x','x','x'],['x','x','x','x']]
    result = implementation(chess)

    for i in range(4):
        for j in range(4):
            sys.stdout.write(result[i][j])