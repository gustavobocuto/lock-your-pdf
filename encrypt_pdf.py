from PyPDF2 import PdfReader, PdfWriter

# Ruta del archivo PDF original
input_pdf_path = input("Digite o caminho do PDF original: ")
output_pdf_path = input("Digite o caminho para salvar o PDF criptografado: ")

# Crear un lector y un escritor de PDF
pdf_reader = PdfReader(input_pdf_path)
pdf_writer = PdfWriter()

# Copiar todas las páginas del PDF original al nuevo PDF
for page_num in range(len(pdf_reader.pages)):
    pdf_writer.add_page(pdf_reader.pages[page_num])

# Establecer una contraseña para el nuevo PDF
password = input("Digite a senha para o arquivo PDF: ")
pdf_writer.encrypt(user_password=password, owner_password=None, use_128bit=True)

# Guardar el PDF cifrado
with open(output_pdf_path, 'wb') as output_pdf:
    pdf_writer.write(output_pdf)

print(f"PDF cifrado y guardado como '{output_pdf_path}'.")

