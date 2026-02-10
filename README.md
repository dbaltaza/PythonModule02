# Python Module 02 - Garden Guardian 🌱

**Data Engineering for Smart Agriculture**

A 42 Lisboa project focusing on exception handling and error management in Python through the lens of agricultural IoT systems.

---

## 📋 Table of Contents

- [About](#about)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Exercises](#exercises)
- [Usage](#usage)
- [Learning Objectives](#learning-objectives)
- [Author](#author)

---

## 🎯 About

This module teaches resilient data pipeline design for agricultural systems. The project demonstrates how to build fault-tolerant monitoring systems that maintain data integrity under real-world conditions through proper exception handling.

All exercises simulate scenarios from a smart agriculture platform where sensors, data validation, and system reliability are critical.

---

## 📁 Project Structure

```
PythonModule02/
├── README.md
├── en.subject.pdf
├── ex0/
│   └── ft_first_exception.py      # Agricultural Data Validation Pipeline
├── ex1/
│   └── ft_different_errors.py     # Different Types of Problems
├── ex2/
│   └── ft_custom_errors.py        # Making Your Own Error Types
├── ex3/
│   └── ft_finally_block.py        # Finally Block - Always Clean Up
├── ex4/
│   └── ft_raise_errors.py         # Raising Your Own Errors
└── ex5/
    └── ft_garden_management.py    # Garden Management System
```

---

## ⚙️ Requirements

### General Instructions

- **Python Version**: 3.10+
- **Code Standards**: Must respect flake8 linter
- **Type Hints**: All functions and methods must include type hints
- **Error Handling**: All programs must use try/except blocks appropriately
- **Reliability**: Programs must never crash

### Authorized Functions

Each exercise specifies which built-in functions are authorized. Common ones include:
- `int()`, `print()`, `open()`, `close()`, `input()`
- Exception handling keywords: `try`, `except`, `finally`, `raise`
- Built-in exception types: `ValueError`, `TypeError`, `ZeroDivisionError`, `FileNotFoundError`, `KeyError`, etc.

---

## 🚀 Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd PythonModule02
```

2. Ensure Python 3.10+ is installed:
```bash
python3 --version
```

3. (Optional) Install flake8 for linting:
```bash
pip install flake8
```

---

## 📚 Exercises

### Exercise 0: Agricultural Data Validation Pipeline
**File**: `ex0/ft_first_exception.py`

Validates temperature readings from field sensors, filtering out corrupted data before it affects agricultural analytics.

**Key Concepts**:
- Basic try/except blocks
- ValueError handling
- Input validation
- Range checking

**Run**:
```bash
python3 ex0/ft_first_exception.py
```

---

### Exercise 1: Different Types of Problems
**File**: `ex1/ft_different_errors.py`

Demonstrates handling different error types that can occur in garden operations.

**Key Concepts**:
- ValueError, ZeroDivisionError, FileNotFoundError, KeyError
- Multiple exception types in one except block
- Error-specific handling

**Run**:
```bash
python3 ex1/ft_different_errors.py
```

---

### Exercise 2: Making Your Own Error Types
**File**: `ex2/ft_custom_errors.py`

Creates custom exception classes for garden-specific problems.

**Key Concepts**:
- Custom exception classes
- Exception inheritance
- Specific vs. general error catching
- `GardenError`, `PlantError`, `WaterError`

**Run**:
```bash
python3 ex2/ft_custom_errors.py
```

---

### Exercise 3: Finally Block - Always Clean Up
**File**: `ex3/ft_finally_block.py`

Ensures resources are cleaned up properly, even when errors occur.

**Key Concepts**:
- try/except/finally structure
- Resource cleanup
- Guaranteed execution of cleanup code

**Run**:
```bash
python3 ex3/ft_finally_block.py
```

---

### Exercise 4: Raising Your Own Errors
**File**: `ex4/ft_raise_errors.py`

Validates plant health parameters and raises appropriate errors when validation fails.

**Key Concepts**:
- Using `raise` keyword
- Creating descriptive error messages
- Input validation with custom errors
- Defensive programming

**Run**:
```bash
python3 ex4/ft_raise_errors.py
```

---

### Exercise 5: Garden Management System
**File**: `ex5/ft_garden_management.py`

Complete garden management system integrating all error handling techniques.

**Key Concepts**:
- Class-based architecture
- Custom exceptions in real applications
- Error recovery and system resilience
- Integration of all previous concepts

**Run**:
```bash
python3 ex5/ft_garden_management.py
```

---

## 💻 Usage

### Running All Tests

Run each exercise individually to see the demonstrations:

```bash
# Exercise 0
python3 ex0/ft_first_exception.py

# Exercise 1
python3 ex1/ft_different_errors.py

# Exercise 2
python3 ex2/ft_custom_errors.py

# Exercise 3
python3 ex3/ft_finally_block.py

# Exercise 4
python3 ex4/ft_raise_errors.py

# Exercise 5
python3 ex5/ft_garden_management.py
```

### Code Quality Check

Verify all files follow flake8 standards:

```bash
flake8 ex0/ft_first_exception.py \
       ex1/ft_different_errors.py \
       ex2/ft_custom_errors.py \
       ex3/ft_finally_block.py \
       ex4/ft_raise_errors.py \
       ex5/ft_garden_management.py
```

---

## 🎓 Learning Objectives

By completing this module, you will understand:

1. **Exception Handling Fundamentals**
   - How to use try/except blocks effectively
   - Different types of built-in exceptions
   - When and how to catch specific vs. general exceptions

2. **Custom Exceptions**
   - Creating custom exception classes
   - Exception inheritance hierarchies
   - Domain-specific error types

3. **Resource Management**
   - Using finally blocks for cleanup
   - Ensuring resources are always released
   - Writing resilient code

4. **Error Raising**
   - When to raise exceptions
   - Creating helpful error messages
   - Validation and defensive programming

5. **Fault-Tolerant Systems**
   - Error recovery strategies
   - Maintaining system stability
   - Building reliable data pipelines

---

## 🔍 Key Concepts Explained

### Why Try/Except Blocks?

Exception handling prevents programs from crashing when unexpected situations occur. In agricultural IoT systems, sensors can fail, data can be corrupted, and network connections can drop. Proper error handling ensures the system continues operating despite these issues.

### Custom Exceptions

Custom exception types make code more readable and maintainable. Instead of generic `Exception`, you can catch `PlantError` or `WaterError`, making it clear what went wrong.

### Finally Blocks

The `finally` block always executes, whether an exception occurred or not. This is crucial for:
- Closing files
- Releasing network connections
- Cleaning up resources
- Ensuring system consistency

### Raising Exceptions

Programs should raise exceptions when they detect invalid states. This is better than returning error codes or allowing invalid data to propagate through the system.

---

## 📝 Notes for 42 Evaluation

### Important Points

- All functions include type hints as required
- Code respects flake8 standards (verified)
- Each exercise is in its own file
- Programs demonstrate both normal and error scenarios
- No unauthorized functions are used
- Programs never crash - all errors are handled gracefully

### During Defense

Be prepared to explain:
- How exception handling works in Python
- The difference between various exception types
- Why custom exceptions are useful
- How finally blocks guarantee cleanup
- When and why to raise exceptions
- How these concepts apply to real-world data engineering

---

## 👨‍💻 Author

**Dinis Marques**  
42 Lisboa - Common Core  
Module: Python Module 02  
Project: Garden Guardian

---

## 📄 License

This project is part of the 42 Lisboa curriculum.

---

*"In agriculture, as in code, resilience is everything. Handle your exceptions, harvest success." 🌾*
