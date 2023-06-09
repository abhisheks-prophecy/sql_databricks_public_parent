WITH all_type_non_partitioned AS (

  SELECT * 
  
  FROM {{ source('alias_spark_catalog_qa_db_warehouse', 'all_type_non_partitioned') }}

),

all_type_partitioned AS (

  SELECT * 
  
  FROM {{ source('alias_spark_catalog_qa_db_warehouse', 'all_type_partitioned') }}

),

Join_1 AS (

  {#asd
  asdasddasd#}
  SELECT 
    all_type_partitioned.p_int AS p_int,
    all_type_partitioned.p_string AS p_string,
    all_type_non_partitioned.c_string AS c_string,
    all_type_non_partitioned.c_int AS c_int,
    all_type_non_partitioned.c_bigint + spark_catalog.qa_db_warehouse.area(10, 20) AS c_bigint,
    all_type_non_partitioned.c_smallint AS c_smallint,
    all_type_non_partitioned.c_tinyint AS c_tinyint,
    all_type_non_partitioned.c_float AS c_float,
    all_type_non_partitioned.c_boolean AS c_boolean,
    all_type_non_partitioned.c_array AS c_array,
    all_type_non_partitioned.c_double AS c_double,
    all_type_non_partitioned.c_struct AS c_struct
  
  FROM all_type_non_partitioned
  INNER JOIN all_type_partitioned
     ON all_type_non_partitioned.c_tinyint = all_type_partitioned.c_tinyint and all_type_non_partitioned.c_smallint = all_type_partitioned.c_smallint

),

Reformat_3 AS (

  SELECT * 
  
  FROM Join_1 AS in0

),

Reformat_4 AS (

  SELECT * 
  
  FROM Reformat_3 AS in0

),

Reformat_2 AS (

  SELECT * 
  
  FROM Reformat_4 AS in0

)

SELECT *

FROM Reformat_4
