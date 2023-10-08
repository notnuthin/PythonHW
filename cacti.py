def cacti_number(array2DOriginal):
    additionalCacti = 0
    array2D = array2DOriginal.copy()
    for i in range(0,len(array2D)):
        for j in range(0,len(array2D[0])):
            if array2D[i][j]==0:
                if i>0:
                    if array2D[i-1][j] == 1:
                        continue
                if i<len(array2D)-1:
                    if array2D[i+1][j] == 1:
                        continue
                if j>0:
                    if array2D[i][j-1] ==1:
                        continue
                if j<len(array2D[0])-1:
                    if array2D[i][j+1] ==1:
                        continue
                array2D[i][j]=1
                additionalCacti+=1
    return additionalCacti

# def main():
#     plot = [ [1, 0, 1, 0, 1],
#              [0, 0, 0, 0, 0],
#              [1, 0, 0, 0, 0] ]
#     print(len(plot))
#     print(len(plot[0]))
#     print(cacti_number(plot))

#     plot2 = [ [0, 1, 0, 0, 0, 0],
#              [0, 0, 0, 1, 0, 0],
#              [1, 0, 1, 0, 0, 1] ]
#     print(cacti_number(plot2))
# main()