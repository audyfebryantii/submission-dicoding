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

## Run steamlit app
```
streamlit run dashboard.py
```
