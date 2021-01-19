class Rect:
    def constructRectangle(self, area: int):
        for i in range(int(area**.5)+1,0,-1):
        
            if area%i==0:
                if i<area//i:
                    return [area//i,i]
                else:
                    return [i,area//i]


print(Rect().constructRectangle(10023))
                
                
        