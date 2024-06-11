Advanced Machine Learning for NBA Draft Prediction
=====================================================
This repository contains the project "Advanced Machine Learning for NBA Draft Prediction," which focuses on building predictive models to determine if college basketball players will be drafted into the NBA. Using various machine learning techniques, we analyze player performance, draft-related data, and game-specific attributes to create classification models. The effectiveness of these models is evaluated using AU ROC scores on validation datasets.

Weekly Progress
-------------------------------------------------------

Week-1 XGBoost 
-------------------------------------------------------
Implemented XGBoost to predict the drafting probabilities of players based on multiple independent features.


Week-2 AdaBoost with Automated Hyperparameter Tuning
-----------------------------------------------------
Used AdaBoost with automated hyperparameter tuning to enhance the prediction accuracy of drafting probabilities.

Week-3 XGBoost with Automated Hyperparameter Tuning
-------------------------------------------------------
Refined the XGBoost model with automated hyperparameter tuning to improve prediction outcomes.

Week-4 Gradient Boost with Automated Hyperparameter Tuning
-------------------------------------------------------
Applied Gradient Boosting with automated hyperparameter tuning to predict drafting probabilities, aiming for higher accuracy.


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>


Initializing and Pushing to a Remote Repository
-------------------------------------------------
1. Initialize Repository: git init initializes a new Git repository.
 
2. Add Remote Repository: git remote add origin git@github.com:bhutanisaumya/Adv_MLA.git sets up the remote repository.
 
3. Stage Changes: git add . stages all changes in the current directory.
      
4. Commit Changes: git commit -m "first commit" commits the staged changes.
 
5. Push to Remote: git push --set-upstream origin main pushes the committed changes to the remote repository's main branch.




Steps to access the Project
-------------------------------
1. Clone the Repository:
 Use git clone to copy the project files to your local computer.

2. Access the Reository:
 Open the command prompt and navigate to the cloned project's directory.

3. Create a virtual setting:
Set up a separate environment for the project's dependencies to avoid conflicts with other projects.

4. Install Requirements:
Use pip install -r requirements.txt to install the necessary libraries.

5. Execute the Code:
Run the provided Jupyter notebooks to execute the code.

