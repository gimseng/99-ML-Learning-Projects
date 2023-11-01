# Guidance on how to contribute

There are two primary ways to help:

- Propose an exercise using the issue tracker, and
- Propose a solution using the pull request

## Propose an exercise using the issue tracker

One generally uses the issue tracker to suggest feature requests, report bugs, and ask questions.
For our project, you are welcome to propose new exercises to be included in this project by creating an new issue.
Describe what you would like in this exercise and if possible propose what the solution should look like.

If you can write up the exercise statment or the codes for the solution, then follow the guide below.

## Propose a solution using the pull request

### General github workflow

Generally speaking, you should fork this repository, make changes in your own fork, and then submit a pull request (PR).
This is the primary way for you to submit solutions to the exercise in codes.

If you are not familir with git, we follow the general ["fork-and-pull"](https://github.com/susam/gitpr) git flow:

1. Fork the repository to your own Github account.
2. Clone the project to your machine. Add upstream to the original repo.

- `git clone https://github.com/your_username/99-ML-Learning-Projects.git`
- `git remote add upstream https://github.com/gimseng/99-ML-Learning-Projects.git` so now `upstream` refers to the original repo and `origin` refers to the remote fork created.

3. Create a branch locally with a succinct but descriptive name (something like `dev-fix-something`). It is best practice not to work with the master branch.
   - `git branch dev-fix-something` this creates a new branch where your changes will be present in.
   - `git checkout dev-fix-something` this lets us switch to the new branch created
4. Commit changes to the branch. Commit small changes often and commit frequently with succint and clear messages.
   - make sure you are in the branch specific to the changes you want to commit
   - `git commit change-you-made`
5. Following any formatting and testing guidelines specific to this repo.
6. Push changes to your fork. Keep your fork's main development branch updated with upstream's. If there are conflicts, resolve within your own forked version.
   - `git push origin dev-fix-something` here we push our branch that has our changes to the remote fork.
   - Now we need to make sure the fork's main development branch is updated with upstream's
     - `git checkout master` to change back to the master branch
     - `git fetch upstream master` to get any changes from upstream to our local fork
     - `git merge upstream/master` to merge changes from upstream to our fork
     - `git push origin` to push the changes to our remote fork
7. Open a PR in our repository and follow the PR template so that we can efficiently review the changes.
   ![Imgur](https://i.imgur.com/Lrv6oOV.png)
   After pushing changes to the fork created, a button will appear which will allow for creating a pull request requesting changes made in the branch to be merged with the original repo
8. After reviewers approve the PR, your branch (and changes) will be merged to the master branch.
9. (Optionally) Delete your branch.

## Structuring the execise or solution

First, create the folder using a placeholder name, roughly related to the model/project goal/data. For e.g., if you are working on linear regression, you could create the folder `linear regression`. Within that, the directory layout should be of the following format:

    .
    ├── exercise                 # Exercise folder
    │   └── readme.md            # A mark-down clear and expansive description of the exercise. Data, goals, methods to use and etc
    ├── solution                 # Solution Folder
    │   ├── readme.md            # A short description on the solutions and what each file does
    │   └── random_forest.ipynb  # Jupyter notebook solution
    └── data                     # Data folder
        ├── train.csv            # Some data
        └── ...

Please provide a description/summary in the `readme.md` in each of the `exercise` and `solution` folders. If its appropriate, reference/credit sources. In the `data` folder, if relevant, provide a `readme.md` to describe the data and its source.

When we eventually merge, the root folder name of your project will be renamed numerically by chronological order.

## Documenting the exercise or solution

When creating the `readme.md`, make sure to follow the below format. This ensures that each project contains the same level of information, providing a more complete experience for the user. Fomat as follow:

1. Exercise Goal
   - This should give a brief explanation of what the exercise is for and what the goal of the solution shold be. Users should be able to tell from this summary whether or not they are interested in completing the exercise.
2. Tasks
   - This should contain tasks the user needs to complete to create a solution for the exercise. Tasks can be either broad or specific, but should be relevant to the solution of the exercise.
3. Skills
   - This can either be dedicated to skills the user needs in order to complete the exercise, or skills that they will develop by completing the exercise. In either case, ensure that skills are labeled so that the user knows if they need to have prior knowledge to gain value from completing the exercise.
4. Resources
   - This section is optional, but encouraged. Resources can be tutorials or documentation on packages or libraries needed to complete the task, articles related to the topic it is focused on, or even other projects in the repository. Anything that could be of use to the user in creating a solution should be included in this section. 
5. Data Information
   - This should contain a brief background on any data included in the exercise. Although the bulk of this explanation will be located in the data subdirectory itself, this section should consist of short summary of that information.
6. Reference / Acknowledgements
    - This section is also optional depending on if there are any neccesary citations or acknolwedgments needed for the exercise.
7. Additional Sections
   - Additional sections can be added if needed. However, please only do so AFTER the sections listed above. This ensures that users can find all of this information in an expected place. 


