"""Run tasks with prefect, using DaskTaskRunner."""
from prefect import flow, task, get_run_logger
from prefect_shell import shell_run_command
from prefect_dask import DaskTaskRunner
import pathlib
import logging

@task
def say_hello(name):
    print(f"hello {name}")

@task
def say_goodbye(name):
    print(f"goodbye {name}")

@flow(task_runner=DaskTaskRunner())
def greetings(names):
    for name in names:
        say_hello.submit(name)
        say_goodbye.submit(name)


@flow(
    name="main_flow",
    version="run0",
    task_runner=DaskTaskRunner(
        cluster_kwargs={
            "n_workers": 1,
            "threads_per_worker": 1,
        }
    ),
    # task_runner=DaskTaskRunner()
)
def shell_flow(messages):
    logger = get_run_logger()
    futures = []
    for message in messages:
        command = f"python script.py {1000} {message}"
        shell_run_command.submit(command=command, return_all=True)
    # Wait for results
    for future in futures:
        logger.info(future.result())
        


# call the flow!
if __name__ == "__main__":
    messages = ["moo", "woof", "quack", "meow"]
    shell_flow(messages)
    # print(result)

