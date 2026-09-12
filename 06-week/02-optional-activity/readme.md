# WEEK 06 - BUSINESS INTELLIGENCE

## Define the Grain and Prepare Test Data

---

## 1. Grain Definition

The grain of the fact table **FACT_ACADEMIC_PERFORMANCE** is:

> **One row represents the academic performance of one student in one course during one academic period.**

This grain was selected because it preserves the individual academic performance detail of each student for each course and academic period.

With this level of detail, the university can analyze academic performance by:

- Student
- Course
- Academic program
- Academic period

It also allows the data to be aggregated to higher levels when necessary.

For example, the data can be analyzed to obtain:

- The average grade of a course.
- The number of student-course records with low academic performance.
- The Low Academic Performance Rate for an academic period.
- The number of failed courses.

The selected grain is consistent with the Week 04 model, where **FACT_ACADEMIC_PERFORMANCE** represents the academic performance of a student in a course during an academic period.

---

## 2. Measures at This Grain

The following measures are appropriate for the selected grain:

| Measure | Description |
|---|---|
| `student_count` | Represents one student in the academic performance record. It has a value of 1 and can be summed to count student-course records. |
| `grade` | Represents the student's grade in the course. It can be analyzed using average, minimum, or maximum. |
| `failed_course_count` | Indicates whether the student failed the course. It has a value of 1 or 0 and can be summed. |
| `low_performance_flag` | Indicates whether the student has low academic performance. It has a value of 1 or 0 and can be used to calculate the Low Academic Performance Rate. |

### Grade Aggregation

The `grade` measure is not added together because the sum of grades does not provide meaningful information.

Instead, grades should be analyzed using statistical functions such as:

- **Average**
- **Minimum**
- **Maximum**

The `student_count`, `failed_course_count`, and `low_performance_flag` measures can be aggregated because their values represent counts or indicators at the selected grain.

---

## 3. Test Data

A test dataset with **15 rows** was created in Excel according to the defined grain.

Each row represents:

> **One student + one course + one academic period.**

### Test Data Structure

The test data uses the following fields:

| Field | Description |
|---|---|
| `performance_id` | Unique identifier of the academic performance record. |
| `time_id` | Identifies the academic period. |
| `student_id` | Identifies the student. |
| `course_id` | Identifies the course. |
| `program_id` | Identifies the academic program. |
| `student_count` | Represents one student in the academic performance record. |
| `grade` | Student's grade in the course. |
| `failed_course_count` | Indicates whether the student failed the course. |
| `low_performance_flag` | Indicates whether the student has low academic performance. |

### Excel Test Dataset

The Excel file contains **15 test records** distributed across different students, courses, academic programs, and academic periods.

The data is coherent with the selected grain because each record represents the academic performance of **one student in one course during one academic period**.

| performance_id | time_id | student_id | course_id | program_id | student_count | grade | failed_course_count | low_performance_flag |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1001 | 101 | 10 | 1 | 4.2 | 0 | 0 |
| 2 | 1 | 1002 | 101 | 10 | 1 | 3.5 | 0 | 0 |
| 3 | 1 | 1003 | 102 | 10 | 1 | 2.8 | 0 | 1 |
| 4 | 1 | 1004 | 102 | 11 | 1 | 2.5 | 1 | 1 |
| 5 | 1 | 1005 | 103 | 11 | 1 | 4.0 | 0 | 0 |
| 6 | 2 | 1001 | 104 | 10 | 1 | 3.8 | 0 | 0 |
| 7 | 2 | 1002 | 102 | 10 | 1 | 2.9 | 0 | 1 |
| 8 | 2 | 1003 | 103 | 10 | 1 | 3.6 | 0 | 0 |
| 9 | 2 | 1004 | 104 | 11 | 1 | 2.4 | 1 | 1 |
| 10 | 2 | 1005 | 101 | 11 | 1 | 4.5 | 0 | 0 |
| 11 | 3 | 1001 | 103 | 10 | 1 | 3.2 | 0 | 0 |
| 12 | 3 | 1002 | 104 | 10 | 1 | 4.1 | 0 | 0 |
| 13 | 3 | 1003 | 101 | 10 | 1 | 2.7 | 0 | 1 |
| 14 | 3 | 1004 | 103 | 11 | 1 | 3.0 | 0 | 1 |
| 15 | 3 | 1005 | 102 | 11 | 1 | 3.9 | 0 | 0 |

---

## 4. What Happens With a Coarser Grain?

If a coarser grain were selected, such as:

> **One row represents the total academic performance of a program during an academic period.**

the model would contain less detail.

It would still be possible to analyze general academic performance by academic program and academic period, but the model would lose individual student and course-level information.

For example, the following analyses would be lost or limited:

- Identifying which specific students have low academic performance.
- Identifying which specific courses have the highest number of students with low academic performance.
- Analyzing the grade of an individual student in a specific course.
- Identifying individual failed courses.
- Comparing the academic performance of individual students.

Therefore, the selected grain is preferable because it preserves detailed information and allows the university to aggregate the data to higher levels when needed.

---

## 5. Conclusion

The selected grain for **FACT_ACADEMIC_PERFORMANCE** is:

> **One student in one course during one academic period.**

This grain provides enough detail to analyze individual academic performance and calculate measures such as:

- Student-course record counts
- Grades
- Failed courses
- Low-performance indicators

The **15 test records** created in Excel follow the selected grain and are consistent with the dimensions defined in the Week 04 star schema.

Using this level of detail allows the university to analyze academic performance from the individual student level up to:

- Courses
- Academic programs
- Academic periods

This supports the calculation of the **Low Academic Performance Rate** and helps the university make decisions related to academic support and student performance.