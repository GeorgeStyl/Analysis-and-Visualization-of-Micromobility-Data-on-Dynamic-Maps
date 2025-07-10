
# Micromovement Data Visualization on Dynamic Maps

This project provides tools and helper scripts for the analysis and visualization of micromovement data, leveraging PowerFleet APIs, geospatial data, and artificial intelligence techniques.

---

## Features

- Integration of APIs via the custom module `Powerfleet_APIs_Management`
- Geospatial computations using `geopandas`, `shapely`, `geopy`, and `geojson`
- Clustering and machine learning using `scikit-learn`
- Data analysis and processing with `pandas`, `numpy`, `scipy`, `statsmodels`
- Visualization using `matplotlib`, `seaborn`, and `plotly`
- Enhanced console output using `colorama`

---

## Requirements

Python version 3.8 or newer is required.

---

## Installation

### Installation with Anaconda

You can install all required packages using the command:

```bash
conda env create -f environment.yml --name <env_name>
```

Then activate the environment with:

```bash
conda activate <env_name>
```

### Installation with pip

Alternatively, you can use `pip` to install the required packages. First, create a virtual environment:
python -m venv <env_name>
source <env_name>/bin/activate  # or .\<env_name>\Scripts\activate on Windows

Then, install the packages from the `requirements.txt` file:
pip install -r requirements.txt


### Manual Installation (Without Conda or pip files)

You can also manually install the required packages without using `environment.yml or requirements.txt`:
pip install package1 package2 package3 ...

Make sure to install the correct versions of each package as specified by the project.

---

## Execution Settings

In the second cell of `all_data_analysis.ipynb`, there are two variables controlling the use of the database connection:

```python
FETCH_FROM_DB = False
UPDATE_DB     = False
```

This means the code **will run without** a database connection.

To enable database usage, change both values to `True` and fill in the connection details that follow in the same cell.

---

## Execution Order of Algorithms

To ensure smooth execution of the notebooks, follow this order:

1. Run `all_data_analysis.ipynb` first. It updates the CSV files needed in the next steps.
2. Then run `visualize_danger_areas_v1.ipynb` and `projection_to_streetsv2.ipynb`, since both depend on the output data from the previous step.
