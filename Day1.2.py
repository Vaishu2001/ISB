#Playing with the pdfs 
from PyPDF2 import PdfFileWriter,PdfFileReader
'''#merge pdfs together
#open your first pdf
#open your sec pdf
#for each page ,copy it to third pdf
#open your third pdf
write_obj=PdfFileWriter()
pdf_list=["C:\\Users\\ASUS\\Desktop\\DBMS1.pdf","C:\\Users\\ASUS\\Desktop\\DBMS2.pdf"]
for i in pdf_list:
	red_obj=PdfFileReader(i)
	pages=red_obj.getNumPages()
	#print(pages)
	for j in range(pages):
		p=red_obj.getPage(j)
		write_obj.addPage(p)
#encrypt the write_obj
write_obj.encrypt('vaishu123','isb2020',True)
#in order convert our write_obj into pdf file
pdf_file=open("C:\\Users\\ASUS\\Desktop\\DBMS1+DBMS2.pdf",'wb')
write_obj.write(pdf_file)'''
#read the pdf
#create new pdf
#read the watermark
#for each page in pdf,merge the watermark with new pdf
pdf=PdfFileReader("C:\\Users\\ASUS\\Desktop\\DBMS1.pdf")
watermark=PdfFileReader("C:\\Users\\ASUS\\Desktop\\certificates\\accenture.pdf ")
page_w=watermark.getPage(0)
new_pdf=PdfFileWriter()
pages=pdf.getNumPages()
for i in range(pages):
	page=pdf.getPage(i)
	page.mergePage(page_w)
	new_pdf.addPage(page)
pdf_f1=open("C:\\Users\\ASUS\\Desktop\\pdf+watermark.pdf",'wb')
new_pdf.write(pdf_f1)
pdf_f1.close()





