class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        leng = len(image)
        # lis = [[0] * leng for _ in range(leng)]
        for i in range(leng):
            a = 0
            b = leng - 1
            while a <= b:
                image[i][a], image[i][b] = 1-image[i][b], 1-image[i][a]
                a+=1
                b-=1
        return image