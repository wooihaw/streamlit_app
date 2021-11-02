from sklearn.model_selection import train_test_split as split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from pandas import read_csv
from joblib import dump

df = read_csv('../data/genders_heights_weights.csv')
X =  df.values[:, 1:]
y = df.values[:, 0]

X_train, X_test, y_train, y_test = split(X, y, stratify=y, random_state=42)

params = {}
params['C'] = [0.001, 0.01, 0.1, 1, 10, 100]
gs = GridSearchCV(LogisticRegression(), params, n_jobs=-1, verbose=1).fit(X_train, y_train)

print(gs.best_params_, gs.best_score_)

lgr = LogisticRegression(**gs.best_params_).fit(X_train, y_train)
print(lgr.score(X_test, y_test))

dump(lgr, 'lgr_model.job')
