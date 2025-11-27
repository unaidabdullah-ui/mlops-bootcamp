from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, r2_score
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

def train_models(df, target):
    X = df.drop(columns=[target])
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    problem_type = "regression" if y.dtype != "object" else "classification"

    results = {}

    if problem_type == "regression":
        models = {
            "LinearRegression": LinearRegression(),
            "RandomForestRegressor": RandomForestRegressor()
        }
        metric = r2_score

    else:
        models = {
            "LogisticRegression": LogisticRegression(),
            "RandomForestClassifier": RandomForestClassifier()
        }
        metric = accuracy_score

    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        score = metric(y_test, preds)
        results[name] = round(score, 4)

    best_model = max(results, key=results.get)
    return models[best_model], results
