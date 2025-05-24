# U.S. Medical Insurance Cost Analysis

This project analyzes medical insurance data from patients in the U.S. to uncover trends and patterns in insurance charges based on factors like smoking status, BMI, and region.

## 📁 Dataset
The dataset used is provided by Codecademy and contains the following columns:
- `age`: Age of primary beneficiary
- `sex`: Insurance contractor gender
- `bmi`: Body mass index
- `children`: Number of children covered by health insurance
- `smoker`: Whether the person smokes
- `region`: U.S. region
- `charges`: Individual medical costs billed by health insurance

## 📊 Analysis Performed

The analysis was done using pure Python (no pandas), and includes:

- ✅ Average insurance cost for **smokers** vs **non-smokers**
- ✅ Average insurance cost for people with **BMI > 30** (obese) vs BMI ≤ 30
- ✅ Average insurance cost per **U.S. region**
- ✅ 📈 Bar chart visualizing average cost per region using `matplotlib`

## 🔧 Tools Used
- Python (built-in `csv` module)
- `matplotlib` for data visualization

## 🧠 Key Insights
- Smokers are charged significantly higher on average.
- People with a BMI above 30 tend to pay more.
- The Southeast region has the highest average insurance charges.


## ✅ How to Run
1. Make sure `insurance.csv` is in the same directory.
2. Run the script:
```bash
python insurance_analysis.py


