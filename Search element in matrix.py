class Matrices:
    def searchMatrix(self, matrix, target):
        x, y = len(matrix) - 1, 0
        while(x >= 0 and x < len(matrix) and y >=0 and y < len(matrix[0])):
            if(matrix[x][y] == target): 
                return True
            if(matrix[x][y] > target):  
                x -= 1
            if(matrix[y][y] < target):  
                y += 1              
        return False  
a=[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],
[10,13,14,17,24],[18,21,23,26,30]]
target=30

print(Matrices().searchMatrix(a,target))

