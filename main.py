import hydra
from omegaconf import DictConfig
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


@hydra.main(
    config_path="conf", config_name="config", version_base=hydra.__version__
)
def main(cfg: DictConfig):
    X, y = make_classification(random_state=0)
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = RandomForestClassifier(
        criterion=cfg.criterion,
        n_estimators=cfg.n_estimators,
        max_depth=cfg.max_depth,
        random_state=0,
    )
    model.fit(X_train, y_train)
    val_predicted = model.predict(X_val)
    val_accuracy = accuracy_score(y_val, val_predicted)

    return val_accuracy


if __name__ == "__main__":
    main()
