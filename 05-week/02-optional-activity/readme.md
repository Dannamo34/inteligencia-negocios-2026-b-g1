# Corte 1 - Business Intelligence

## Objectives

- Self-assess the concepts learned during Corte 1.
- Solve a practical case involving star schema modeling.
- Identify the topics I understand well and those that I need to review before the midterm exam.

---

# 1. Summary of Corte 1 Concepts

## Data Chain

The data chain represents the process through which data is transformed into useful information for decision-making. This process begins with **data collection**, continues with its **storage, transformation, and analysis**, and ultimately allows organizations to generate information and knowledge to support decision-making.

In general, the data chain can be represented as follows:

**Data → Information → Knowledge → Decisions**

For example, a pharmacy records every sale made. This data can be transformed into information about which products are sold the most. This information can then generate knowledge about customer and sales behavior and finally support decisions such as increasing the inventory of certain products.

---

## KPI

A **KPI (Key Performance Indicator)** is a key performance indicator used to measure the achievement of a specific organizational objective.

KPIs should be related to specific objectives and should allow the performance of a process or activity to be evaluated.

Some examples of KPIs are:

- Total sales per month.
- Number of products sold.
- Average transaction value.
- Sales growth percentage.
- Number of sales per branch.

For example, if a pharmacy has the objective of increasing its monthly sales, an appropriate KPI could be the **percentage growth in sales compared to the previous month**.

---

## OLTP vs OLAP

### OLTP

**OLTP (Online Transaction Processing)** is used to manage the daily operations of an organization.

Its main objective is to record and process transactions quickly, consistently, and securely.

Examples include:

- Recording a sale.
- Recording a payment.
- Updating inventory.
- Creating an invoice.
- Registering a customer.

OLTP databases are normally designed to perform frequent insert, update, and query operations.

### OLAP

**OLAP (Online Analytical Processing)** is focused on analyzing large amounts of information.

It allows historical data to be queried and analyzed from different perspectives to support decision-making.

Examples include:

- Analyzing sales by month.
- Comparing sales between branches.
- Identifying the best-selling products.
- Analyzing sales behavior over several years.

### Main Difference

| OLTP | OLAP |
|---|---|
| Transaction-oriented | Analysis-oriented |
| Manages day-to-day operations | Analyzes historical information |
| Handles many small transactions | Handles complex analytical queries |
| Frequently inserts and updates data | Mainly queries data |
| Example: sales transaction system | Example: Data Warehouse |

---

## Data Warehouse

A **Data Warehouse** is a centralized repository of data designed primarily for analysis and decision-making.

It integrates information from different sources and preserves historical data that can be analyzed using Business Intelligence tools.

Some of its main characteristics are:

- Integrates information from different sources.
- Preserves historical information.
- Is analysis-oriented.
- Facilitates report generation.
- Allows organizations to calculate indicators and analyze trends.

For example, a pharmacy chain can use a Data Warehouse to store historical information about sales, products, and branches and then analyze how sales have evolved over several months or years.

---

## Star Schema

A **star schema** is a modeling technique mainly used in Data Warehouses.

It consists of a **fact table** located at the center and several **dimension tables** connected to it.

The fact table contains the business events that need to be analyzed and the numerical measures associated with those events.

The dimension tables contain descriptive information that allows the facts to be analyzed from different perspectives.

The structure is called a star schema because the fact table is located at the center, while the dimensions are arranged around it.

### General Example

```text
                    DIM_PRODUCT
                         |
                         |
DIM_BRANCH ------ FACT_TABLE ------ DIM_TIME
                         |
                         |
                    DIM_CUSTOMER
```

2. Practical Case: Pharmacy Chain
Problem Statement

A pharmacy chain wants to analyze its sales by:

Product.
Branch.
Month.

To address this need, a star schema is proposed. The central fact table represents the sales transactions, while the dimensions allow the information to be analyzed from different perspectives.

Proposed Star Schema
                         DIM_PRODUCT
                              |
                              |
                              |
DIM_BRANCH ------------ FACT_SALES ------------ DIM_TIME
                              |
                              |
                              |
                         DIM_CUSTOMER

For the minimum requirements of the case, the Product, Branch, and Time dimensions are used.

