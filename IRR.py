def calculate_npv(discount_rate, cash_flows):
    """
    Calculate the Net Present Value (NPV) of a series of cash flows.

    Args:
        discount_rate (float): The discount rate used for NPV calculation.
        cash_flows (list): A list of cash flows, where the first element is the initial investment (usually negative).

    Returns:
        float: The calculated Net Present Value.
    """
    npv = 0
    for i, cash_flow in enumerate(cash_flows):
        # Calculate the present value of each cash flow and add it to the NPV
        npv += cash_flow / ((1 + discount_rate) ** i)
    return npv


def calculate_irr(cash_flows, tolerance=0.0001, max_iterations=1000):
    """
    Calculate the Internal Rate of Return (IRR) of a series of cash flows using the bisection method.

    Args:
        cash_flows (list): A list of cash flows, where the first element is the initial investment (usually negative).
        tolerance (float): The acceptable tolerance for the NPV to be considered close enough to zero.
        max_iterations (int): The maximum number of iterations allowed in the bisection method.

    Returns:
        float: The calculated Internal Rate of Return.
    """
    # Set initial bounds for the bisection method
    low = -1.0
    high = 100.0

    for _ in range(max_iterations):
        # Calculate the midpoint (current guess for IRR)
        mid = (low + high) / 2

        # Calculate the NPV at the current guess
        npv = calculate_npv(mid, cash_flows)

        # Check if the NPV is within the tolerance
        if abs(npv) < tolerance:
            return mid

        # Adjust the bounds based on the sign of the NPV
        if npv > 0:
            low = mid
        else:
            high = mid

    # If the maximum number of iterations is reached, return None
    return None


if __name__ == "__main__":
    # Prompt the user to enter cash flows separated by commas
    cash_flows_input = input("Please enter the cash flows separated by commas (e.g., -1000,200,300,400): ")
    try:
        # Convert the input string to a list of floats
        cash_flows = [float(x) for x in cash_flows_input.split(',')]
        # Calculate the IRR
        irr = calculate_irr(cash_flows)
        if irr is not None:
            print(f"The Internal Rate of Return (IRR) is: {irr * 100:.2f}%")
        else:
            print("Could not converge to a solution within the maximum number of iterations.")
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers separated by commas.")

    # Keep the console window open until the user presses Enter
    input("Press Enter to exit...")