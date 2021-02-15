#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The algorithm is run O(n) times. This is because that's the number of times the calculation needs to be run for the value a to become equal to n*n*n is n because it's increased by n*n through each for loop pass.


b) The time complexity for this algorthm is O(n log n). This is because there are two different nested for loops that need to be taken into consideration when we are making our calculations. The first is a typical for loop that moves from 0 to the size n, and a second for loop whose calculations are halved because of variable being used as a condiditon for the while loop is constantly being doubled within the while loop, which wil half the number of times it's called. 


c) This algorithm is run O(n) times where n is the number of bunnies throw in as input. This is because the value of n is only decremented by a value of 1 each time the function is called, so it would call the function n number of times because n is how many subtractions would be required to get the input size to zero. 

## Exercise II

You should begin dropping eggs from the half way point of the stories of the buildings at n/2. If the egg doesn't break at the story height of n/2 that means that all of the values of n that are lower than n/2 can be discarded as not possible places where the will break because the heights are smaller. If the egg does break, and you want to find the first location where the egg starts breaking you can ignore the upper half of the story numbers n because if it already broke at n/2 then it will break at all values greater than n/2. This method is valuable because each possible variation of the egg breaking or not breaking n/2 will cut the sample size that you need to check in half.

drop_egg(floor/2):
   if egg is broken
      drop_eggs(floor-1)
   else:
      if floor is already visited
        return floor-1
      drop_eggs(floor+1)

   This algorithm would run with a O(N) time complexity where n corresponds to the number of floors. Despite the algorithms sample size halfing it is stil treated as an O(N) algorithm.


