import dagshub
import mlflow

mlflow.set_tracking_uri("https://dagshub.com/Apoorv7668/MLOPS_Project.mlflow")

dagshub.init(repo_owner='Apoorv7668', repo_name='MLOPS_Project', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)