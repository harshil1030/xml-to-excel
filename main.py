from flask import Flask, render_template, request
import xml.etree.ElementTree as ET
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Parse XML data
            xml_data = file.read()
            root = ET.fromstring(xml_data)
            
            # Extract data from XML and create a DataFrame
            data = []
            for child in root:
                # Assuming XML structure, modify accordingly
                row = {}
                row['name'] = child.find('name').text
                row['age'] = child.find('age').text
                data.append(row)
                
            df = pd.DataFrame(data)
            
            # Convert DataFrame to Excel
            excel_file = 'output.xlsx'
            df.to_excel(excel_file, index=False)
            
            return f'<a href="{excel_file}">Download Excel File</a>'
    
    return render_template('upload.html')

if __name__ == '__main__':
    app.run()
