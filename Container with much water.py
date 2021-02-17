'''
Given n non-negative integers a1, a2, ..., an , 
where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints 
of the line i is at (i, ai) and (i, 0). Find two lines,
 which, together with the x-axis forms a container, 
 such that the container contains the most water.

Notice that you may not slant the container.
'''
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