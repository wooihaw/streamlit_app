from pandas import read_csv
from sklearn.model_selection import train_test_split as split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from joblib import dump

csv_file = "https://raw.githubusercontent.com/wooihaw/datasets/main/heights_weights_genders.csv"
df = read_csv(csv_file)
X = df.drop("Gender", axis=1)
y = df["Gender"]
X_train, X_test, y_train, y_test = split(X, y, stratify=y, test_size=0.3, random_state=42)

params = {}
params["C"] = [0.001, 0.01, 0.1, 1, 10, 100]
params["penalty"] = ['none', "l2"]
params["solver"] = ["lbfgs", "saga", "newton-cg", "sag"]
gs = GridSearchCV(LogisticRegression(), params, n_jobs=-1, verbose=1).fit(
    X_train, y_train
)

print(gs.best_params_, gs.best_score_)

lgr = LogisticRegression(**gs.best_params_).fit(X_train, y_train)
print(f"{lgr.score(X_test, y_test)=:.3%}")

dump(lgr, "lgr_model.job")
