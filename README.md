# Demo - Running shell scripts in parallel with Prefect

Running multiple shell scripts in parallel, using Prefect 2.0.

- `script.py`: A placeholder CLI script (maybe something that cannot be easily re-written in python).
- `run_tasks.py`: Creates a Prefect flow which contains many tasks, each of which runs a different shell command.

## Instructions

Install requirements (**STRONGLY RECOMMENDED**: Create a virtualenv or conda environment first):

```bash
pip install -r requirements.txt
```

Run shell scripts using Prefect:

```bash
python run_tasks.py
```

Monitor task status using Orion UI:
```bash
prefect orion start
```