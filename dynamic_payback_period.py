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


def calculate_dynamic_payback_period(discount_rate, cash_flows):
    """
    Calculate the dynamic payback period of a series of cash flows.

    Args:
        discount_rate (float): The discount rate used for present value calculations.
        cash_flows (list): A list of cash flows, where the first element is the initial investment (usually negative).

    Returns:
        float: The calculated dynamic payback period. If not recoverable, returns None.
    """
    cumulative_pv = 0
    for i, cash_flow in enumerate(cash_flows):
        pv = cash_flow / ((1 + discount_rate) ** i)
        cumulative_pv += pv
        if cumulative_pv >= 0:
            if i == 0:
                return 0
            previous_pv = cumulative_pv - pv
            fraction = -previous_pv / pv
            return i - 1 + fraction
    return None


if __name__ == "__main__":
    # Prompt the user to enter the discount rate
    discount_rate_input = input("Please enter the discount rate (e.g., 0.1 for 10%): ")
    try:
        discount_rate = float(discount_rate_input)
        # Prompt the user to enter cash flows separated by commas
        cash_flows_input = input("Please enter the cash flows separated by commas (e.g., -1000,200,300,400): ")
        cash_flows = [float(x) for x in cash_flows_input.split(',')]
        # Calculate the dynamic payback period
        payback_period = calculate_dynamic_payback_period(discount_rate, cash_flows)
        if payback_period is not None:
            print(f"The dynamic payback period is: {payback_period:.2f} years")
        else:
            print("The investment cannot be recovered within the given cash flows.")
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")

    # Keep the console window open until the user presses Enter
    input("Press Enter to exit...")
    