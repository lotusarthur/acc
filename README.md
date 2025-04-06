### README

#### Financial Calculation Scripts

These Python scripts are designed to perform key financial calculations, including Net Present Value (NPV), Internal Rate of Return (IRR), and Dynamic Payback Period. They provide a simple and intuitive way for users to input relevant financial data and obtain the corresponding results.

#### Author
LI JINQIU

#### File Descriptions

1. **`calculate_npv.py`**
    - This script contains the `calculate_npv` function, which calculates the Net Present Value of a series of cash flows. The Net Present Value is a fundamental concept in finance, used to evaluate the profitability of an investment by discounting future cash flows back to the present.
    - **Function Signature**: `calculate_npv(discount_rate, cash_flows)`
    - **Input**:
      - `discount_rate`: A floating - point number representing the discount rate used for the NPV calculation.
      - `cash_flows`: A list of floating - point numbers where the first element is typically the initial investment (usually negative), and the rest are subsequent cash inflows.
    - **Output**: A floating - point number representing the calculated Net Present Value.

2. **`calculate_irr.py`**
    - This script includes the `calculate_irr` function, which uses the bisection method to calculate the Internal Rate of Return of a series of cash flows. The Internal Rate of Return is the discount rate at which the Net Present Value of an investment is zero.
    - **Function Signature**: `calculate_irr(cash_flows, tolerance=0.0001, max_iterations=1000)`
    - **Input**:
      - `cash_flows`: A list of floating - point numbers with the initial investment (usually negative) as the first element.
      - `tolerance`: An optional floating - point number indicating the acceptable tolerance for the NPV to be considered close enough to zero. The default value is `0.0001`.
      - `max_iterations`: An optional integer representing the maximum number of iterations allowed in the bisection method. The default value is `1000`.
    - **Output**: A floating - point number representing the calculated Internal Rate of Return. If the algorithm fails to converge within the maximum number of iterations, it returns `None`.

3. **`calculate_dynamic_payback_period.py`**
    - This script features the `calculate_dynamic_payback_period` function, which calculates the dynamic payback period of a series of cash flows. The dynamic payback period takes into account the time value of money and determines how long it takes for an investment to be recovered.
    - **Function Signature**: `calculate_dynamic_payback_period(discount_rate, cash_flows)`
    - **Input**:
      - `discount_rate`: A floating - point number representing the discount rate used for present value calculations.
      - `cash_flows`: A list of floating - point numbers where the first element is usually the initial investment (negative).
    - **Output**: A floating - point number representing the calculated dynamic payback period. If the investment cannot be recovered within the given cash flows, it returns `None`.

#### How to Use

1. **For `calculate_npv.py`**:
    - Run the script.
    - Enter the discount rate as prompted (e.g., `0.1` for 10%).
    - Enter the cash flows separated by commas (e.g., `-1000,200,300,400`).
    - The script will output the calculated Net Present Value.

2. **For `calculate_irr.py`**:
    - Run the script.
    - Enter the cash flows separated by commas.
    - The script will attempt to calculate the Internal Rate of Return and display the result as a percentage. If it fails to converge, an appropriate error message will be shown.

3. **For `calculate_dynamic_payback_period.py`**:
    - Run the script.
    - Enter the discount rate as prompted.
    - Enter the cash flows separated by commas.
    - The script will output the dynamic payback period in years, or indicate if the investment cannot be recovered.

#### Notes
- All input values should be valid floating - point numbers.
- The scripts are designed to handle invalid input gracefully and will display appropriate error messages.
- After the calculation is completed, the console window will remain open until the user presses the Enter key. 
