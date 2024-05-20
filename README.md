# Chest_Disease_Classification_Using_CT_Scan


## Git commands

```bash
git add .
git commit -m "Updated"
git push origin main
```

# How to run
```bash
conda create -n chest python=3.8 -y
```

# Activate the environment
```bash
conda activate chest
```

# Install the packages
```bash
pip install -r requirements.txt
```

# Workflow

```
Update config.yaml
Update params.yaml
Update the entity
Update the configuration manager in src config
Update the components
Update the pipeline
Update the main.py
Update the dvc.yaml
```

# Mlflow dagshub connection uri

MLFLOW_TRACKING_URI=https://dagshub.com/nehatiwaribt/MLFLOW_Experiments.mlflow \
MLFLOW_TRACKING_USERNAME=nehatiwaribt \
MLFLOW_TRACKING_PASSWORD=69b7eff71c84adf740ce4cb88a58db53c7182365 \
python script.py

## RUN from bash terminal

export MLFLOW_TRACKING_URI=https://dagshub.com/nehatiwaribt/MLFLOW_Experiments.mlflow 

export MLFLOW_TRACKING_USERNAME=nehatiwaribt 

export MLFLOW_TRACKING_PASSWORD=69b7eff71c84adf740ce4cb88a58db53c7182365

## DVC cmd

dvc init
dvc repro
dvc dag

