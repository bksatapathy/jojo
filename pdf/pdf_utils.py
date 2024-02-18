from pypdf import PdfWriter
import os

from Exceptions.new_exceptions import NotAPDFError


def merge_pdfs(dir_path: str, output_pdf_name_with_path: str, file_names=None) -> str:
    """
    Merges two or more PDF files into single PDF File. If file_names param is empty, it assumes all files.
    :param dir_path: str
        Path where all input PDF lies
    :param file_names: list
        It is a List of PDF Files which will be merged
    :param output_pdf_name_with_path: str
        Output File name along with path
    :return: str
        Final PDF File name with Path
    """
    if file_names is None:
        file_names = []

    os.chdir(dir_path)
    list_of_files_in_curr_dir: list = os.listdir()

    # Basic Checks
    for file in file_names:
        if file not in list_of_files_in_curr_dir or not file.endswith(".pdf"):
            raise NotAPDFError("Check The List of PDF Files.")

    if not file_names:
        for file in list_of_files_in_curr_dir:
            if file.endswith(".pdf"):
                file_names.append(file)

    merger = PdfWriter()

    return ""
