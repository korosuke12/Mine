### 📞 Phone Number Generator – Project Description

This Streamlit application generates **fake phone numbers** based on user-defined settings. It provides an interactive web interface where users can choose a country code, specify a phone number prefix, define the total number length, and generate multiple phone numbers at once.

#### Features

* **Country Code Selection:** Supports multiple country codes including USA (+1), UK (+44), India (+91), Australia (+61), Japan (+81), and Germany (+49).
* **Custom Prefix:** Allows users to add a custom starting sequence to generated phone numbers.
* **Flexible Number Length:** Users can define the total length of the phone number (excluding the country code).
* **Bulk Generation:** Generates between 1 and 1000 phone numbers in a single operation.
* **Interactive Display:** Displays generated phone numbers in a tabular format using a Pandas DataFrame.
* **CSV Export:** Enables users to download the generated phone numbers as a CSV file for further use.

#### How It Works

1. The user selects a country code from the sidebar.
2. The user optionally enters a prefix and specifies the desired phone number length.
3. The application generates random digits to fill the remaining length after the prefix.
4. Each generated number is combined with the selected country code.
5. The results are displayed in a table and can be downloaded as a CSV file.

#### Technologies Used

* **Python** – Core programming language.
* **Streamlit** – For building the interactive web interface.
* **Pandas** – For organizing generated numbers into a tabular structure.
* **Random Module** – For generating random numeric sequences.

#### Use Cases

* Software testing and QA environments.
* Demonstrating phone number validation systems.
* Creating sample datasets for educational purposes.
* Testing database imports and exports.

**Note:** The generated phone numbers are randomly created and intended for testing, development, and demonstration purposes only. They do not guarantee correspondence to real or active phone numbers.
