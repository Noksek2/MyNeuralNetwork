import numpy as np
Arr=np.array
class MyANN:
    def __init__(my):
        my.W=[]
        my.B=[]
        my.H=None
    def Add(my, w, b):
        my.W.append(w)
        my.B.append(b)
    def SetH(my, H):
        my.H=np.vectorize(H)
    def Calc(my, x):
        z=x
        if len(my.W) != len(my.B):
            print(f'len of W:{len(my.W)} and B : {len(my.B)}')
            return
        N = len(my.W)
        for idx in range(N):
            w=my.W[idx]
            b=my.B[idx]
            z=my.H(np.dot(z,w)+b)
        return z
NN=MyANN()
NN.Add(Arr([[0.5,-0.5], [0.5,-0.5]]), Arr([-0.2, 0.7]))
NN.Add(Arr([[0.5], [0.5]]), Arr([-0.7]))
NN.SetH(lambda x:int(x>0))

D=[[0,0],[1,0],[0,1],[1,1]]
print('===XOR===')
for d in D:
    print(f'{d} : {NN.Calc(Arr(d))}')
