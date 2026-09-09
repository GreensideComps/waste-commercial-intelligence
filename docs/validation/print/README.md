# Print-ready versions

| File | Pages | Use |
|---|---|---|
| `manager-pack.pdf` | **7** — cover, then **one card per page**, then the closing note | Print single-sided. Hand over one card at a time, face down. |
| `interview-sheet.pdf` | 2 | Interviewer copy. **Do not show the participant** — page 2 identifies Mell Square as the control. |
| `*.html` | — | Open in a browser and Ctrl/Cmd+P if you'd rather adjust before printing |
| `build-print.py` | — | Regenerates both from the Markdown sources |

Regenerate after editing the Markdown:

```
python3 docs/validation/print/build-print.py
/opt/pw-browsers/chromium-*/chrome-linux/chrome --headless --no-sandbox \
  --no-pdf-header-footer --print-to-pdf=docs/validation/print/manager-pack.pdf \
  file://$PWD/docs/validation/print/manager-pack.html
```
