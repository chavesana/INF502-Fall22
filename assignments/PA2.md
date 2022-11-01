# INF 502 - PA2
Programming Assignment 2 for INF 502.

**DUE DATE:** Dec 8, 2022 11:59 PM

**GROUP ASSIGNMENT:** You can solve this in groups of up to 4 students (2, 3, or 4 students).

**How to subm it:**
* Follow the steps defined on this markdown.
* Create a Jupyter Notebook file with the solution and submit to your GitHub repository (same used for the other assignments). Name this file as `PA2.ipynb`
  - make sure you add your names and GitHub username in the file, so I can connect the groups.
  - ALL the students in your group MUST SUBMIT the solution to your own GitHub, but they will be identical files. Please make sure you include the GitHub link to the assignment for both students in the head of your file (just like we have done for HW4), so I can easily switch from one GitHub to the other.

I will evaluate the latest commit before the deadline.

---

This assignment will asses your ability to write complete applications that deal with data collection and analysis in Python.
The focus will be on using all the knowledge acquired in this course, from basic Python to Pandas, using JSON, ploting data, etc.

**IMPORTANT:** This assignment will evolve during the following weeks, after we learn other contents. Start as soon as possible, and you'll understand the problem better as we move forward.

We're heading toward the end! I hope you have fun and enjoy! We're almost there!

---

## Context

In this assignment, we will work with real data from GitHub to understand the dynamics of repositories and developers who contribute to them. Your application will consume the [GitHub REST API](https://docs.github.com/en/free-pro-team@latest/rest) to collect information about repositories, pull requests, and users.

We will focus on the social side of software development. Therefore, we will also scrape data from their GitHub profile.

**Important:** Be aware of GitHub Terms of Service:

> 7. Information Usage Restrictions

>> You may use information from our Service for the following reasons, regardless of whether the information was scraped, collected through our API, or obtained otherwise:

>> Researchers may use public, non-personal information from the Service for research purposes, only if any publications resulting from that research are open access.
 Archivists may use public information from the Service for archival purposes.
Scraping refers to extracting information from our Service via an automated process, such as a bot or webcrawler. Scraping does not refer to the collection of information through our API. Please see Section H of our Terms of Service for our API Terms.

>> You may not use information from the Service (whether scraped, collected through our API, or obtained otherwise) for spamming purposes, including for the purposes of sending unsolicited emails to users or selling personal information, such as to recruiters, headhunters, and job boards.

>> Your use of information from the Service must comply with the GitHub Privacy Statement.

---

### Requirement 1: paradigm
You need to use object-oriented programming to deal with the data you are collecting and analyzing. The easy way to do this is by analyzing the structure of the `json` dictionary structure you obtain from the API. When you have nested elements, a new object *may* be necessary.

### Requirement 2: data
About repositories, we would like to keep the name, owner (login), description, homepage, license (can be another class), number of forks, watchers, and date_of_collection (the date you collect the data). When you request to print the object it should be like this:

* `Owner/RepositoryName: Description (# of watchers)`

Each repository also needs to be related to a list of pull requests. Thus, for each repo, you need to collect the pull requests that are returned in the first page of a query like this:

* `https://api.github.com/search/issues?q=is:pr+repo:jabref/jabref` (using repository jabref/jabref as an example)

For each pull request you need to keep: title, number, body, state, date of creation (created_at), 
closing date (if the state is different than open), user.

* For the last 4 fields  (number of commits, additions, deletions, changed_files. ), you will need to make another query using the following format (using the number of the pull requests you found before):

* `https://api.github.com/repos/JabRef/jabref/pulls/5531`

Then, for each author (user) you find in the pull requests, you need to keep the username and number of pull requests (calculated).

You are also required to *scrape* the following information from the user profile page on GitHub: 
Number of Repositories, Number of Followers, Number of Following, Number of contributions in the last year.

### Requirement 3: the data structure

You need to have a function called `to_CSV` that can be reused to convert any object to a csv entry (row). The function receives the file name and the object to be converted. If the file does not exist, you need to create the file (with a header). If the file  exists, you need to append a new line with the object in the CSV. To make it possible, you will need to have a method in each of your classes with the very same name, which will return a string with the data already structured as a CSV.

Use this function to create/update the files as following (NO REPEATED ENTRIES):

* when you collect data from a repo, you need to add it to a CSV called `repos.csv`
* when you collect the pull requests of a repo, you need to store them in a file named after the owner and the name of repo (repos/owner-repo.csv) 
* when you collect data from users, you need to add it to a CSV called `users.csv` 


### Requirement 4: functions to the user

A user may be able to:

* request the system to collect data for a specific repository (from GitHub). By providing the owner and repository name, your program needs to start the collection of everything
(repository, pull request, users -- including scraped data)
* list all repos collected
* list all pull requests from a repo (list the repos available, so the user will select an existing option)
* list the summary of a repo, containing:
   - number of pull requests in `open` state
   - number of pull requests in `closed` state
   - number of users
   - date of the oldest pull requested
   
* plot the data given a repo:
   - a boxplot that compares closed vs. open pull requests in terms of number of commits
   - a boxplot that compares closed vs. open pull requests in terms of additions and deletions
   - a boxplot that compares the number of changed files grouped by the author association
   - a scatterplot that shows the relationship between additions and deletions
 
 * plot the data about pull requests from ALL repos:
   - line graph showing the total number of pull requests per day
   - line graph comparing number of open and closed pull requests per day
   - bars comparing the number of users per repo

* calculate the correlation between the data collected for the users
(following, followers, number of pull requests, number of contributions, etc.)

* calculate the correlation between all the numeric data in the pull requests for a repo

### Requirement 5: Tests

You need to write at least 5 unit tests.
    
