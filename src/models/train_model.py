
from sklearn.ensemble import GradientBoostingClassifier, AdaBoostClassifier
from sklearn.metrics import f1_score, accuracy_score, roc_auc_score
from sklearn.model_selection import GridSearchCV
from xgboost import XGBClassifier

def train_gb_classifier(X_train, y_train):
    # Define hyperparameters for GradientBoostingClassifier
    hyperparameters = {
        'learning_rate': 0.1,
        'n_estimators': 100,
        'max_depth': 1,
        'random_state': 42
    }
    
    # Instantiate a GradientBoostingClassifier with specified hyperparameters
    gb_classifier = GradientBoostingClassifier(**hyperparameters)
    
    # Fit the GradientBoostingClassifier model with the training data
    gb_classifier.fit(X_train, y_train)
    
    return gb_classifier  # Return the trained classifier

def train_adaboost_classifier(X_train, y_train):
    # Define hyperparameters for AdaBoostClassifier
    hyperparameters = {
        'learning_rate': 0.5,
        'n_estimators': 200,
        'random_state': 43
    }
    
    # Instantiate an AdaBoostClassifier with specified hyperparameters
    adab_classifier = AdaBoostClassifier(**hyperparameters)
    
    # Fit the AdaBoostClassifier model with the training data
    adab_classifier.fit(X_train, y_train)
    
    return adab_classifier  # Return the trained classifier

def train_xgb_classifier(X_train, y_train):
    # Define hyperparameters for XGBClassifier
    hyperparameters = {
        'colsample_bytree': 0.8,
        'learning_rate': 0.01,
        'max_depth': 4,
        'min_child_weight': 1,
        'n_estimators': 200,
        'subsample': 0.8,
        'reg_lambda': 0.5,
        'random_state': 42
    }
    
    # Instantiate an XGBClassifier with specified hyperparameters
    xgb_classifier = XGBClassifier(**hyperparameters)
    
    # Fit the XGBClassifier model with the training data
    xgb_classifier.fit(X_train, y_train)
    
    return xgb_classifier  # Return the trained classifier
