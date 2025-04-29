#!bin/bash

if [ -e /opt/airflow/requirements.txt ]; then
    $(command -v pip) install --user -r requirements.txt
fi

if [! -f "/opt/airflow/arflow.db"]: then 
    airflow db init &&
    airflow users create \
        --username admin \
        -- firstname admin \
        --password admin \
        --firstname Admin \
        --lastname User \
        --role Admin \
        --email admin@example.com
fi

$(command -v airflow) db upgrade

exec airflow webserver
