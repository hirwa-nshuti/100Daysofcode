class Area:
    def maxArea(self, height):
            start, end = 0, len(height) - 1
            surface = 0
            while start != end:
                if height[start] < height[end]:
                    t = height[start]*(end - start)
                    surface = max(surface,t)
                    start += 1
                else:
                    t = (height[end]*(end - start))
                    surface = max(surface,t)
                    end -= 1

            return surface

a=[1,8,6,2,5,4,8,3,7]
print(Area().maxArea(a))