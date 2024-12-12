# Create a virtual environment and activate it
```bash
uv sync
source .venv/bin/activate
```

# Default run (nothing saved)

```bash
python main.py
```

# Simple grid search (nothing saved)

```bash
python main.py -cn grid_search
```

# Optuna search (results saved in optuna.db)

You can stop and restart the script, optuna will look into the database to continue the search from where it stopped
```bash
python main.py -cn optuna
```

# Grid search or optuna search in parallel using joblib or on SLURM cluster

Beware that you need an existing directory `outputs` for the scripts to launch correctly.
```bash
python main.py -cn grid_search_joblib
python main.py -cn grid_search_slurm
python main.py -cn optuna_joblib
python main.py -cn optuna_slurm
```

# Explore optuna search results
Create another environment because of dependencies incompatibilities and install `optuna-dashboard`
```bash
uv venv .dashboard_venv --python=3.11.10
deactivate # If another environment is activated
source .dashboard_venv/bin/activate
uv pip install "optuna-dashboard>=0.16.2"
```

`optuna-dashboard` requires to update the database but you need to keep the original one for the script to continue using it.

Therefore you can copy and upgrade the database and launch the dashboard with
```bash
cp optuna.db optuna_up.db
optuna storage upgrade --storage sqlite:///optuna_up.db
optuna-dashboard sqlite:///optuna_up.db
```