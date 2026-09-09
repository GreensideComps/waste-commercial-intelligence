import markdown, re, pathlib, html
CSS = """
@page { size: A4; margin: 10mm 12mm 9mm 12mm; }
*{box-sizing:border-box}
body{font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;font-size:8.5pt;
     line-height:1.28;color:#14181d;margin:0}
h1{font-size:15pt;margin:0 0 1mm;letter-spacing:-.2px}
h2{font-size:11.6pt;margin:0 0 3mm;font-weight:600;color:#2c3038}
h3{font-size:8.2pt;margin:3.4mm 0 1.2mm;text-transform:uppercase;letter-spacing:.85px;
   color:#6a3d00;border-bottom:1px solid #e0d5c4;padding-bottom:1mm}
p{margin:0 0 1.9mm}
table{border-collapse:collapse;width:100%;margin:0 0 2.2mm;font-size:8pt}
th,td{border:1px solid #ccd2da;padding:1mm 1.6mm;text-align:left;vertical-align:top}
th{background:#eef1f5;font-weight:600}
blockquote{margin:1.8mm 0 2.2mm;padding:1.8mm 3mm;background:#f6f7f9;
           border-left:2.6px solid #8a9099;font-size:8.6pt}
blockquote p{margin:0 0 1.2mm}blockquote p:last-child{margin:0}
ul,ol{margin:0 0 1.9mm;padding-left:4.4mm}
li{margin-bottom:.8mm}
a{color:#14181d;text-decoration:none;border-bottom:.5px dotted #99a;
  word-break:break-all;font-size:7.8pt}
hr{display:none}
strong{font-weight:650}
.card{page-break-after:always;break-after:page}
.card:last-of-type{page-break-after:auto;break-after:auto}
.foot{position:fixed;bottom:3mm;left:0;right:0;font-size:7pt;color:#8d949d;text-align:center}
"""
def build(src,out,title,footer,split,merge_first=0):
    md=pathlib.Path(src).read_text()
    if split:
        parts=[p for p in re.split(r'\n-{3,}\n(?:-{3,}\n)?',md) if p.strip()]
        if merge_first: parts=["\n\n".join(parts[:merge_first])]+parts[merge_first:]
        body="".join(f'<section class="card">{markdown.markdown(p,extensions=["tables","sane_lists","nl2br"])}</section>' for p in parts)
    else:
        body=f'<section>{markdown.markdown(md,extensions=["tables","sane_lists","nl2br"])}</section>'
    pathlib.Path(out).write_text(
        f'<!doctype html><html><head><meta charset="utf-8"><title>{html.escape(title)}</title>'
        f'<style>{CSS}</style></head><body>{body}<div class="foot">{html.escape(footer)}</div></body></html>')
build('docs/validation/manager-pack.md','docs/validation/print/manager-pack.html',
 'NRS Opportunity Discovery Test — Evidence Pack',
 'NRS opportunity discovery test · prepared and verified 9 September 2026',True,merge_first=2)
build('docs/validation/manager-interview-sheet.md','docs/validation/print/interview-sheet.html',
 'Interview Sheet','Interviewer copy — not for circulation',False)
print("html rebuilt")
