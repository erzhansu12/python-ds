# 🚢 Titanic — Survival Prediction (Classic ML)

My first classic machine-learning project, built on the
[Kaggle Titanic dataset](https://www.kaggle.com/c/titanic): predict whether a passenger survived.

📓 Notebook: [`titanic_classic_ml.ipynb`](titanic_classic_ml.ipynb)

## What's inside

**1. Data loading** — `train.csv` / `test.csv` from Kaggle.

**2. Feature engineering**
| New feature | How it's built |
|---|---|
| `Name_length` | length of the passenger's name |
| `Has_Cabin` | 1 if a cabin number is known |
| `FamilySize` | `SibSp + Parch + 1` |
| `IsAlone` | 1 if `FamilySize == 1` |
| `Title` | Mr / Miss / Mrs / Master / Rare, extracted from the name with a regex |

Missing values are filled (`Embarked` → `S`, `Fare` → median, `Age` → random values within mean ± std),
then `Sex`, `Embarked`, `Title` are encoded as numbers and `Age` / `Fare` are binned into groups.

**3. Exploratory analysis**
- Pearson correlation heatmap of all features
- Seaborn pairplot coloured by `Survived`

**4. Modelling setup**
- A custom **stacking** function (base models → meta-model), with either cross-validated
  out-of-fold predictions or a hold-out validation split
- Hyper-parameter grids for `GradientBoostingClassifier`, `RandomForestClassifier`, `SVC`,
  `LogisticRegression` (+ `XGBClassifier` imported), with `StratifiedKFold(5)` for `GridSearchCV`

## Tech stack
`pandas` · `numpy` · `matplotlib` · `seaborn` · `scikit-learn` · `xgboost`

## How to run
The notebook was written on Kaggle and reads data from `../input/titanic/`.
Easiest way: open it in a Kaggle notebook with the *Titanic* competition data attached.
To run locally, download the data and change the paths in the second cell.
