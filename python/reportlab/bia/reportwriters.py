#!/usr/bin/python

from reportlab.platypus.doctemplate import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib import styles
from reportlab.lib.enums import TA_RIGHT
from reportlab.rl_config import canvas_basefontname as _baseFontName

class ReportWriter():
    def write_report(self, outputobject=None, report_values=[]):
        doc = SimpleDocTemplate(outputobject)
	catalog = []
	poss_styles = styles.getSampleStyleSheet()
	poss_styles.add(styles.ParagraphStyle(name="Myown", fontName=_baseFontName, fontSize=10, leading=12, alignment=TA_RIGHT))
	catalog.append(Paragraph("godparent name", poss_styles.get("Myown")))
	catalog.append(Paragraph("Address line 1", poss_styles.get("Myown")))
	catalog.append(Paragraph("Address line 2", poss_styles.get("Myown")))
	catalog.append(Paragraph("Overview of your payments in **year**", poss_styles.get("Title")))
	print (str(report_values))
	for line in report_values["values"]:
	    print str(line)
	    godparent_name, payment_date, amount, currency, child_name = line
	    catalog.append(Paragraph("{0} {1} {2} {3} {4}".format(godparent_name, payment_date, amount, currency, child_name), poss_styles.get("Normal")))
	catalog.append(Paragraph("This paragraph is written in my own style", poss_styles.get("Myown")))
	doc.build(catalog)

def getDummyData():
    data = {"values": [
	["parentname", "30-12-2013", "15", "euro", "somekid"],
	["parentname", "30-12-2013", "15", "euro", "somekid"],
	["parentname", "30-12-2013", "15", "euro", "somekid"],
	["parentname", "30-12-2013", "15", "euro", "somekid"],
	["parentname", "30-12-2013", "15", "euro", "somekid"],
	["parentname", "30-12-2013", "15", "euro", "somekid"],
	["parentname", "30-12-2013", "15", "euro", "somekid"],
    ]}
    return data

reportw = ReportWriter()
outpdf = "testoutput.pdf"
reportw.write_report(outputobject=outpdf, report_values=getDummyData())
