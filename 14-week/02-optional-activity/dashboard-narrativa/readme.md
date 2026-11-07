# Interactive Sales Dashboard – 2025

## 1. Project Overview

This project presents an interactive sales dashboard developed in Microsoft Power BI. The dashboard analyzes the sales performance of a fictional retail business during 2025. Its purpose is to identify sales trends, evaluate product performance, and compare the different sales channels.

## 2. Dataset Description

The dataset contains 500 simulated sales transactions from January to December 2025. It includes the transaction ID, date, product, category, sales channel, quantity, unit price, and total sale amount. The data was generated using Python and stored in a CSV file called `ventas.csv`.

## 3. Dashboard & insight

The dashboard presents total sales, number of transactions, and units sold through interactive KPI cards and charts. It includes sales comparisons by product and sales channel, as well as a monthly sales trend for 2025. Users can explore the information using date and sales channel slicers, and the date hierarchy allows drill-down analysis. The business recorded total sales of **COP 46,840,000** from 500 transactions and sold 1,558 units. **Anillos** was the best-performing product, generating COP 8,985,000 in sales. **WhatsApp** was the leading sales channel, with COP 12,160,000 in revenue. Based on these results, the business should strengthen its WhatsApp sales strategy and maintain the promotion of high-performing products while developing campaigns to improve the sales of lower-performing products.

## 4. Visualizations and Interactivity

The report includes:
- KPI cards for total sales, number of sales, and units sold.
- A column chart showing sales by product.
- A bar chart comparing sales by channel.
- A line chart showing sales evolution during 2025.
- A date slicer to filter the reporting period.
- A sales channel slicer to compare channel performance.
- A date hierarchy with year and month levels for drill-down analysis.
- Cross-filtering between report visualizations.

## 5. Tools Used

- Microsoft Power BI Desktop.
- Python.
- CSV dataset.
- DAX measures.

## 6. Files

- `generar_datos.py`: Python script used to generate the sales dataset.
- `ventas.csv`: Simulated sales data used in Power BI.
- `dashboard-ventas-2025.pbix`: Interactive Power BI report.
- `README.md`: Project documentation.