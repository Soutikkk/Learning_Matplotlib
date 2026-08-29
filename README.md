# 📊 Learning Matplotlib in Python

A beginner-friendly repository documenting my journey of learning **Matplotlib in Python** through hands-on programs, visualizations, and real-world datasets.

This project covers the fundamentals of Matplotlib and gradually moves toward creating different types of charts, customizing visualizations, using subplots, and combining **Pandas + Matplotlib** for data visualization.

---

## 🐍 About

**Matplotlib** is one of the most widely used Python libraries for creating data visualizations.

This repository contains a collection of small, focused programs that demonstrate different Matplotlib concepts step by step.

The examples start with simple line plots and gradually introduce:

* Plot customization
* Markers and line styles
* Titles and axis labels
* Tick customization
* Grid lines
* Bar charts
* Pie charts
* Scatter plots
* Histograms
* Subplots
* Pandas integration
* Visualization using CSV data

The goal of this project is to build a strong foundation in **Python data visualization** before moving on to more advanced Data Science and Machine Learning projects.

---

## 📂 Project Structure

```text
Learning_Matplotlib/
│
├── 📁 Programs/
│   ├── 01_hello_world.py
│   ├── 02_import_matplotlib.py
│   ├── 03_check_matplotlib_version.py
│   ├── 04_plot_basic_list_data.py
│   ├── ...
│   ├── 54_subplots_mixed_chart_types.py
│   ├── ...
│   ├── 55_read_csv_preview.py
│   ├── ...
│   └── 62_pokemon_type_barh_with_axis_labels.py
│
├── 📓 Learning_Matplotlib.ipynb
├── 📊 Pokemon.csv
├── 📄 Pokemon2.json
└── 📖 README.md
```

---

# 📚 Topics Covered

## 1. Getting Started with Matplotlib

Learned the basics of importing Matplotlib and checking its version.

```python
import matplotlib
print(matplotlib.__version__)
```

Also introduced:

```python
import matplotlib.pyplot as plt
```

---

## 2. Basic Line Plots 📈

Learned how to create basic line graphs using Python lists and NumPy arrays.

Topics include:

* Plotting `x` and `y` values
* Plotting only `y` values
* Using NumPy arrays with Matplotlib
* Displaying plots with `plt.show()`

Example:

```python
plt.plot(x, y)
plt.show()
```

---

## 3. Plot Customization 🎨

Learned how to customize the appearance of line plots using:

* Markers
* Marker size
* Marker face color
* Marker edge color
* Custom HEX colors
* Line styles
* Line width
* Multiple lines

Examples of line styles:

```python
linestyle="solid"
linestyle="dashed"
linestyle="dotted"
```

---

## 4. Multiple Lines

Learned how to display multiple datasets on the same graph.

This is useful when comparing different groups or trends.

The project also demonstrates using a dictionary to reuse common line styling:

```python
line_style = dict(
    marker="o",
    markersize=8,
    linestyle="solid",
    linewidth=3
)
```

---

## 5. Titles & Labels 🏷️

Learned how to make graphs easier to understand by adding:

* Titles
* X-axis labels
* Y-axis labels
* Font sizes
* Font weights
* Colors

Example:

```python
plt.title("Class Size of Students in Different Years")
plt.xlabel("Years")
plt.ylabel("Number of Students")
```

---

## 6. Tick Customization

Learned how to customize axis ticks using:

```python
plt.xticks()
plt.tick_params()
```

Topics include:

* Custom tick labels
* Rotating tick labels
* Font customization
* Tick direction
* Tick length
* Tick width

---

## 7. Grid Lines

Learned how grid lines can make graphs easier to read.

Examples include:

```python
plt.grid()
```

Grid customization was also explored for:

* X-axis only
* Y-axis only
* Both axes
* Dashed grid lines
* Grid transparency
* Grid line width

---

# 📊 Different Types of Charts

## 8. Bar Charts

Bar charts are useful for comparing different categories.

The project covers:

* Basic bar charts
* Multiple colors
* Horizontal bar charts

Examples:

```python
plt.bar(categories, values)
```

and:

```python
plt.barh(categories, values)
```

---

## 9. Pie Charts 🥧

Learned how to visualize the distribution of categories using pie charts.

Topics include:

* Basic pie charts
* Labels
* Percentages
* Start angles
* Shadows
* Custom colors
* Titles
* Exploding slices

Example:

```python
plt.pie(
    values,
    labels=categories,
    autopct="%1.1f%%",
    startangle=90
)
```

---

## 10. Scatter Plots 🔵

Scatter plots are useful for studying relationships between two variables.

The project demonstrates:

* Basic scatter plots
* Axis labels
* Titles
* Transparency
* Marker size
* Multiple groups
* Legends

Example:

```python
plt.scatter(x, y)
```

A practical example used in the project is the relationship between:

> **Hours Studied vs. Scores Obtained**

This introduces the idea of identifying possible correlations between variables.

