# 🧮 Infix to Postfix Converter (Shunting Yard)

An implementation of Edsger Dijkstra's famous **Shunting Yard Algorithm**. 

This algorithm parses standard human-readable mathematical expressions (Infix notation, like `A + B * C`) and converts them into machine-readable Reverse Polish Notation (Postfix notation, like `A B C * +`). It uses a **Stack** data structure to temporarily hold operators and parentheses, ensuring that mathematical order of operations (PEMDAS/BODMAS) is strictly followed.

**Why is this useful?** 
Computers cannot easily evaluate standard math equations because of parentheses and operator precedence. By converting the equation to Postfix first, a computer can evaluate the entire expression in a single, blazing-fast left-to-right sweep without ever needing to look backwards.

---

## ⏱️ Complexity
* **Time Complexity:** $O(n)$ (Each character in the string is processed and pushed/popped from the stack at most once).
* **Space Complexity:** $O(n)$ (In the worst-case scenario, the stack will store all the operators and parentheses from the expression).
