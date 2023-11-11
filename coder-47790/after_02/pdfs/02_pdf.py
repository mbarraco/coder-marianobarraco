
# # renombar archivo
# import os

# os.rename("b.pdf", "c.pdf")


from pypdf import PdfMerger


merger = PdfMerger()

merger.append("a.pdf")
merger.append("c.pdf")
merger.append("d.pdf")
merger.append("e.pdf")
merger.write("result.pdf")
merger.close()