---

## 11. Histograms 📉

Histograms are used to visualize the distribution of quantitative data.

The project explores:

* Normally distributed data
* Different levels of variance
* Clipping values
* Different numbers of bins
* Histogram edge colors

Example:

```python
plt.hist(scores, bins=30)
```

Different bin sizes such as:

```text
10 bins
20 bins
30 bins
50 bins
```

are explored to understand how bin size affects visualization.

---

# 🧩 Subplots

## 12. Creating Multiple Plots

Learned how to create multiple plots inside a single figure using:

```python
plt.subplots()
```

The project covers:

* Creating subplot grids
* 2 × 2 subplot layouts
* Multiple line plots
* Four different plots
* `tight_layout()`
* Mixing different chart types

For example, a single figure can contain:

```text
┌─────────────┬─────────────┐
│ Line Plot   │ Bar Chart   │
├─────────────┼─────────────┤
│ Scatter     │ Pie Chart   │
└─────────────┴─────────────┘
```

This is an important concept for creating dashboards and multi-view visualizations.

---

# 🐼 Pandas + Matplotlib

## 13. Working with Real Data

The final section combines **Pandas and Matplotlib**.

The project loads the Pokémon dataset using:

```python
import pandas as pd

df = pd.read_csv("Pokemon.csv")
```

The dataset is then explored using:

```python
df.head()
```

and:

```python
df["Type1"].value_counts()
```

---

## 14. Pokémon Data Visualization ⚡

The Pokémon dataset is used to create visualizations showing the number of Pokémon belonging to each primary type.

Examples include:

* Pokémon type counts
* Vertical bar charts
* Horizontal bar charts
* Chart titles
* X-axis labels
* Y-axis labels
* Edge colors

Example:

```python
type_count = df["Type1"].value_counts()

plt.barh(
    type_count.index,
    type_count.values
)

plt.title("Count of Pokemon by Type")
plt.xlabel("Count")
plt.ylabel("Type")

plt.show()
```

This provides a practical example of how **Pandas can prepare data and Matplotlib can visualize it**.

---

# 🛠️ Technologies Used

| Technology          | Purpose                   |
| ------------------- | ------------------------- |
| 🐍 Python           | Programming language      |
| 📊 Matplotlib       | Data visualization        |
| 🔢 NumPy            | Numerical data and arrays |
| 🐼 Pandas           | Data manipulation         |
| 📓 Jupyter Notebook | Interactive learning      |
| 📄 CSV              | Dataset                   |
| 📋 JSON             | Structured data           |
| 🔧 Git & GitHub     | Version control           |

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/Soutikkk/Learning_Matplotlib.git
```

## 2. Navigate to the Project

```bash
cd Learning_Matplotlib
```

## 3. Install the Required Libraries

```bash
pip install matplotlib numpy pandas jupyter
```

## 4. Run the Programs

Navigate to the `Programs` directory and run any Python file:

```bash
python Programs/04_plot_basic_list_data.py
```

You can also open the Jupyter Notebook:

```text
Learning_Matplotlib.ipynb
```

using Jupyter Notebook or JupyterLab.


---

# 📈 Learning Progress

* [x] Import Matplotlib
* [x] Check Matplotlib version
* [x] Basic line plots
* [x] NumPy with Matplotlib
* [x] Markers
* [x] Marker customization
* [x] Line styles
* [x] Multiple lines
* [x] Titles
* [x] Axis labels
* [x] Tick customization
* [x] Grid lines
* [x] Bar charts
* [x] Horizontal bar charts
* [x] Pie charts
* [x] Scatter plots
* [x] Histograms
* [x] Subplots
* [x] Multiple chart types in subplots
* [x] Pandas + Matplotlib
* [x] Pokémon dataset visualization

---

# 🎓 Learning Resource

A major learning reference for this project was the **Bro Code** tutorial on Matplotlib.

### 👨‍🏫 Credit

**Bro Code — YouTube**

🔗 **[Matplotlib Tutorial](https://youtu.be/c9vhHUGdav0)**

Thank you to **Bro Code** for creating the tutorial and providing a clear, practical introduction to Matplotlib.

> This repository is my personal learning/practice project. The programs were written while following along with the concepts taught in the tutorial and experimenting with them independently.

---

# 📌 Future Learning

This project provides the foundation for moving toward more advanced visualization and data-analysis topics, including:

* Advanced Matplotlib customization
* Seaborn
* Exploratory Data Analysis (EDA)
* Statistical visualization
* Data storytelling
* Interactive visualizations
* Machine Learning data visualization

---

# 👨‍💻 Author

**Soutikkk**

Learning → Practicing → Building 🚀

Python 🐍 → Pandas 🐼 → Matplotlib 📊 → Data Science 🤖

---

## ⭐ Support

If this repository helps you learn Matplotlib, consider giving it a ⭐ on GitHub!

**Happy Learning! 🚀📊🐍**
