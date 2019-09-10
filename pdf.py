
#install fpdf using pip
from fpdf import FPDF
#start your pdf file by calling FPDF()
pdf = FPDF()
#ADD a page to your pdf
pdf.add_page()
#set font for your pdf
pdf.set_font('Arial','B',24)
#write anything in a perticular postion(40,10)cell and then the matter
pdf.cell(40,10,'hello ashutosh its working')
#save your pdf file
pdf.output('fpdfdemo.pdf','F')
