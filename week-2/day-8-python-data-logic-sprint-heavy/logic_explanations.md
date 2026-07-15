# Logic Explanations

## 1. Why Validation Was Done Before Revenue Calculation

Validation is performed before revenue calculation to prevent incorrect records from affecting business results.

The function `validate_order()` checks:
- If customer name is missing.
- If quantity is less than or equal to 0.
- If price is less than or equal to 0.

Invalid records are removed from the analysis because they can create incorrect results. For example, an order with price `0` or quantity `0` would affect average order value calculations and make the report inaccurate.

The pipeline follows this order:

Raw Data → Validation → Cleaning → Revenue Calculation → Reporting

This ensures that only reliable data is used for business analysis.

---

## 2. How Status Normalization Works

Status normalization is handled by the function `normalize_status()`.

The function:
1. Receives the original status value.
2. Removes extra spaces using `.strip()`.
3. Converts the value to lowercase using `.lower()`.
4. Checks if the value is `"completed"` or `"complete"`.
5. Converts both values into one standard format: `"completed"`.

Example:

Before cleaning: