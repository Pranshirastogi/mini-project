
# 🎓 Data Analysis Mini Project

This project is an interactive **data analysis dashboard** built using **Streamlit** and **Plotly**. It explores a dataset containing **university rankings** along with relevant features such as **country, subject, teaching score, research score, citations, and gender distribution**.

---

## 🔍 Project Overview

This dashboard allows users to:

- View the dataset of universities and their rankings.
- Analyze ranking distributions by country and subject.
- Visualize statistical plots such as pie charts, box plots, scatter plots, and violin plots.
- Explore gender-based statistics (female and male percentages).
- Compare teaching and research metrics against world rankings.

---

## 📚 Features

- **Sidebar controls** to toggle visualizations.
- **Interactive charts** powered by Plotly.
- **Responsive layout** using Streamlit.
- **Geographical plots** (via Folium - optional for future expansion).
- Modular and readable code.

---

## 🧰 Libraries Used

- `pandas` – for data manipulation
- `numpy` – for numerical operations
- `streamlit` – for web interface
- `plotly.express` – for interactive plotting
- `matplotlib.pyplot` – imported but not used (optional)
- `plotly.graph_objects` – additional plot customization
- `folium` – for interactive maps (future extension)
- `MarkerCluster` from `folium.plugins` – (not used currently but useful for map clustering)

---

## 📁 File Structure

```
project_folder/
├── dataset.csv              # Input data file with university data
├── app.py                   # Main Streamlit application script
└── README.md                # This file
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/data-analysis-streamlit.git
cd data-analysis-streamlit
```

### 2. Install Requirements

Ensure you have Python 3.7+ and install the dependencies:

```bash
pip install pandas numpy streamlit plotly folium matplotlib
```

### 3. Run the App

```bash
streamlit run app.py
```

Then open your browser at: `http://localhost:8501`

---

## 📊 Visualizations Included

- ✅ Pie Chart: Country-wise university count
- ✅ Pie Chart: Subject-wise university distribution
- ✅ Box Plot: Subjects overview
- ✅ Violin Plot: Citations distribution
- ✅ Scatter Plot: World Rank vs Teaching
- ✅ Scatter Plot: World Rank vs Research
- ✅ Scatter Plot: Female % by Subject
- ✅ Scatter Plot: Male % by Subject

---

## 📝 Notes

- Ensure the file `dataset.csv` is present in the project root.
- You can expand the project to include maps using `folium` and location data.
- If required, remove unused libraries (`matplotlib`, `folium`) to clean up the code.

---

## 👨‍💻 Author

Developed as a **mini project for data analysis** using open-source Python tools.


