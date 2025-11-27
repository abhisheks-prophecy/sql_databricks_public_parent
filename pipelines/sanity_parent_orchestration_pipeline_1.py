with DAG():
    Join_1 = Task(
        task_id = "Join_1", 
        component = "Join", 
        conditions = [{"alias" : "in1", "expression" : {"expression" : "in0.Year!=in1.p_int"}, "joinType" : "inner"}], 
        expressions = [{"expression" : {"expression" : "in0.Year"}, "alias" : "Year", "_row_id" : "946204249"},          {
           "expression": {"expression" : "in0.Industry_aggregation_NZSIOC"}, 
           "alias": "Industry_aggregation_NZSIOC", 
           "_row_id": "1176669989"
         },          {
           "expression": {"expression" : "in0.Industry_code_NZSIOC"}, 
           "alias": "Industry_code_NZSIOC", 
           "_row_id": "512373631"
         },          {
           "expression": {"expression" : "in0.Industry_name_NZSIOC"}, 
           "alias": "Industry_name_NZSIOC", 
           "_row_id": "800819083"
         },          {"expression" : {"expression" : "in0.Units"}, "alias" : "Units", "_row_id" : "1265429051"},          {"expression" : {"expression" : "in0.Variable_code"}, "alias" : "Variable_code", "_row_id" : "408359860"},          {"expression" : {"expression" : "in0.Variable_name"}, "alias" : "Variable_name", "_row_id" : "1184240860"},          {"expression" : {"expression" : "in0.Variable_category"}, "alias" : "Variable_category", "_row_id" : "91409689"},          {"expression" : {"expression" : "in0.Value"}, "alias" : "Value", "_row_id" : "868772804"},          {
           "expression": {"expression" : "in0.Industry_code_ANZSIC06"}, 
           "alias": "Industry_code_ANZSIC06", 
           "_row_id": "1794245626"
         },          {"expression" : {"expression" : "in1.c_array"}, "alias" : "c_array", "_row_id" : "1815491843"},          {"expression" : {"expression" : "in1.c_struct"}, "alias" : "c_struct", "_row_id" : "41391956"},          {"expression" : {"expression" : "in1.p_string"}, "alias" : "p_string", "_row_id" : "1871610112"},          {"expression" : {"expression" : "in1.c_int"}, "alias" : "c_int", "_row_id" : "611720632"},          {"expression" : {"expression" : "in1.c_float"}, "alias" : "c_float", "_row_id" : "1740915852"},          {"expression" : {"expression" : "in1.c_boolean"}, "alias" : "c_boolean", "_row_id" : "2101590630"},          {"expression" : {"expression" : "in1.c_double"}, "alias" : "c_double", "_row_id" : "645177296"},          {"expression" : {"expression" : "in1.c_id"}, "alias" : "c_id", "_row_id" : "9649701"}], 
        activeTab = "conditions", 
        columnsSelector = [         "8-feNove7Bs0VviWp3xX9$$T71qBqKi7bcktRx0Y-Tmb##p_int",          "8-feNove7Bs0VviWp3xX9$$T71qBqKi7bcktRx0Y-Tmb##c_array",          "8-feNove7Bs0VviWp3xX9$$T71qBqKi7bcktRx0Y-Tmb##c_struct",          "8-feNove7Bs0VviWp3xX9$$T71qBqKi7bcktRx0Y-Tmb##p_string",          "8-feNove7Bs0VviWp3xX9$$T71qBqKi7bcktRx0Y-Tmb##c_int",          "8-feNove7Bs0VviWp3xX9$$T71qBqKi7bcktRx0Y-Tmb##c_float",          "8-feNove7Bs0VviWp3xX9$$T71qBqKi7bcktRx0Y-Tmb##c_boolean",          "8-feNove7Bs0VviWp3xX9$$T71qBqKi7bcktRx0Y-Tmb##c_double",          "8-feNove7Bs0VviWp3xX9$$T71qBqKi7bcktRx0Y-Tmb##c_id"], 
        headAlias = "in0"
    )
    SetOperation_1 = Task(
        task_id = "SetOperation_1", 
        component = "SetOperation", 
        operationType = "union", 
        preserveDuplicates = False, 
        useMinus = False, 
        inputAliases = ["in0", "in1"]
    )
    industry_data_by_year = Task(
        task_id = "industry_data_by_year", 
        component = "Reformat", 
        columnsSelector = [         "3GJQ5BE6pT_AekQrGQJ8H$$Jy_WVb-XM5VtupVwD5uNZ##Year",          "3GJQ5BE6pT_AekQrGQJ8H$$Jy_WVb-XM5VtupVwD5uNZ##Industry_aggregation_NZSIOC",          "3GJQ5BE6pT_AekQrGQJ8H$$Jy_WVb-XM5VtupVwD5uNZ##Industry_code_NZSIOC",          "3GJQ5BE6pT_AekQrGQJ8H$$Jy_WVb-XM5VtupVwD5uNZ##Industry_name_NZSIOC",          "3GJQ5BE6pT_AekQrGQJ8H$$Jy_WVb-XM5VtupVwD5uNZ##Units",          "3GJQ5BE6pT_AekQrGQJ8H$$Jy_WVb-XM5VtupVwD5uNZ##Variable_code",          "3GJQ5BE6pT_AekQrGQJ8H$$Jy_WVb-XM5VtupVwD5uNZ##Variable_name",          "3GJQ5BE6pT_AekQrGQJ8H$$Jy_WVb-XM5VtupVwD5uNZ##Variable_category",          "3GJQ5BE6pT_AekQrGQJ8H$$Jy_WVb-XM5VtupVwD5uNZ##Value",          "3GJQ5BE6pT_AekQrGQJ8H$$Jy_WVb-XM5VtupVwD5uNZ##Industry_code_ANZSIC06"], 
        expressions = [{"expression" : {"expression" : "Year"}, "alias" : "Year", "_row_id" : "734491227"},          {
           "expression": {"expression" : "Industry_aggregation_NZSIOC"}, 
           "alias": "Industry_aggregation_NZSIOC", 
           "_row_id": "272373540"
         },          {
           "expression": {"expression" : "Industry_code_NZSIOC"}, 
           "alias": "Industry_code_NZSIOC", 
           "_row_id": "1826467208"
         },          {"expression" : {"expression" : "Industry_name_NZSIOC"}, "alias" : "Industry_name_NZSIOC", "_row_id" : "514055851"},          {"expression" : {"expression" : "Units"}, "alias" : "Units", "_row_id" : "724308560"},          {"expression" : {"expression" : "Variable_code"}, "alias" : "Variable_code", "_row_id" : "701552096"},          {"expression" : {"expression" : "Variable_name"}, "alias" : "Variable_name", "_row_id" : "1161051806"},          {"expression" : {"expression" : "Variable_category"}, "alias" : "Variable_category", "_row_id" : "1965703473"},          {"expression" : {"expression" : "Value"}, "alias" : "Value", "_row_id" : "630174067"},          {
           "expression": {"expression" : "Industry_code_ANZSIC06"}, 
           "alias": "Industry_code_ANZSIC06", 
           "_row_id": "1112211330"
         }]
    )
    SQLStatement_1 = Task(
        task_id = "SQLStatement_1", 
        component = "SQLStatement", 
        fileTabs = [{"path" : "out", "id" : "out", "language" : "sql", "content" : "select * from SetOperation_1"}]
    )
    ordered_by_year = Task(
        task_id = "ordered_by_year", 
        component = "OrderBy", 
        columnsSelector = [         "hbC8g47rNx88OHrTIVAF-$$mGhAMktxY-5M3l8aoo0wC##Year",          "hbC8g47rNx88OHrTIVAF-$$mGhAMktxY-5M3l8aoo0wC##Industry_aggregation_NZSIOC"], 
        orders = [{"expression" : {"expression" : "Year"}, "sortType" : "asc"},          {"expression" : {"expression" : "Industry_aggregation_NZSIOC"}, "sortType" : "desc"}]
    )
    S3Source_1 = SourceTask(
        task_id = "S3Source_1", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3", id = "s3"), 
        format = CSVFormat(
          header = True, 
          schema = {
            "fields": [{
                          "dataType": {"type" : "Bigint"}, 
                          "description": "The year in which the data was collected.", 
                          "name": "Year"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "The classification of industries based on the New Zealand Standard Industry Output Classification.", 
                          "name": "Industry_aggregation_NZSIOC"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "Code representing the industry classification according to NZSIOC standards", 
                          "name": "Industry_code_NZSIOC"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "Name of the industry as per the NZSIOC classification", 
                          "name": "Industry_name_NZSIOC"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "The measurement units used for the data values", 
                          "name": "Units"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "Code representing the specific variable being measured", 
                          "name": "Variable_code"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "Name of the variable being measured in the dataset", 
                          "name": "Variable_name"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "Category classification of the variable being measured", 
                          "name": "Variable_category"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "The measured value associated with the industry data", 
                          "name": "Value"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "The code representing the industry classification according to ANZSIC 2006 standards.", 
                          "name": "Industry_code_ANZSIC06"
                        }], 
            "providerType": "arrow"
          }, 
          separator = ","
        ), 
        filePath = "/datasets/orchestration_datasets/csv/valid/9MB_annual-enterprise-survey-2023-financial-year-provisional.csv"
    )
    Aggregate_1 = Task(
        task_id = "Aggregate_1", 
        component = "Aggregate", 
        aggregate = [{"expression" : {"expression" : "any_value(Year)"}, "alias" : "Year", "_row_id" : "1242836399"},          {
           "expression": {"expression" : "any_value(Industry_aggregation_NZSIOC)"}, 
           "alias": "Industry_aggregation_NZSIOC", 
           "_row_id": "1246450168"
         },          {
           "expression": {"expression" : "any_value(Industry_code_NZSIOC)"}, 
           "alias": "Industry_code_NZSIOC", 
           "_row_id": "1325563384"
         },          {
           "expression": {"expression" : "any_value(Industry_name_NZSIOC)"}, 
           "alias": "Industry_name_NZSIOC", 
           "_row_id": "1085368753"
         },          {"expression" : {"expression" : "any_value(Units)"}, "alias" : "Units", "_row_id" : "547542453"},          {"expression" : {"expression" : "any_value(Variable_code)"}, "alias" : "Variable_code", "_row_id" : "600846907"},          {"expression" : {"expression" : "any_value(Variable_name)"}, "alias" : "Variable_name", "_row_id" : "896049477"},          {
           "expression": {"expression" : "any_value(Variable_category)"}, 
           "alias": "Variable_category", 
           "_row_id": "1608692147"
         },          {"expression" : {"expression" : "any_value(Value)"}, "alias" : "Value", "_row_id" : "925564803"},          {
           "expression": {"expression" : "any_value(Industry_code_ANZSIC06)"}, 
           "alias": "Industry_code_ANZSIC06", 
           "_row_id": "1197268180"
         }], 
        allowSelection = True, 
        condition = {"expression" : ""}, 
        activeTab = "aggregate", 
        columnsSelector = [         "J8BuGsnd84bJrXkbmTQpD$$M9iD2yScm3RWfbp_Z6lYA##Year",          "J8BuGsnd84bJrXkbmTQpD$$M9iD2yScm3RWfbp_Z6lYA##Industry_aggregation_NZSIOC",          "J8BuGsnd84bJrXkbmTQpD$$M9iD2yScm3RWfbp_Z6lYA##Industry_code_NZSIOC",          "J8BuGsnd84bJrXkbmTQpD$$M9iD2yScm3RWfbp_Z6lYA##Industry_name_NZSIOC",          "J8BuGsnd84bJrXkbmTQpD$$M9iD2yScm3RWfbp_Z6lYA##Units",          "J8BuGsnd84bJrXkbmTQpD$$M9iD2yScm3RWfbp_Z6lYA##Variable_code",          "J8BuGsnd84bJrXkbmTQpD$$M9iD2yScm3RWfbp_Z6lYA##Variable_name",          "J8BuGsnd84bJrXkbmTQpD$$M9iD2yScm3RWfbp_Z6lYA##Variable_category",          "J8BuGsnd84bJrXkbmTQpD$$M9iD2yScm3RWfbp_Z6lYA##Value",          "J8BuGsnd84bJrXkbmTQpD$$M9iD2yScm3RWfbp_Z6lYA##Industry_code_ANZSIC06"], 
        groupBy = [{"expression" : {"expression" : "Year"}, "alias" : "", "_row_id" : "zqDhM9r1l6"}]
    )
    env_uitesting_main_model_databricks_1_1 = Task(
        task_id = "env_uitesting_main_model_databricks_1_1", 
        component = "Model", 
        modelName = "env_uitesting_main_model_databricks_1"
    )
    send_danger_email = Task(
        task_id = "send_danger_email", 
        component = "Email", 
        body = "This is a dangerous email from sanity pipeline for parent databricks project", 
        subject = "This is a dangerous email from sanity pipeline for parent databricks project", 
        includeData = True, 
        fileName = "sanity_parent_sql_databricks", 
        to = ["abhisheks@prophecy.io"], 
        bcc = ["abhisheks+bcc@prophecy.io"], 
        cc = ["abhisheks+cc@prophecy.io"], 
        connection = Connection(kind = "smtp", id = "smtp"), 
        fileFormat = "xlsx"
    )
    S3Source_1.out0 >> ordered_by_year.in0
    ordered_by_year.out >> industry_data_by_year.in0
    env_uitesting_main_model_databricks_1_1.out >> Join_1.in1
    Aggregate_1.out >> [SetOperation_1.in0, SetOperation_1.in1]
    Join_1.out >> send_danger_email.in0
    SetOperation_1.out >> SQLStatement_1.in0
    SQLStatement_1.out >> Join_1.in0
    industry_data_by_year.out >> Aggregate_1.in0
