# Bank System (Simple Bank Application)

This is a mini project for a Simple Bank Application implemented in Python. The project provides basic banking functionalities, including user authentication, withdraw, and deposit operations.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [How to Run](#how-to-run)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Simple Bank Application is a command-line-based program that simulates basic banking operations. It consists of two classes: `transaction` and `login`.

- The `transaction` class handles withdraw and deposit operations for a user's account. It keeps track of the account balance and updates it based on the chosen transaction.

- The `login` class handles user authentication. Users must provide their username and password to access the banking features. The default login credentials are username: "user" and password: "user123" for demonstration purposes.

## Features

- User Authentication: Only registered users can access the banking functionalities by providing the correct username and password.

- Withdraw: Users can withdraw funds from their account. The application calculates the new available balance accordingly.

- Deposit: Users can deposit funds into their account. The application updates the available balance after each deposit.

## Usage

To use the Simple Bank Application:

1. Clone this repository to your local machine using the following command:
```
git clone <repository-url>
```

2. Open the Python script containing the mini project:
```
cd Simple-Bank-Application
python bank_application.py
```

3. Enter the default login credentials (username: "user", password: "user123") or use your registered account credentials.

4. Once logged in, you will be presented with the transaction options: withdraw or deposit. Choose the desired transaction type and follow the prompts to enter the amount.

5. The application will display the updated available balance after each transaction.

## How to Run

Make sure you have Python installed on your system. The application runs on Python 3.

```bash
python bank_application.py
```

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---
Feel free to customize the README file with more details or additional sections if needed. Make sure to include proper attributions, license information, and any other relevant project-related details. Happy coding!
