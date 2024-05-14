def read_txt_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_html_file(output_folder, file_name, content):
    with open(f"{output_folder}/{file_name}.html", "w", encoding="utf-8") as file:
        file.write(f"""
        <html>
        <head>
            <title>{file_name}</title>
        </head>
        <body>
            <pre>{content}</pre>
        </body>
        </html>
        """)

def txt_to_html(input_file, output_folder):
    file_name = input_file.split('/')[-1].split('.')[0]  # Get the file name for the HTML title
    text_content = read_txt_file(input_file)
    write_html_file(output_folder, file_name, text_content)

if __name__ == "__main__":
    input_file_path = "text.txt"  # Update with the path to your text file
    output_folder = "output"  # Target folder for the HTML output file
    txt_to_html(input_file_path, output_folder)