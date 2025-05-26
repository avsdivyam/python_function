# ☕ Coffee Machine Program

This program simulates a simple coffee vending machine that serves `espresso`, `latte`, or `cappuccino`. It manages resources, processes coins, and handles user interactions.

---

## 📋 Features & Requirements

### 1. User Prompt  
- Prompts the user with:  
  ```
  What would you like? (espresso/latte/cappuccino):
  ```  
- Based on the user's input, the machine proceeds accordingly.
- The prompt repeats after each action is completed (serving drink, showing report, etc.).

---

### 2. Turn Off the Machine  
- Input `off` to shut down the machine (intended for maintenance).  
- The program will terminate immediately.

---

### 3. Print Report  
- Input `report` to display current resource levels. Example output:
  ```
  Water: 100ml  
  Milk: 50ml  
  Coffee: 76g  
  Money: $2.5
  ```

---

### 4. Check Resources  
- Before making a drink, the machine checks if sufficient ingredients are available.
- If not enough, it displays:
  ```
  Sorry there is not enough [ingredient].
  ```
- It does **not** proceed to make the drink.

---

### 5. Process Coins  
- If ingredients are sufficient, user is prompted to insert coins:
  - Quarters = $0.25  
  - Dimes = $0.10  
  - Nickels = $0.05  
  - Pennies = $0.01  
- The total amount is calculated from user input.

---

### 6. Transaction Check  
- If the inserted amount is **less than** the drink cost:
  ```
  Sorry that's not enough money. Money refunded.
  ```
- If enough money is inserted:
  - Profit is added to the machine.
  - If excess money was inserted, change is returned:
    ```
    Here is $[change] dollars in change.
    ```

---

### 7. Make Coffee  
- If the transaction is successful and ingredients are available:
  - Resources are deducted accordingly.
  - A success message is shown:
    ```
    Here is your [drink]. Enjoy!
    ```

#### Example Before and After Report for a Latte:
**Before:**
```
Water: 300ml  
Milk: 200ml  
Coffee: 100g  
Money: $0
```

**After:**
```
Water: 100ml  
Milk: 50ml  
Coffee: 76g  
Money: $2.5
```

---

## ✅ Summary

This program manages:
- User interactions
- Machine status and resources
- Coin-based transactions
- Realistic feedback and error messages
