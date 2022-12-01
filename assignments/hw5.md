## Divide and conquer assignment

* **Individual Assignment**
* **Due:** Nov 21

**How to subm it:**

* Follow the steps defined on this markdown.
* Create a Jupyter Notebook file with the solution and submit to your GitHub repository (same used for the other assignments). Name this file as `hw5.ipynb`
* Submit the solution to your GitHub.

I will evaluate the latest commit before the deadline.

**Due date:** November 29, 11:59 PM

---

# Instructions

Two positive integers always have common factors. For example, the common factors 12 and 18 are 1, 2, 3, and 6 because 12 and 18 are both divisible by these numbers.

The greatest common factor (GCF) of a number is the largest number by which both numbers are divisible. In the example, the number 6 is the GCF of 12 and 18.

There are at least two methods for calculating GCF of two numbers. One is the method of **successive divisions**. In this process, we make several divisions until we reach an exact division. The divisor of this division is the GCF. For example, for the 48 and 30 we have the following:

1. we divide the largest number by the smallest number:
   $48/30 = 1$ (with remainder of 18)

2. we divide 30 (the divisor of the previous division) by 18 (the remainder of the previous division) and so on:
   - $30/18 = 1$ (with remainder of 12)
   - $18/12 = 1$ (with remainder of 6)
   - $12/6 = 2$ (exact division)

3) The divisor of the exact division is 6. So the GCF of 48 and 30 is 6.

### Your task

Implement a "divide and conquer" function `GCF(a,b)` that solves the GCF problem for any two positive integers `a` and `b`.

Create a main program that tests your function with at least 4 different pairs of numbers. Provide the solution and an explanation of your solution in a notebook. Your explanation must include a description of what you have done to implement your `GCF()` function and a detailed example of how the function would behave for one particular pair of numbers (function calls, parameters, returns, program state).
