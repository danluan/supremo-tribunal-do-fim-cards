import csv
from jinja2 import Environment, FileSystemLoader
import imgkit

env = Environment(loader=FileSystemLoader('templates'))

def render_cards(filename, output_dir):

    template = env.get_template(f'{filename}.html')
    
    with open(f'content/{filename}.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        records = list(reader)

    for i, record in enumerate(records):
        title = record['title'].replace(' ', '_').lower()
        print("printing record: ", record['title'])
        rendered_html = template.render(title=record['title'], description=record['description'])
        html_file = f"tmp/temp.html"
        print("writing to file: ", html_file)
        with open(html_file, "w", encoding="utf-8") as fhtml:
            fhtml.write(rendered_html)
        
        img_file = f"out/{output_dir}/card_{title}.png"
        
        kitoptions = {
            "enable-local-file-access": None,
            "width": 750,
            "height": 1095,
            "quality": 75
            
        }
        
        imgkit.from_file(html_file, img_file, options=kitoptions)


def main():
    render_cards('100', '100-reais')
    render_cards('5', '5-reais')
    render_cards('mandato', 'mandatos')
    
if __name__ == "__main__":
    main()