The Customer dimension can be added if the organization needs to analyze sales by customer.

3. Fact Table: FACT_SALES

The FACT_SALES fact table represents each sales event carried out at a branch.

This table stores the measures that will later be used for analysis.

Measures

The main proposed measures are:

Measure	Description
quantity_sold	Number of units sold
unit_price	Selling price of each unit
discount	Discount amount applied to the sale
total_sale	Total value of the sale
Keys

The main foreign keys in the fact table are:

product_id
branch_id
time_id

These keys allow each sale to be related to its corresponding dimensions.

Example of FACT_SALES
product_id	branch_id	time_id	quantity_sold	unit_price	discount	total_sale
101	1	20260801	3	15000	0	45000
205	2	20260801	2	25000	5000	45000
101	1	20260901	5	15000	2000	73000
4. Dimension: DIM_PRODUCT

The DIM_PRODUCT dimension provides information about the products being sold.

It allows sales to be analyzed according to categories, brands, presentations, laboratories, and other product characteristics.

Attributes
product_id
product_name
category
brand
presentation
laboratory
product_type
Example of DIM_PRODUCT
product_id	product_name	category	brand	presentation	laboratory
101	Acetaminophen	Analgesic	Generic	Tablets	Laboratory A
205	Vitamin C	Vitamins	Brand X	Tablets	Laboratory B

This dimension allows the organization to answer questions such as:

Which product sells the most?
Which category generates the highest sales?
Which brand has the best results?
5. Dimension: DIM_BRANCH

The DIM_BRANCH dimension allows sales to be analyzed according to the branch where the transaction took place.

Attributes
branch_id
branch_name
city
address
zone
branch_type
Example of DIM_BRANCH
branch_id	branch_name	city	zone
1	Central Branch	Neiva	Central
2	North Branch	Neiva	North
3	South Branch	Neiva	South

This dimension allows the organization to answer questions such as:

Which branch sells the most?
Which city generates the highest revenue?
Which zone has the highest sales volume?
6. Dimension: DIM_TIME

The DIM_TIME dimension allows sales to be analyzed over time.

It facilitates historical analysis and allows information to be grouped by day, month, quarter, or year.

Attributes
time_id
date
day
month
month_name
quarter
year
Example of DIM_TIME
time_id	date	month	month_name	quarter	year
20260801	2026-08-01	8	August	3	2026
20260802	2026-08-02	8	August	3	2026
20260901	2026-09-01	9	September	3	2026
7. Relationship Between Facts and Dimensions

The final structure of the star schema is:

                         DIM_PRODUCT
                         ------------
                         product_id
                         product_name
                         category
                         brand
                         presentation
                         laboratory
                         product_type
                              |
                              |
                              |
DIM_BRANCH ------------- FACT_SALES ------------- DIM_TIME
-----------               ----------               ---------
branch_id                 product_id               time_id
branch_name               branch_id                date
city                      time_id                  day
address                   quantity_sold            month
zone                      unit_price               month_name
branch_type               discount                 quarter
                          total_sale               year

The FACT_SALES table is located at the center because it contains the business events and measures that need to be analyzed.

The dimension tables provide the descriptive context necessary to interpret the information stored in the fact table.

8. Model Justification

A star schema was selected because the main requirement of the pharmacy chain is to analyze sales from different perspectives.

The FACT_SALES table represents the main business event: a completed sale. It stores the measures that can be analyzed, such as quantity sold, unit price, discounts, and total sales.

The DIM_PRODUCT dimension allows the organization to answer questions related to products, such as:

Which product sells the most?
Which category generates the highest sales?
Which brand has the best results?

The DIM_BRANCH dimension allows the organization to analyze the performance of each branch, for example:

Which branch sells the most?
Which city generates the highest revenue?
Which zone has the highest sales volume?

The DIM_TIME dimension allows historical analysis, such as:

Which month had the highest sales?
How have sales evolved over time?
Which quarter had the best results?
How do sales behave from year to year?

Therefore, the model allows the dimensions to be combined to perform analyses such as:

Sales by product + branch + month

For example:

How much revenue was generated by Acetaminophen sales at the Central Branch during August 2026?

The star schema facilitates this type of query because the dimensions contain the descriptive information, while the fact table contains the measures that are analyzed.
