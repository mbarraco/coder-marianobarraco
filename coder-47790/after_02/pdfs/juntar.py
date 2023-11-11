from pypdf import PdfMerger


pairs = [
    ("dir_a/a.pdf", "dir_b/a.pdf"),
    ("dir_a/c.pdf", "dir_b/c.pdf"),
]


for i, pareja in enumerate(pairs):
    archivo_a, archivo_b = pareja
    print(archivo_a, archivo_b)
    merger = PdfMerger()
    merger.append(archivo_a)
    merger.append(archivo_b)
    merger.write(f"archivo_{i}.pdf")
    merger.close()


# merger = PdfMerger()
# merger.append("a.pdf")
# merger.append("c.pdf")
# merger.append("d.pdf")
# merger.append("e.pdf")
# merger.write("result.pdf")
# merger.close()