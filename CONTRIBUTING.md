# Guidance on how to contribute

There are two primary ways to help:
 - Propose an exercise using the issue tracker, and
 - Propose a solution using the pull request

## Propose an exercise using the issue tracker

One generally uses the issue tracker to suggest feature requests, report bugs, and ask questions.
For our project, you are welcome to propose new exercises to be included in this project by creating an new issue.
Describe what you would like in this exercise and if possible propose what the solution should look like.

If you can write up the exercise statment or the codes for the solution, then follow the guide below.


##  Propose a solution using the pull request

### General github workflow

Generally speaking, you should fork this repository, make changes in your own fork, and then submit a pull request (PR). 
This is the primary way for you to submit solutions to the exercise in codes. 

If you are not familir with git, we follow the general ["fork-and-pull"](https://github.com/susam/gitpr) git flow:

1. Fork the repository to your own Github account.
2. Clone the project to your machine. Add upstream to the original repo.
3. Create a branch locally with a succinct but descriptive name (something like `dev-fix-something`). It is best practice not to work with the master branch.
4. Commit changes to the branch. Commit small changes often and commit frequently with succint and clear messages.
5. Following any formatting and testing guidelines specific to this repo.
6. Push changes to your fork. Keep your fork's main development branch updated with upstream's. If there are conflicts, resolve within your own forked version.
7. Open a PR in our repository and follow the PR template so that we can efficiently review the changes.
8. After reviewers approve the PR, your branch (and changes) will be merged to the master branch.
9. (Optionally) Delete your branch.


## Structuring the execise or solution

First, create the folder based on the next number of the project. For e.g., if you see `015` folder being the latest project folder, then create the `016` folder. Within that, the directory layout should be
    .
    ├── exercise                 # Exercise folder
    │   └── readme.md            # A mark-down clear and expansive description of the exercise. Data, goals, methods to use and etc
    ├── solution                 # Solution Folder
    │   ├── readme.me            # A short description on the solutions and what each file does
    │   └── random_forest.ipynb  # Jupyter notebook solution
    │   └── cnn.py               # A python .py solution
    │   └── ...



