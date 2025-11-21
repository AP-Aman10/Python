# =====================================================================
#                ULTIMATE CAFE MANAGEMENT SYSTEM
#                   Realistic POS Professional
# =====================================================================

import datetime
import os

# ANSI Colors
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"

# ------------------------ MENU DATABASE -----------------------------
menu = {
    "C01": ["Coffee", 50],
    "T02": ["Tea", 20],
    "S03": ["Sandwich", 70],
    "B04": ["Burger", 120],
    "P05": ["Pasta", 150],
    "D06": ["Cold Drink", 40],
    "F07": ["French Fries", 60],
    "M08": ["Momos", 80],
    "P09": ["Pizza", 200],
    "I10": ["Ice Cream", 50]
}

daily_sales = []  # Stores all bills of the day


# ------------------------ CLEAR SCREEN -----------------------------
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# ------------------------ SHOW MENU -----------------------------
def show_menu():
    print(CYAN + "\n================== MENU LIST ==================" + RESET)
    print(YELLOW + " CODE    ITEM                PRICE" + RESET)
    print(CYAN + "----------------------------------------------" + RESET)

    for code, data in menu.items():
        print(GREEN + f" {code:<6} {data[0]:20} ₹{data[1]}" + RESET)

    print(CYAN + "==============================================\n" + RESET)


# ------------------------ TAKE ORDER ------------------------
def take_order():
    order = {}

    print(MAGENTA + "👉 Enter item codes separated by commas (C01,B04,P09)" + RESET)
    codes = input(GREEN + "Enter Codes: " + RESET).upper().replace(" ", "").split(",")

    for code in codes:
        if code in menu:
            while True:
                try:
                    qty = int(input(BLUE + f"Quantity for {menu[code][0]}: " + RESET))
                    if qty > 0:
                        order[code] = order.get(code, 0) + qty
                        break
                    else:
                        print(RED + "❌ Quantity must be greater than 0!" + RESET)
                except ValueError:
                    print(RED + "❌ Enter numbers only!" + RESET)
        else:
            print(RED + f"❌ Invalid Code: {code} (skipped)" + RESET)

    return order


# ------------------------ BILL CALCULATION ------------------------
def calculate_bill(order):
    subtotal = sum(menu[c][1] * q for c, q in order.items())
    gst = subtotal * 0.05
    total = subtotal + gst
    return subtotal, gst, total


# ------------------------ SAVE BILL TO FILE (UTF-8 FIX APPLIED) ------------------------
def save_receipt(order, subtotal, gst, total):
    os.makedirs("Bills", exist_ok=True)
    filename = "Bills/" + datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + ".txt"

    # *** FIX: Force UTF-8 encoding to avoid Rupee symbol error ***
    with open(filename, "w", encoding="utf-8") as file:
        file.write("AMAN'S CAFE - OFFICIAL BILL\n")
        file.write("----------------------------------\n")

        for c, qty in order.items():
            name, price = menu[c]
            file.write(f"{name} x{qty} - ₹{price * qty}\n")

        file.write("----------------------------------\n")
        file.write(f"Subtotal: ₹{subtotal}\n")
        file.write(f"GST 5%: ₹{gst}\n")
        file.write(f"Total: ₹{total}\n")

    print(GREEN + f"\n📄 Bill saved as: {filename}" + RESET)


# ------------------------ PRINT RECEIPT ------------------------
def print_receipt(order, subtotal, gst, total):
    print(YELLOW + "\n\n========== CUSTOMER RECEIPT ==========" + RESET)
    print(BLUE + "         Aman Café - India" + RESET)
    print(" Date:", datetime.datetime.now().strftime("%d-%m-%Y  %I:%M:%S %p"))
    print(YELLOW + "---------------------------------------" + RESET)

    for code, qty in order.items():
        name, price = menu[code]
        print(f"{name:15} x{qty}  → ₹{price * qty}")

    print(YELLOW + "---------------------------------------" + RESET)
    print(GREEN + f"Subtotal           : ₹{subtotal}")
    print(f"GST (5%)           : ₹{gst:.2f}")
    print(f"TOTAL PAYABLE      : ₹{total:.2f}" + RESET)
    print(YELLOW + "---------------------------------------" + RESET)
    print(MAGENTA + "      Thanks for visiting! 😊" + RESET)


# ------------------------ ADMIN: DAILY REPORT ------------------------
def daily_report():
    print(CYAN + "\n========== DAILY SALES REPORT ==========" + RESET)

    if not daily_sales:
        print(RED + "No sales today yet." + RESET)
        return

    total_income = sum(s["total"] for s in daily_sales)

    for i, sale in enumerate(daily_sales, 1):
        print(GREEN + f"\nBill {i} - ₹{sale['total']}" + RESET)

    print(YELLOW + f"\nTOTAL INCOME TODAY = ₹{total_income}" + RESET)


# ------------------------ MAIN PROGRAM ------------------------
while True:
    clear()
    print(CYAN + "========== WELCOME TO AMAN'S CAFE ==========" + RESET)
    print(GREEN + "\n1. Take Order")
    print("2. Show Menu")
    print("3. Admin Report")
    print("4. Exit" + RESET)

    choice = input(YELLOW + "\nSelect Option: " + RESET)

    # TAKE ORDER
    if choice == "1":
        clear()
        show_menu()
        order = take_order()
        if order:
            subtotal, gst, total = calculate_bill(order)
            print_receipt(order, subtotal, gst, total)
            save_receipt(order, subtotal, gst, total)

            daily_sales.append({"order": order, "total": total})

        input(MAGENTA + "\nPress Enter to continue..." + RESET)

    # SHOW MENU
    elif choice == "2":
        clear()
        show_menu()
        input(GREEN + "\nPress Enter..." + RESET)

    # ADMIN
    elif choice == "3":
        clear()
        daily_report()
        input("\nPress Enter...")

    # EXIT
    elif choice == "4":
        clear()
        print(GREEN + "Thank you for using Aman Café POS System!" + RESET)
        break

    else:
        print(RED + "❌ Invalid choice!" + RESET)
        input()
