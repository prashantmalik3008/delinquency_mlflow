import dagshub
import mlflow

mlflow.set_tracking_uri('https://dagshub.com/prashantmalik3008/delinquency_mlflow.mlflow')
dagshub.init(repo_owner='prashantmalik3008', repo_name='delinquency_mlflow', mlflow=True)


with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)