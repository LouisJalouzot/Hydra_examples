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

# Grid search on SLURM cluster (nothing saved)

```bash
python main.py -cn slurm_grid_search
```

# Optuna search (results saved in optuna.db)

```bash
python main.py -cn optuna
```

# Optuna search on SLURM cluster (results saved in optuna.db)

```bash
python main.py -cn optuna_slurm
```

# Explore optuna search results
Create another environment because of dependencies incompatibilities and install `optuna-dashboard`
```bash
uv venv .dashboard_venv --python=3.11.10
deactivate # If another environment is activated
source .dashboard_venv/bin/activate
uv pip install optuna-dashboard>=0.16.2
```

Upgrade the database and launch the dashboard
```bash
optuna storage upgrade --storage sqlite:///optuna.db
optuna-dashboard sqlite:///optuna.db
```