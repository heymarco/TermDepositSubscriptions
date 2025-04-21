# Readme

---

The goal is to predict whether a client will subscribe to a fixed-term deposit (`y`) based on the Bank Marketing dataset on UCI.

### Notebook
The main notebook for data preprocessing and model training can be found under [main.ipynb](notebooks/main.ipynb).

### Project structure
- `config` contains the path configurations for the loaded data and final models
- `notebook` contains the [main notebook](notebooks/main.ipynb)
- `utils` contains the definitions and groupings of the [column names](utils/column_names.py)

### Setup & Dependencies
- Dependencies are managed via [pipenv](https://pipenv.pypa.io/en/latest/). Before setting up the virtual environment, [install pipenv](https://pipenv.pypa.io/en/latest/installation.html).
- To set up the virtual environment, run `pipenv install -e .`
  - if you encounter problems, try deleting the `Pipfile.lock` file
- To enter the virtual environment, run `pipenv shell` 
- run `jupyter notebook` and follow the link displayed in your terminal
