class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        keepGoing = True
        sol = 0
        

        while (keepGoing):
            keepGoing = False
            nextBoxes = []
            for box in initialBoxes:
                if (status[box]):
                    sol += candies[box]
                    keepGoing = True
                    for newBox in (containedBoxes[box]):
                        nextBoxes.append(newBox)
                    for newKey in keys[box]:
                        status[newKey] = True
                else:
                    nextBoxes.append(box)
            
            initialBoxes = nextBoxes
        return sol