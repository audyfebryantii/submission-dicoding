# Dicoding Data Analyst Submission

## Dataset
[Bike Sharing Dataset](https://drive.google.com/file/d/1RaBmV6Q6FYWU4HWZs80Suqd7KQC34diQ/view?usp=sharing) [(Sumber)](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset)

## Folder Structure
```bash
├── dashboard
│   ├── 8960285.jpg
│   └── dashboard.py
│   └── main_data.csv
├── data
│   ├── day.csv
│   └── hour.csv
│   └── Readme.txt
├── README.md
├── notebook.ipynb
└── requirements.txt
```

## Setup environment
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit babel
```

## Run streamlit app (local)
1. Clone this repository
   ```
   https://github.com/audyfebryantii/submission-dicoding.git
   ```
2. Direct the path to the dashboard directory
   ```
   cd submission-dicoding/dashboard
   ```
3. Run streamlit app
   ```
   streamlit run dashboard.py
   ```

## Run streamlit app (cloud)
```
https://bike-rental-dash.streamlit.app/
```
