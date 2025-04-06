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


if __name__ == "__main__":
    try:
        # Prompt the user to enter the discount rate
        discount_rate = float(input("Please enter the discount rate (e.g., 0.1 for 10%): "))
        # Prompt the user to enter the cash flows separated by commas
        cash_flows_input = input("Please enter the cash flows separated by commas (e.g., -1000,300,300,300,300): ")
        # Convert the input string to a list of floats
        cash_flows = [float(cf) for cf in cash_flows_input.split(',')]
        # Calculate the NPV
        npv = calculate_npv(discount_rate, cash_flows)
        print(f"Net Present Value (NPV): {npv}")
    except ValueError:
        print("Invalid input. Please make sure to enter valid numbers.")


    input("Press Enter to exit...")
    