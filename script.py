import xml.etree.ElementTree as ET
import sys

def generate_html_report(jtl_file, output_html):
    # Parse the JMeter results file
    tree = ET.parse(jtl_file)
    root = tree.getroot()

    # Open the HTML file for writing
    with open(output_html, 'w') as f:
        f.write("<html><head><title>JMeter Results Tree</title>")
        f.write("<style>table {width: 100%; border-collapse: collapse;} th, td {border: 1px solid black; padding: 8px; text-align: left;} th {background-color: #f2f2f2;}</style>")
        f.write("</head><body>")
        f.write("<h1>JMeter Results Tree</h1>")
        f.write("<table><tr><th>Time Stamp</th><th>Label</th><th>Response Code</th><th>Response Message</th><th>Elapsed Time</th><th>Success</th></tr>")

        # Iterate over each sample result
        for sample in root.findall('httpSample'):
            timestamp = sample.get('ts', 'N/A')
            label = sample.get('lb', 'N/A')
            response_code = sample.get('rc', 'N/A')
            response_message = sample.get('rm', 'N/A')
            elapsed_time = sample.get('t', 'N/A')
            success = sample.get('s', 'N/A')

            # Write each result into the table
            f.write(f"<tr><td>{timestamp}</td><td>{label}</td><td>{response_code}</td><td>{response_message}</td><td>{elapsed_time}</td><td>{success}</td></tr>")

        f.write("</table></body></html>")

# Check for correct number of arguments
if len(sys.argv) != 3:
    print("Usage: python generate_jmeter_report.py <input_jtl_file> <output_html_file>")
    sys.exit(1)

# Get file paths from command-line arguments
jtl_file = sys.argv[1]
output_html = sys.argv[2]

# Generate the HTML report
generate_html_report(jtl_file, output_html)
print(f"Report generated: {output_html}")

