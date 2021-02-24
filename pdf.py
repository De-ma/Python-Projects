import pdftotext

# Load your PDF
with open("Untitled.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# # If it's password-protected
# with open("secure.pdf", "rb") as f:
#     pdf = pdftotext.PDF(f, "secret")

# How many pages?
print(len(pdf))

# Iterate over all the pages
for page in pdf:
    print(page)
