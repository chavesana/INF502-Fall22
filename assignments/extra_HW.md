# Extra-credit: in-class assignment

**GROUP ASSIGNMENT:** You can solve this in groups of up to 4 students (2, 3, or 4 students).

**How to subm it:**

* Follow the steps defined on this markdown.
* Create a Jupyter Notebook file with the solution and submit to your GitHub repository (same used for the other assignments). Name this file as `extra_HW.ipynb`
  - make sure you add your names and GitHub username in the file, so I can connect the groups.
  - ALL the students in your group MUST SUBMIT the solution to your own GitHub, but they will be identical files. Please make sure you include the GitHub link to the assignment for both students in the head of your file (just like we have done for HW4), so I can easily switch from one GitHub to the other.

I will evaluate the latest commit before the deadline.

**Due date:** November 10, 11:59 PM

**Points:** 20 points, which will count as extra credit points in the HW rubric.

---

### Instructions

1. You are required to write a function that scrapes the Wikipedia article with the list of countries by population (Main Table) (https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population_density). 

We do not want to collect the data related to "World" (Find a way to skip these lines).

Collect the following information:

* Country name
* Area ($km^2$)
* Area ($mi^2$)
* Population

2. Store the data into a Pandas Dataframe. Make sure you have the numeric columns as numbers.

3. Provide a summary of the data (average, mean, etc. What information is relevant to explore the data?)

4. Calculate the correlation between the columns.

5. Plot a scatterplot (population vs. area ($km^2$))
