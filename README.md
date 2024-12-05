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

# Explore optuna search results (open in firefox)

```bash
optuna-dashboard sqlite:///optuna.db
```