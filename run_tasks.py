"""Run tasks with prefect, using DaskTaskRunner."""
from prefect import flow, task, get_run_logger
from prefect_shell import shell_run_command
from prefect_dask import DaskTaskRunner
import pathlib
import logging


@flow(
    name="main_flow",
    version="run0",
    # task_runner=DaskTaskRunner()
    # task_runner=DaskTaskRunner(
    #     cluster_kwargs={
    #         "n_workers": 4,
    #         "threads_per_worker": 1,
    #     }
    # ),
)
def shell_flow(messages):
    logger = get_run_logger()
    for message in messages:
        command = f"python script.py {10} {message} 2>&1 | tee {message}.txt"
        logger.info(f"Running command: {command}")
        shell_run_command.submit(command=command, return_all=True)


# call the flow!
if __name__ == "__main__":
    messages = ["moo", "woof", "quack", "meow"]
    shell_flow(messages)

