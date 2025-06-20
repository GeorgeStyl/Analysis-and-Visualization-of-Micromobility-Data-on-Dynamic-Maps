
# Micromovement Data Visualization on Dynamic Maps  
# Αποτύπωση Δεδομένων Μικρο-Μετακινήσεων σε Δυναμικούς Χάρτες

This project provides tools and helper scripts for the analysis and visualization of micromovement data, leveraging PowerFleet APIs, geospatial data, and artificial intelligence techniques.  
Το έργο αυτό προσφέρει εργαλεία και βοηθητικά scripts για την ανάλυση και οπτικοποίηση δεδομένων μικρο-μετακινήσεων, αξιοποιώντας APIs της PowerFleet, γεωχωρικά δεδομένα και τεχνικές τεχνητής νοημοσύνης.

---

## Features  
## Δυνατότητες

- Integration of APIs via the custom module `Powerfleet_APIs_Management`  
  Ενσωμάτωση APIs μέσω του προσαρμοσμένου module `Powerfleet_APIs_Management`

- Geospatial computations using `geopandas`, `shapely`, `geopy`, and `geojson`  
  Γεωχωρικοί υπολογισμοί με χρήση `geopandas`, `shapely`, `geopy` και `geojson`

- Clustering and machine learning using `scikit-learn`  
  Ομαδοποίηση και μηχανική μάθηση με `scikit-learn`

- Data analysis and processing with `pandas`, `numpy`, `scipy`, `statsmodels`  
  Ανάλυση και επεξεργασία δεδομένων με `pandas`, `numpy`, `scipy`, `statsmodels`

- Visualization using `matplotlib`, `seaborn`, and `plotly`  
  Οπτικοποίηση με `matplotlib`, `seaborn` και `plotly`

- Enhanced console output using `colorama`  
  Εμπλουτισμένη έξοδος στην κονσόλα με `colorama`

---

## Requirements  
## Προαπαιτούμενα

Python version 3.8 or newer is required.  
Απαιτείται Python έκδοση 3.8 ή νεότερη.

---

## Installation  
## Εγκατάσταση

### Installation with Anaconda  
### Εγκατάσταση με Anaconda

You can install all required packages using the command:  
Μπορείτε να εγκαταστήσετε όλα τα απαραίτητα πακέτα με την εντολή:

```bash
conda env create -f environment.yml --name <env_name>
```

Then activate the environment with:  
Στη συνέχεια, ενεργοποιήστε το περιβάλλον με:

```bash
conda activate <env_name>
```

---

## Execution Settings  
## Ρυθμίσεις Εκτέλεσης

In the second cell of `all_data_analysis.ipynb`, there are two variables controlling the use of the database connection:  
Στο δεύτερο κελί του αρχείου `all_data_analysis.ipynb`, υπάρχουν δύο μεταβλητές που ελέγχουν αν θα χρησιμοποιηθεί σύνδεση με βάση δεδομένων:

```python
FETCH_FROM_DB = False
UPDATE_DB     = False
```

This means the code **will run without** a database connection.  
Αυτό σημαίνει ότι ο κώδικας **θα εκτελεστεί χωρίς** σύνδεση με βάση δεδομένων.

To enable database usage, change both values to `True` and fill in the connection details that follow in the same cell.  
Εάν θέλετε να ενεργοποιήσετε τη χρήση βάσης δεδομένων, αλλάξτε τις τιμές σε `True` και συμπληρώστε τα αντίστοιχα πεδία σύνδεσης που ακολουθούν στο ίδιο κελί.

---

## Execution Order of Algorithms  
## Σειρά Εκτέλεσης των Αλγορίθμων

To ensure smooth execution of the notebooks, follow this order:  
Για την ομαλή εκτέλεση των notebooks, η σωστή σειρά είναι η εξής:

1. Run `all_data_analysis.ipynb` first. It updates the CSV files needed in the next steps.  
   Εκτελέστε πρώτα το `all_data_analysis.ipynb`. Αυτό το notebook ενημερώνει τα σχετικά CSV αρχεία που απαιτούνται για τα επόμενα βήματα.

2. Then run `visualize_danger_areas_v1.ipynb` and `projection_to_streetsv2.ipynb`, since both depend on the output data from the previous step.  
   Στη συνέχεια, εκτελέστε τα `visualize_danger_areas_v1.ipynb` και `projection_to_streetsv2.ipynb`, αφού το πρώτο έχει ολοκληρωθεί, καθώς αυτά τα δύο notebooks εξαρτώνται από τα δεδομένα που θα παραχθούν από το `all_data_analysis.ipynb`.

---
