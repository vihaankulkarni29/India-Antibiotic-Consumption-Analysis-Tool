# India Antibiotic Consumption Analysis Tool

This tool scrapes and analyzes data from specified public health articles to provide a summary of antibiotic consumption patterns in India. It extracts key metrics, compares them against WHO guidelines, and identifies the most prevalent antibiotics, generating a concise report.

## Features

-   **Web Scraping**: Fetches the latest text content from predefined medical and public health articles.
-   **Data Extraction**: Uses regular expressions to parse the text and extract key data points on antibiotic consumption.
-   **Structured Analysis**: Organizes extracted data into a pandas DataFrame for clear analysis.
-   **Automated Reporting**: Generates a summary report that includes:
    -   Total and per capita consumption figures.
    -   A comparison of India's usage against the WHO AWaRe framework targets.
    -   Identification of the most consumed antibiotic molecules.
    -   Key insights into the market dynamics driving consumption.
-   **File Output**: Saves the generated analysis report to a text file (`analysis_report.txt`).

## Project Structure
.
├──.gitignore
├── analysis.py
├── main.py
├── parser.py
├── requirements.txt
├── scraper.py
└── README.md
```

-   `main.py`: The main entry point for the application. It orchestrates the scraping, parsing, and analysis process.
-   `scraper.py`: Contains the function to fetch HTML content from URLs.
-   `parser.py`: Contains functions for extracting and structuring data from the raw text.
-   `analysis.py`: Contains the function to generate the final analysis report from the structured data.
-   `requirements.txt`: Lists the necessary Python packages for the project.
-   `README.md`: This documentation file.
-   `.gitignore`: Specifies files and directories to be ignored by Git.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <repository-directory>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the analysis, simply execute the `main.py` script from your terminal:

```bash
python main.py
```

The script will perform the following actions:
1.  Print status updates to the console as it scrapes the articles.
2.  Print the final analysis report to the console.
3.  Save the same report to a file named `analysis_report.txt` in the root directory.

## Data Sources

The analysis is based on data extracted from the following articles:
-   `https://pmc.ncbi.nlm.nih.gov/articles/PMC9511665/`
-   `https://pmc.ncbi.nlm.nih.gov/articles/PMC9596537/`
-   `https://www.cgdev.org/blog/four-key-findings-antibiotic-consumption-india`

## Limitations

-   **Scraping Fragility**: The tool's web scraping functionality depends on the current HTML structure of the source websites. Any redesign of these sites may break the scraper, requiring updates to the parsing logic.
-   **Static Regex**: Data extraction relies on specific regular expression patterns tailored to the text in the source articles. Changes in phrasing or data presentation may cause the parser to miss information.
```
