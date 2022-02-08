# airflow-api-webinar

This repo contains example DAGs used in Astronomer's Airflow API webinar on 2/8/22. A link to the webinar recap will be posted here soon. 

## DAGs

DAGs included in this repo are for the purpose of highlighting the Airflow API:

- `api-dag`: Uses the `SimpleHttpOperator` to trigger a DAG in a separate Airflow environment using the Airflow API dagRuns endpoint. Requires a connection ID called `airflow-api` with API authentication for the remote Airflow environment.
- `dependent-dag`: Example DAG that is triggered by the API. The task waits for 30 seconds to facilitate showing the DAG running after triggering it remotely using the API.
- `random-failure-dag`: Example DAG that randomly fails when run, for showing using the API to get DAG runs (find successes and failures) and clear failed task runs to rerun the DAG.

## API Calls

The following API calls were used in the webinar with these DAGs:

- **Get Providers:** GET request to http://localhost:8080/api/v1/providers
- **Get Import Errors:** GET request to http://localhost:8080/api/v1/importErrors
- **Trigger a DAG Run:** POST request to http://localhost:8080/api/v1/dags/random_failures/dagRuns
  - Body: {"execution_date": "2022-02-03T14:15:22Z"}
- **GET DAG Runs:** GET request to http://localhost:8080/api/v1/dags/random_failures/dagRuns
- **Rerun Tasks:** POST request to http://localhost:8080/api/v1/dags/random_failures/clearTaskInstances
  - Body: {"dry_run": false, "task_ids": ["random-task], "start_date": "2022-02-03T17:29:00.056990+00:00", "end_date": "2022-02-03T17:52:59.147853+00:00", "only_failed": true, "only_running": false, "include_subdags": false, "include_parentdag": false, "reset_dag_runs": true}

Note: when running locally with the Astronomer CLI, all these requests can use Basic Auth with admin:admin credentials 

## Getting Started

The easiest way to run these example DAGs and try the Airflow API is to use the Astronomer CLI to get an Airflow instance up and running locally:

 1. [Install the Astronomer CLI](https://www.astronomer.io/docs/cloud/stable/develop/cli-quickstart)
 2. Clone this repo somewhere locally and navigate to it in your terminal
 3. Initialize an Astronomer project by running `astro dev init`
 4. Start Airflow locally by running `astro dev start`
 5. Navigate to localhost:8080 in your browser and you should see the tutorial DAGs there
