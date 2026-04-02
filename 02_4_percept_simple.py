import numpy as np

def make_model(W,B):
    return lambda X: int(np.sum(W*X)+B > 0)

INPUT=np.array([[0,0],[1,0],[0,1],[1,1]], dtype=np.int16)
or_model=make_model([0.5,0.5],-0.2)
and_model=make_model([0.5,0.5],-0.7)
nand_model=make_model([-0.5,-0.5],0.7)
xor_model=lambda D: and_model(np.array([or_model(D),nand_model(D)]))

data_2d=INPUT
for d2 in data_2d:
    print(f'INPUT {d2}')
    print(f'OR : {or_model(d2)}', end=', ' )
    print(f'AND : {and_model(d2)}', end=', ')
    print(f'NAND : {nand_model(d2)}', end=', ')
    print(f'XOR : {xor_model(d2)}', end='\n\n')