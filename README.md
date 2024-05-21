# Chest-Disease-Classification-from-Chest-CT-Scan-Image


## Workflows

1. Update config.yaml
2. Update params.yaml
3. Update the entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline 
7. Update the main.py
8. Update the dvc.yaml 




## Git commands

```bash
git add .

git commit -m "Updated"

git push origin main
```

## How to run?

```bash
conda create -n chest python=3.8 -y
```

```bash
conda activate chest
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```

### Mlflow dagshub connection uri

```bash
MLFLOW_TRACKING_URI=https://dagshub.com/nehatiwaribt/Chest_Disease_Classification_Using_CT_Scan.mlflow\
MLFLOW_TRACKING_USERNAME=nehatiwaribt \
MLFLOW_TRACKING_PASSWORD=69b7eff71c84adf740ce4cb88a58db53c7182365   \
python script.py
```


### RUN from bash terminal

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/nehatiwaribt/Chest_Disease_Classification_Using_CT_Scan.mlflow

export MLFLOW_TRACKING_USERNAME=nehtiwaribt 

export MLFLOW_TRACKING_PASSWORD=69b7eff71c84adf740ce4cb88a58db53c7182365  

```



### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag