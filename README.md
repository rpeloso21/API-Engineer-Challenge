# Part 1 - Flask File Processor

## Overview
This is a Flask web application that allows users to upload text files containing key-value pairs separated by `^^`. The application processes the file, extracts and flattens the data, and provides a downloadable processed file in a structured format.

## Features
- Upload a text file via a web interface.
- Parse and process the file by extracting key-value pairs.
- Save the processed data into a structured format.
- Download the processed file.

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Flask
- Werkzeug

### Setup
1. Clone this repository:
   ```sh
   git clone https://github.com/rpeloso21/API-Engineer-Challenge.git
   cd API-Engineer-Challenge
   ```
2. Install dependencies:
   ```sh
   pip install flask werkzeug
   ```
3. Run the application:
   ```sh
   python main.py
   ```
4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Usage
1. Open the web interface.
2. Upload a `.txt` file containing key-value pairs separated by `^^`.
3. The server will process the file and generate a structured output.
4. Download the processed file in a structured format.

## File Processing Format
### Input Format Example:
```
name=John^^age=30^^city=New York
name=Alice^^age=25^^city=Los Angeles
```
### Output Format Example:
```
name|age|city
John|30|New York
Alice|25|Los Angeles
```

## Project Structure
```
flask-file-processor/
│── main.py              # Main Flask application
│── templates/
│   └── upload.html     # Upload page
│── uploads/            # Directory for uploaded files
│── processed/          # Directory for processed files
```

## API Endpoints
### `GET /`
- Renders the file upload page.

### `POST /upload`
- Accepts a file upload.
- Processes the file and returns a downloadable processed file.

## Error Handling
- Returns an error if no file is uploaded.
- Returns an error if the file format is incorrect.
- Handles unexpected server errors gracefully.

# Part 2 - Quadrilateral Classification and Area Calculation

## Overview
This Python script analyzes a quadrilateral based on its four given coordinate points. It classifies the shape and calculates its area. Additionally, it provides a visualization of the shape using Matplotlib.

## Features
- **Classifies quadrilaterals**: Identifies if the given points form a square, rectangle, rhombus, parallelogram, trapezoid, kite, or an undefined shape.
- **Calculates area**: Uses the Shapely library to compute the area of the quadrilateral.
- **Graphical representation**: Plots the quadrilateral using Matplotlib.
- **Error handling**: Includes exception handling to catch unexpected errors.

## Requirements
Ensure you have the following dependencies installed:
```sh
pip install matplotlib shapely sympy numpy
```

## Usage
1. Modify the `points` variable in `main.py` to your desired coordinates:
```python
points = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
```
2. Run the script:
```sh
python main.py
```
3. The output will display:
   - The classification of the quadrilateral.
   - The computed area (or `-1` if the shape is invalid).
   - A graphical plot of the quadrilateral.

## Example
### Input:
```python
points = [(0, 0), (3, 4), (7, 3), (4, -2)]
```
### Output:
```
Parallelogram 10.5
```
A plot of the quadrilateral will also be displayed.

## Error Handling
- If the input points do not form a valid quadrilateral, the script will return `"Not a quadrilateral"`.
- If the shape does not match predefined classifications, it returns `"Other"` and sets the area to `-1`.


**Author:** Bobby Peloso  
**GitHub:** https://github.com/rpeloso21

