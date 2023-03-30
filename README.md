# Data analysis project - Netherlands Office Taipei

This project was part of my internship at the Netherlands Office Taipei. Research focused on (economic/innovative) strengths and weaknesses of Netherlands & Taiwan, and their trade relations. Insights were visualised using Tableau.

## Data
All data is open source.
- **CBS data** (import, dependencies)
- **Taiwan Trade Office data** (export) 
- **Patents from Lens.org** (counted by simple families)


## Code
Each Python file is added into the relevant directory/folder. 
- **Trade/Export/TW_data-preprocessing.py:** Preprocesses data from TW trade office (Unpack **TW_export_data-2018-2022.zip**), concatenates the files together to **Export-all-updated.xlsx**. Columns with exchange rate are added manually. 
- **Patents/patents_to_family.py**: Create patent families and exports to Excel files and manually added to 'Patent families' folder. Uncomment the code if applicant_types are wanted (NOTE: runtime is long).\
- **Patents/patent_families_overlap.py** Find overlapping patents between digital technologies cluster and nanotechnology cluster.

