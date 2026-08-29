#!/usr/bin/env python3
from pathlib import Path
import argparse,json,importlib.util
ROOT=Path(__file__).resolve().parents[1]
def load(name):
 spec=importlib.util.spec_from_file_location(name,ROOT/'scripts'/f'{name}.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def main():
 p=argparse.ArgumentParser();p.add_argument('input_json');p.add_argument('--format',choices=['markdown','confluence','both'],default='markdown');p.add_argument('--output-dir',default='.');a=p.parse_args();data=json.loads(Path(a.input_json).read_text(encoding='utf-8'));od=Path(a.output_dir);od.mkdir(parents=True,exist_ok=True)
 if a.format in ('markdown','both'):
  m=load('render_report_markdown');out=od/f"sakerhetsgranskning-{m.clean_name(data['metadata'].get('system_name'))}.md";out.write_text(m.render(data),encoding='utf-8');print(out)
 if a.format in ('confluence','both'):
  m=load('render_report_confluence');out=od/f"sakerhetsgranskning-{m.clean_name(data['metadata'].get('system_name'))}.confluence.txt";out.write_text(m.render(data),encoding='utf-8');print(out)
if __name__=='__main__':main()
