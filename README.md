# Zip Password Cracking

This Python script is designed to crack passwords for zip files using a brute-force approach. It utilizes the `zipfile` library to interact with zip files and employs a list of 1,000,000 password samples to attempt to unlock the encrypted zip file.

## How It Works
1. The script iterates through the list of password samples.
2. For each password, it attempts to extract the contents of the zip file.
3. If successful, it prints password found and then the password and stops execution.

## Usage
1. Clone the repository: `git clone https://github.com/jmugambwa1/zip-password-cracking.git`
2. Make sure you have Python installed on your system.
3. Place your encrypted zip file in the same directory as the script.
4. Run the script: `python zip_cracker.py`

## Note
- Ensure you have the necessary permissions to run the script.
- Depending on the complexity of the password and the computing power of your system, the cracking process may take some time.

## Sample
```python
python zip_cracker.py
```

## Contributing
Contributions are welcome. Fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
Special thanks to the Python community for providing valuable resources and libraries.

For any questions or issues, please contact [khezajoel@gmail.com].
