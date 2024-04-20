import re

from PyPDF2 import PdfReader


def scrappe_data(filename):
    reader = PdfReader(filename)
    page = reader.pages[0]
    text = page.extract_text()
    lines = text.split("\n")

    for line in lines:
        match = re.search(
            r"([A-ZáéíóúÁÉÍÓÚüÜ]+)\s([\w\s]+(?:#\d+)?)\s+([\d.]+)\s+\$\s+([\d.]+)\s+\$\s+([\d.]+)", line)
        if match:
            article_name = match.group(1).strip()
            model = match.group(2).strip()
            quantity = match.group(3)
            min_price = match.group(4)
            max_price = match.group(5)

            print(
                f"{article_name}  |  {model}  |  {quantity}  |  {min_price}   |  {max_price}")


if __name__ == "__main__":
    scrappe_data("precios.pdf")
