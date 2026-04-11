

# It's easy to write a one-line script that converts Celsius to Fahrenheit and Kelvin. But what happens if the user accidentally types a word instead of a number? A basic script will immediately crash.

* I wanted to build something bulletproof, so I engineered a continuous application loop:

# Tech Highlights:
* 🔹 Exception Handling: Implemented a try/except ValueError block so the program gracefully warns the user instead of throwing a fatal error if they enter invalid data.

* 🔹 Continuous Execution: Built a while True loop so users can perform multiple conversions without restarting the script.

* 🔹 Clean Formatting: Utilized Python f-strings to lock decimal places down to .1f and .2f for professional, readable terminal outputs.


