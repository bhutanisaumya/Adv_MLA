from sklearn.metrics import roc_auc_score, accuracy_score

def evaluate_classifier(classifier, X_train, y_train, X_val, y_val):
    # Model's prediction on the training set
    y_pred_train = classifier.predict(X_train)

    # ROC AUC score on the training set
    auc_train = roc_auc_score(y_train, y_pred_train)
    print(f'ROC AUC score on training set: {auc_train:.4f}')
    
    # Model's prediction on the validation set
    y_pred_val = classifier.predict(X_val)
    
    # ROC AUC score on the validation set
    auc_val = roc_auc_score(y_val, y_pred_val)
    print(f'ROC AUC score on validation set: {auc_val:.4f}')
    
    # Accuracy score on the validation set
    accuracy_val = accuracy_score(y_val, y_pred_val)
    print(f'Accuracy score on validation set: {accuracy_val:.4f}')



#evaluate_classifier(gb_classifier1, X_train_scaled, y_sm, X_val_scaled, y_val)
