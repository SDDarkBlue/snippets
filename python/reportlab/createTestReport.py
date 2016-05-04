#!/usr/bin/python

from reportlab.platypus.doctemplate import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle
from reportlab.lib import styles, colors

doc = SimpleDocTemplate("myreport.pdf")
poss_styles = styles.getSampleStyleSheet()
title = Paragraph("This is a test report", poss_styles.get("Title"))
header2 = Paragraph("This is heading 2", poss_styles.get("Heading2"))
some_text = Paragraph("This is a paragraph. It contains quite some text to make sure it looks like a paragraph. Don't read all of it. You'll learn nothing. It's wasted time in fact. By the way, what's the difference between 'wasted' and 'waisted'? Is there any? Ok, this should be enough text to give you an idea of what a paragraph looks like. Oh, and by the way, reportlab is quite awesome. So far, I'm loving it.", poss_styles.get("Normal"))
table_header = Paragraph("This is a table", poss_styles.get("Heading2"))
table = Table([["cell 11", "cell 12"], ["cell 3", "cell 4"]], [250, 250]) 
tblStyle = TableStyle(
    [
        ('GRID', (0,0), (-1, -1), 1, colors.black),
    ]
)
table.setStyle(tblStyle)
catalog = []
catalog.append(title)
catalog.append(header2)
catalog.append(some_text)
catalog.append(table_header)
catalog.append(table)
doc.build(catalog)
