def passWrodPdf(name,password):
    from PyPDF2 import PdfFileReader, PdfFileWriter
    try:
        pdf_path =  input(r'enter Your PDF File Path (.pdf) - ')
        out_pdfpath = input(r'Enter Your Output PDF path Location -')
        # pdf_path = r'{}'.format(pdf_path)
        # out_pdfpath = r'{}'.format(out_pdfpath)
        open_pdf = PdfFileReader(pdf_path)
        #creating pdfwriter object
        pdfWriter = PdfFileWriter()
        #now we need to get the pdf pages & add to pdf writer so that we are itteriting through all of the page indexes
        for i in range(open_pdf.numPages):
            page_deatils = open_pdf.getPage(i)
            pdfWriter.add_page(page_deatils)
        #now enscrypt our output pdf
        pdfWriter.encrypt(password)
        dd = out_pdfpath+'\\{}.pdf'.format(name)
        #now write the output on the given loacation
        with open(out_pdfpath+'\\{}.pdf'.format(name),'wb') as filename:
            pdfWriter.write(filename)
            #wb means write byte mode
            print(f'File is Sucessfully Generated!! & Path Location is {out_pdfpath}')
    except Exception as Ex:
        return Ex
passWrodPdf('kunal','B@neswar12345')