import os

def clear_screen():
    os.system('clear')

def show_menu():
    print("╔════════════════════════╗")
    print("║    Terminal Calculator  ║")
    print("╠════════════════════════╣")
    print("║ [1] ➕ Addition         ║")
    print("║ [2] ➖ Subtraction      ║")
    print("║ [3] ✖️ Multiplication   ║")
    print("║ [4] ➗ Division         ║")
    print("║ [5] ❌ Exit            ║")
    print("╚════════════════════════╝")

def calculator():
    while True:
        clear_screen()
        show_menu()
        choice = input("Select an option (1-5): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = num1 + num2
                symbol = "+"
            elif choice == '2':
                result = num1 - num2
                symbol = "-"
            elif choice == '3':
                result = num1 * num2
                symbol = "×"
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero!")
                    input("Press Enter to continue...")
                    continue
                result = num1 / num2
                symbol = "÷"

            clear_screen()
            print(f"\n🧮 {num1} {symbol} {num2} = {result}\n")
            input("Press Enter to continue...")

        elif choice == '5':
            print("Exiting calculator...")
            break
        else:
            print("Invalid input! Try again.")
            input("Press Enter to continue...")

calculator()