# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        inDeegre = [len(i) for i in ingredients]
        graph = defaultdict(list)
        for i in range(len(recipes)):
            for node in ingredients[i]:
                graph[node].append((recipes[i], i))
        ans = []
        queue = deque(supplies)
        while queue:
            x = queue.popleft()
            for node in graph[x]:
                inDeegre[node[1]] -= 1
                if inDeegre[node[1]] == 0:
                    ans.append(node[0])
                    queue.append(node[0])
        return ans
