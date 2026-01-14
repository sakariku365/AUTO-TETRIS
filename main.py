print("AUTO-TETRIS")

field = []
for i in range(20):
    for j in range(10):
        row=[]
        row.append(0)
    field.append(row)

minos = [            #[ミノの種類][y][x]
    [   [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0] ]
]

