import sys
from fpdf import FPDF

# this help to change the color of cli interface
CLI_COLORS = {
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "BLUE": "\033[34m",
    "YELLOW": "\033[93m",
    "RESET": "\033[0m",
}

# this will store all item data i.e -
# {"item": "abc",  "price": 52, "quantity": 3, "total": "156"} total is counted by "price * quantity"
bill_items = []

# created a global list i can create global variable but it increase complexity
# so i creat list to store sum of all item price
all_items_price_sum = [0]


def main():
    # this program name is billing.py but as per cs50 requirements it is in project.py file
    print(
        f"{CLI_COLORS['GREEN']}============ Welcome To Billing.py ============{CLI_COLORS['RESET']}"
    )

    # this will call menu function and sotore the return value
    option = menu()
    # calling function as per menu return value
    if option == "create_bill":
        creat_bill_page()
        create_bill_pdf()
        exit_program()
    elif option == "exit":
        exit_program()


# this is program menu function to display program menu
def menu():
    # printing menu
    print(f"{CLI_COLORS['BLUE']}1. Create Bill \n2. Exit{CLI_COLORS['RESET']}")
    # taking input until user enter valid option
    while True:
        # taking input and handeling error
        try:
            option = int(
                input(f"{CLI_COLORS['YELLOW']}Enter your option: {CLI_COLORS['RESET']}")
            )
        except ValueError:
            print(f"{CLI_COLORS['RED']}Enter a valid Option{CLI_COLORS['RESET']}")
            continue

        # performing operation based on input
        match option:
            case 1:
                return "create_bill"
            case 2:
                return "exit"
            case _:
                print(f"{CLI_COLORS['RED']}Enter a valid Option{CLI_COLORS['RESET']}")
                continue


# this function help to creat bill list
def creat_bill_page():

    print_empty_line()

    #  printing the operation name performed in this function
    print(
        f"{CLI_COLORS['GREEN']}============ Create Bill ============{CLI_COLORS['RESET']}"
    )
    # dummy variable to check is user entering data first time or not initialize as true
    first = True
    while True:
        # if use is first time the skip the conformation message and set first to false
        if first:
            first = False
        else:
            if not (
                input("Do You want to add new item \n[y]-yes \n[any other char than y]-No \nChoice: ").lower() in ["y", "yes"]
            ):
                # appending all items bill amount in last
                bill_items.append(["", "", "Final Amount", f"${round(all_items_price_sum[0], 2)}"])

                return

        print_empty_line()

        # take input item name as string
        item = take_input_item_info(
            f"{CLI_COLORS['YELLOW']}Enter Item Name: {CLI_COLORS['RESET']}", "string"
        )

        # if user want to clear completer row data (this value is comming form take_input_item_info func as return value)
        if item == "clear_entry":
            continue

        # take input item price as float (real number)
        price_of_item = take_input_item_info(
            f"{CLI_COLORS['YELLOW']}Enter Price of one '{item}': {CLI_COLORS['RESET']}",
            "real",
        )

        # if user want to clear completer row data (this value is comming form take_input_item_info func as return value)
        if price_of_item == "clear_entry":
            continue

        # take input item price as float (intiger number)
        quantity = take_input_item_info(
            f"{CLI_COLORS['YELLOW']}Enter quantity of '{item}': {CLI_COLORS['RESET']}",
            "intiger",
        )

        # if user want to clear completer row data (this value is comming form take_input_item_info func as return value)
        if quantity == "clear_entry":
            continue

        # calculating total price
        total = price_of_item * quantity

        # calculating price of all item in the bill list
        all_items_price_sum[0] += int(total)

        # appending item to list as list
        bill_items.append(
            [
                item,
                f"${round(price_of_item, 2)}",
                round(quantity, 2),
                f"${round(total, 2)}",
            ]
        )


# it take input as per argument what data type needed in return value
def take_input_item_info(input_message, data_type):
    # taking input untill user input valid data
    while True:
        # error handeling and checking number must be greater than 0
        try:
            if data_type == "intiger":
                int_check = int(input(input_message))
                if int_check > 0:
                    return int(int_check)
                else:
                    print("Input is samller than 1")
                    continue
            elif data_type == "real":
                float_check = float(input(input_message))
                if float_check > 0:
                    return float(float_check)
                else:
                    print("Input is samller than 1")
                    continue
            elif data_type == "string":
                return str(input(input_message))

        # operation if error occur
        except (TypeError, ValueError, EOFError):
            while True:
                quiting = input(
                    f"{CLI_COLORS['RED']}\n1. Confirm Exit \n2. Clear This Complete Row \n3. Do Nothing just take input again {CLI_COLORS['BLUE']}\nChoose Option: {CLI_COLORS['RESET']}"
                ).lower()

                # here match option as string not as int
                match quiting:
                    case "1":
                        exit_program()
                    case "2":
                        return "clear_entry"
                    case "3":
                        print_empty_line()
                        break  # this will exit this while toop and prompt user again
                    case _:
                        continue  # this will ask user to choose option again


# this program print messege and exit
def exit_program():
    sys.exit(
        f"{CLI_COLORS['GREEN']}============ Good Bye 🙋 ============{CLI_COLORS['RESET']}"
    )


# this program print empty line and created because
# if i write print any where in program while reviewing
# i or reviewer can think i forgot to write somthing in print
def print_empty_line():
    print()


#  creating pdf
def create_bill_pdf():
    pdf = FPDF()
    pdf.add_page()

    # printing header to the pdf
    pdf.set_font("Arial", size=16, style="B")
    pdf.cell(0, 10, txt="--- CS50 Shop ---", ln=True, align="C")

    # initialize the table header value
    headers = ["Items", "Price", "Quantity", "Total"]
    # this will create 4 column or 5 vertical line on pdf page
    each_cell_width = pdf.w / 5
    # initialize each cell height
    each_cell_height = 11

    # this will set font bold
    pdf.set_font("Times", size=10, style="B")
    # printing header to the pdf
    for header in headers:
        pdf.cell(each_cell_width, each_cell_height, txt=header, border=True, align="C")
    pdf.ln(each_cell_height)

    # this will set font normal
    pdf.set_font("Times", size=9, style="")
    # printing data or bill data
    for row in bill_items:
        for item in row:
            pdf.cell(each_cell_width, each_cell_height, txt=str(item), border=True, align="C")
        pdf.ln(each_cell_height)

    # saving/outputing file as bill.pdf
    pdf.output("bill.pdf")


# calling main function
if __name__ == "__main__":
    main()
