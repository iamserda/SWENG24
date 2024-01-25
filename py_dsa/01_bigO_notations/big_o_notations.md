# Notes on Big O Notations

## What is BigO Notation?

A way of comparing code based on their efficiency.

### What is "Time Complexity?"

How our code behaves relative to cycles of work, speed, as the number of inputs grows?

- Does it get slower?
- Does stay the same?

### What is "Space Complexity?"

How much memory does our solution requires as the number of inputs increases?

- Does the space remain the same.
- Does it increase? How fast? Linear, Exponential, Constant?

Big O Notations: Best, Average and Worst cases
Omega: "Best-case", or the most efficient we can expect from a routine.
Theta: "Average-case" usually mid-way between the worst and the best case.
Omicron(O in Big O): "Worst-case" case, the least efficient case for a solution.
ex: `[11, 5, 16, 9, 55]`, if we had to look for a number in this array, if the number is 11, we would find it immediately because it is right at the beginning. That's Omega.
If we were looking for `16` we would get it in average, mid-way through the array.
If we were looking for `55` or a number that's not there like `56`, we would need O(n) operations to find `55` or to realize `56` is NOT in the array.

So why is Omega and Tetha NOT as important as Omicron?
You can think of it this way. If you were to be given a car with a full tank of gas, and were told to cross a desert. Within the desert, there are no other gas stations. No place to get water until you have crossed. What would you want to know?

- Some may want to know, on average, how successful are people at crossing the dessert?
- Some may want to know how much gas does it take to cross the desert on average?

These are fine questions but one who truly cares about survival would ask:

- What happens in the worst-case? What if I get lost in the desert and run out of gas?
- What if the tank leaked or sands got into the engine.
- These may not be cases that always happened but they are possible and likely.

In building a new software, you may expect 1000 users. So you structure your code and it works well for 1000 users. But unless you have strictly restricted the system to always be 1000 users, there is a chance that you may get 1001, 1002.... 1M.... 10M. What happens to your code if your product is reviewed by a Tik-Toker and all of a sudden you are flooded with users who want to sign up. Or your marketplace goes from 100 items to 10,000 items. How does that affect your search. You would want to know what is the worst case when searching for a product or a user's login. You want to know that because it may not happened but it is still a likely possibility that the very last user wants to login. If your search is linear, that person would need to wait a long time to login as the system compares their username with every other usernames in the database.

#### O(1): Constant time-complexity: read as "constant-time" or "oh of 1"

It does NOT mean 1 operations or 1 routine or 1 run or 1 work.

Instead, O(1) means `the number of work remains UNCHANGED regardless of the input.` If we have an input "n", and a function `f` then `f(n)` for `n = 1` is the same amount of work done when `n = 1000`. So if f(1) completes 10 work to return a result, f(infinity - 1) MUST also complete 10 steps and return the result. It should be done faster or slower. 10 steps for 1, 10 steps for infinity - 1.
See `linear-tc.md` for an example.

#### O(log n):Constant time-complexity: reads "oh of log n"

O(log n) running time, it means that as the input size grows, the number of operations grows very slowly.
See `quadratic-tc.md` for an example.

