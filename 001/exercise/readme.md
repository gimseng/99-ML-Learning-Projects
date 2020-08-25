# 👋🛳️ Ahoy, Welcome to your first ML project.

This is one of the first newbie challenge/problem that you should be doing to enter into the world of ML.

We will use machine learning to create a model that predicts which passengers survived the Titanic shipwreck.

# THE CHALLENGE

The sinking of the Titanic is one of the most infamous shipwrecks in history.
On April 15, 1912, during her maiden voyage, the widely considered “unsinkable” RMS Titanic sank after colliding with an iceberg. Unfortunately, there weren’t enough lifeboats for everyone onboard, resulting in the death of 1502 out of 2224 passengers and crew.

While there was some element of luck involved in surviving, it seems some groups of people were more likely to survive than others.

In this challenge, we ask you to build a predictive model that answers the question: “what sorts of people were more likely to survive?” using passenger data (ie name, age, gender, socio-economic class, etc).
In this competition, you’ll gain access to two similar datasets that include passenger information like name, age, gender, socio-economic class, etc. One dataset is titled `train.csv` and the other is titled `test.csv`.

The file `train.csv` will contain the details of a subset of the passengers on board (891 to be exact) and importantly, will reveal whether they survived or not, also known as the “ground truth”.

The `test.csv` dataset contains similar information but does not disclose the “ground truth” for each passenger. It’s your job to predict these outcomes.

Using the patterns you find in the `train.csv` data, predict whether the other 418 passengers on board (found in `test.csv`) survived.

# Tasks

Most Machine learning projects usually follow a similar outline (a set of phases) which are listed below to help you get started.

- Inspecting Data (this process is where you familiarize yourself with the data)
    - Inspect the data
    - Check for Null Values 
    - View statistical details using ``describe()``

    What can you infer from the statistical measures? Like possible outliers? 
    
- Data Analysis and Visualization (this process is where you explore the data, clean it and infer some insights from it)
    
    - Delete columns irrelevant or not useful for prediction
    - Get the average rate of survival by Gender, Pclass
    - Plotting the number of people who survived and who didn't survive
    - Plot the precenrage of survival by gender
    - Handle null/missing values 
    - Plot the survival rate by Age
    - Handle categorical text values and turn them into numerical
    - Plot the correlation between features and label

    What do you infer from the data? What can you conclude from it? Who is most likely to survive, based on the data?

- Model Building and Evaluation (this process is where you start building models and choose a model based on accuracy metrics)
    - Choose a model suitable for classification
    - Fit the training (and possible validation) data
    - Use cross-validation to get the average accuracy for model selections or accuracy benchmark
    - Find out how "well" the model performs on test data using some metrics
    - **Bonus**: Try other classification algorithms and compare the accuracy metrics by presenting them in a readable, easy to compare format
        - Choose the model with the best accuracy metric


Source: https://www.kaggle.com/c/titanic
