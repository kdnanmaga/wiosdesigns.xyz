import mistune
import yaml
import os
from jinja2 import Template

mdparser = mistune.Markdown()
page_folder = 'markdown/'

template = None
with open('template.html') as f:
  template = Template(f.read())
  f.close()
  

for page_file_name in os.listdir(page_folder):
  print(page_file_name)
  with open(page_folder+page_file_name) as page_file:
    contents = page_file.read().split('---')
    page = yaml.safe_load(contents[1])
    page['main_html'] = mdparser(contents[2])
    page['file'] = page_file_name[:-3]+'.html'
    page_content = template.render(title=page['title'],description=page['description'],image=page['image'],keywords=page['keywords'],main_html=page['main_html'],filename=page['file'])
    with open(page['file'],'w') as w:
      w.write(page_content)
      w.close()
    
