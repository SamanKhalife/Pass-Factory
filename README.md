# Pass-Factory
This Python script generates all possible combinations of a given length using a specified set of characters, including letters, digits, and symbols. The script then saves these combinations to a specified file.

### Note:
- **Educational Use Only**: This script is for educational purposes only. Any other use is not my responsibility.
- **Watch Your Memory Usage**: Generating a large number of combinations can consume substantial memory and disk space. Use with caution.

## Features
- **Character Set Customization**: Choose whether to include letters, digits, and symbols in the combinations.
- **Dynamic Length**: Specify the length of the combinations to generate.
- **File Output**: Save all generated combinations to a user-defined file.

## How to Use
1. First, **clone** this repository to your local machine using the following command:

```bash
git clone https://github.com/SamanKhalife/Pass-Factory.git
```
2. **Navigate** to the Project Directory
Change your directory to the cloned repository:

```bash
cd Pass-Factory
```

3. **Run** the script in your terminal or command line:
    ```bash
    python3 pass-factory.py
    ```

4. **Follow the Prompts**:
    - **Include letters?** (yes/no): Specify if letters should be included in the combinations.
    - **Include digits?** (yes/no): Specify if digits should be included.
    - **Include symbols?** (yes/no): Specify if symbols should be included.
    - **Enter the desired combination length**: Input the length of each combination.
    - **Enter the file name to save the combinations**: Provide the name of the file where combinations will be saved.

## Example Usage

```bash
python3 pass-factory.py
```

**Output:**

```
Include letters? (yes/no): yes
Include digits? (yes/no): yes
Include symbols? (yes/no): no
Enter the desired combination length: 2
Enter the file name to save the combinations (e.g., 'combinations.txt'): combinations.txt
```

The script will generate all possible combinations of length 2 using letters and digits and save them to `combinations.txt`.

## Important Notes

- **Memory Usage**: Generating and saving all combinations can consume a large amount of memory and disk space, especially for longer combination lengths.
- **Error Handling**: The script includes basic error handling for invalid inputs and potential memory errors.

Made by [Saman Khalife](https://github.com/SamanKhalife)
