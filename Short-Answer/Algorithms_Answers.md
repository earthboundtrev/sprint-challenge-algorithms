#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The algorithm is run O(n) times. This is because that's the number of times the calculation needs to be run for the value a to become equal to n*n*n cubed since it's increased by n*n through each for loop pass.


b) The time complexity for this algorthm is O(n log n). This is because there are two different nested for loops that need to be taken into consideration when we are making our calculations. The first is a typical for loop that moves from 0 to the size in, and a second for loop whose calculations are halved because of variable being used for the while loop is constantly being doubled. 


c) This algorithm is run O(n) times where n is the number of bunnies throw in as input. This is because the value of n is only decremented by a value of 1 each time the function is called, so it would call the function n number of times because n is how many subtractions would be required to get the input size to zero. 

## Exercise II

You should drop all of the eggs carefully and gently staring from the first floor. In this way you can assure that floor is at the smallest possible value, and a lot of eggs will break along the way, but fewer will break this way then from staring from the top

drop_egg(floor):
   if eggs == broken
      return floor
   else:
      drop_eggs(floor+1)


