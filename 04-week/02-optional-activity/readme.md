# Week 04 - Business Intelligence

## 1. Fact Table Definition

### Business Process: Student Enrollment

For this model, the selected business process is **student enrollment** at a university.

The fact table represents each enrollment event of a student in a course during an academic period.

### Fact Table: FACT_ENROLLMENT

The fact table contains the dimension keys and the measures that can be aggregated.

**Measures:**

- `enrollment_count`: represents an enrollment and can be summed.
- `enrollment_value`: represents the amount paid for the enrollment and can be summed when this data is available.

Grades are not used as a summable measure because it does not make sense to add grades from different students. Grades can instead be analyzed using averages, maximums, or minimums.

### FACT_ENROLLMENT Structure

- `enrollment_id` - Primary key.
- `time_id` - Foreign key.
- `student_id` - Foreign key.
- `course_id` - Foreign key.
- `program_id` - Foreign key.
- `enrollment_count` - Measure.
- `enrollment_value` - Measure.

---

## 2. Dimension Design

The model contains four dimensions, including the Time dimension.

### Time Dimension: DIM_TIME

Allows enrollment data to be analyzed according to different time periods.

**Attributes:**

- `time_id`
- `date`
- `day`
- `month`
- `quarter`
- `year`
- `academic_period`

### Student Dimension: DIM_STUDENT

Allows enrollment data to be analyzed according to student characteristics.

**Attributes:**

- `student_id`
- `name`
- `age`
- `gender`
- `semester`

### Course Dimension: DIM_COURSE

Allows enrollment data to be analyzed according to courses.

**Attributes:**

- `course_id`
- `course_name`
- `course_code`
- `credits`
- `course_type`

### Academic Program Dimension: DIM_PROGRAM

Allows enrollment data to be analyzed according to the academic program of the student.

**Attributes:**

- `program_id`
- `program_name`
- `faculty`
- `academic_level`

---

## 3. Star Schema

The star schema consists of a central fact table and four dimensions connected through their keys.

```text
                         ┌──────────────────────┐
                         │      DIM_TIME        │
                         ├──────────────────────┤
                         │ PK time_id           │
                         │ date                 │
                         │ day                  │
                         │ month                │
                         │ quarter              │
                         │ year                 │
                         │ academic_period      │
                         └──────────┬───────────┘
                                    │
                                    │
┌──────────────────────┐            │            ┌────────────────────────┐
│    DIM_STUDENT       │            │            │      DIM_COURSE        │
├──────────────────────┤            │            ├────────────────────────┤
│ PK student_id        │            │            │ PK course_id           │
│ name                 │            │            │ course_name            │
│ age                  │            │            │ course_code            │
│ gender               │            │            │ credits                │
│ semester             │            │            │ course_type            │
└──────────┬───────────┘            │            └───────────┬────────────┘
           │                        │                        │
           │                        │                        │
           │              ┌─────────▼──────────┐             │
           └─────────────►│  FACT_ENROLLMENT   │◄────────────┘
                          ├─────────────────────┤
                          │ PK enrollment_id    │
                          │ FK time_id          │
                          │ FK student_id       │
                          │ FK course_id        │
                          │ FK program_id       │
                          │ enrollment_count    │
                          │ enrollment_value    │
                          └──────────▲──────────┘
                                     │
                                     │
                          ┌──────────┴───────────┐
                          │     DIM_PROGRAM      │
                          ├──────────────────────┤
                          │ PK program_id        │
                          │ program_name         │
                          │ faculty              │
                          │ academic_level       │
                          └──────────────────────┘