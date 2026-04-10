from prophecy_pipeline_sdk.graph import *
from prophecy_pipeline_sdk.properties import *
args = PipelineArgs(label = "sanity_parent_orchestration_pipeline_1", version = 1, auto_layout = False)

with Pipeline(args) as pipeline:
    s3source_1 = Process(
        name = "S3Source_1",
        properties = S3Source(
          connector = "s3",
          format = S3Source.CsvReadFormat(schema = "external_sources/sanity_parent_orchestration_pipeline_1/S3Source_1.yml"),
          properties = S3Source.S3SourceInternal(
            filePath = "/datasets/orchestration_datasets/csv/valid/9MB_annual-enterprise-survey-2023-financial-year-provisional.csv"
          )
        ),
        input_ports = None
    )
    env_uitesting_main_model_databricks_1_1 = Process(
        name = "env_uitesting_main_model_databricks_1_1",
        properties = ModelTransform(modelName = "env_uitesting_main_model_databricks_1"),
        is_custom_output_schema = True
    )
    sanity_parent_orchestration_pipeline_1__join_1 = Process(
        name = "sanity_parent_orchestration_pipeline_1__Join_1",
        properties = ModelTransform(modelName = "sanity_parent_orchestration_pipeline_1__Join_1"),
        input_ports = ["in_0", "in_1"]
    )
    send_danger_email = Process(
        name = "send_danger_email",
        properties = Email(
          body = "This is a dangerous email from sanity pipeline for parent databricks project",
          subject = "This is a dangerous email from sanity pipeline for parent databricks project",
          includeData = True,
          fileName = "sanity_parent_sql_databricks",
          to = ["abhisheks@prophecy.io"],
          bcc = ["abhisheks+bcc@prophecy.io"],
          cc = ["abhisheks+cc@prophecy.io"],
          connection = "smtp",
          fileFormat = "xlsx"
        ),
        output_ports = None,
        comment = "Sends a cautionary email from a sanity check, including data attachment for parent Databricks project."
    )
    s3source_1 >> sanity_parent_orchestration_pipeline_1__join_1._in(0)
    env_uitesting_main_model_databricks_1_1 >> sanity_parent_orchestration_pipeline_1__join_1._in(1)
    sanity_parent_orchestration_pipeline_1__join_1 >> send_danger_email
