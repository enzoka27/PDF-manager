import os

def list_pdfs(path):
    n = 1
    for i in os.listdir(path):
        print(f'\033[31m{n}-{i.replace(".pdf", "")}\033[m')  # or i[:-4] to remove the .pdf
        n += 1  # add numbers to the PDFs

def open_pdf(path, pdf_index):
    try:
        if 1 <= pdf_index <= len(os.listdir(path)):
            os.startfile(f'{path}\{os.listdir(path)[pdf_index-1]}')
        else:
            print('PDF not found! Try a valid number.')
    except ValueError:
        print('Type a valid number.')  # Try and Except to avoid errors from the user

def main():
    path = 'C:\\ExamplePath'  # using double bars to avoid syntax error
    list_pdfs(path)

    while True:
        try:
            pdf_index = int(input('Which PDF do you want to open? '))
            open_pdf(path, pdf_index)
        except ValueError:
            print('Type a valid number!')

if __name__ == "__main__":  # to avoid running the code when importing the module
    main()