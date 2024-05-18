# BeyondChatsAssigment
# Citation Finder

This project fetches data from a paginated API, identifies sources for each response, and returns the citations.

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/Bhawesh6417/citation-finder.git
    cd citation-finder
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the script to fetch data and generate citations:
    ```sh
    python main.py
    ```

5. (Optional) To run the Flask app:
    ```sh
    python app.py
    ```

## Usage

- The script will generate a `citations.json` file with the citations.
- To view the results in a web interface, run the Flask app and open `http://127.0.0.1:5000` in your browser.
