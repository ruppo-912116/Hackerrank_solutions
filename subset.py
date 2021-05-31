permutation = []
chosen = []

def search():
    if (len(permutation)== 3):
        pass
    else:
        for i in range(3):
            if(chosen[i]):
                continue
            chosen[i] = True
            permutation.append(i)
            search()
            chosen[i]= False
            print(permutation.pop())

if __name__ == "__main__":
    
    for i in range(50):
        chosen.append(False) 
    search()
    