from os import getenv
from pathlib import Path
from typing import Dict, Iterator, Tuple

from fastapi import FastAPI, File, UploadFile

from expylliarmus.analyze import analyze_book_spells

# reads from EXP_BOOKS_FOLDER the filepath where books are written or read, defaults to local/books otherwise
EXP_BOOKS_FOLDER = getenv('EXP_BOOKS_FOLDER')
EXP_BOOKS_PATH = (Path(EXP_BOOKS_FOLDER) if EXP_BOOKS_FOLDER else Path(__file__).parent.parent.parent / 'local' / 'books').resolve()

print(f"Reads and writes books in '{EXP_BOOKS_PATH}' folder")

# defines the web application and its routes
expylliarmus = FastAPI()

@expylliarmus.post('/books/upload')
def upload_book(
    file: UploadFile = File(..., description='The text content of a book')
):
    if file.filename.endswith('.txt'):
        with open(EXP_BOOKS_PATH / file.filename, 'bw') as book_file:
            book_file.writelines(file.file.readlines())
        return {'msg': f'Wrote {file.filename} ({file.content_type})'}
    else:
        raise ValueError(f"Book content must be posted in a .txt file, got '{file.filename}'")

@expylliarmus.get('/books')
def list_books():
    book_paths: List[Path] = sorted(EXP_BOOKS_PATH.rglob('*.txt'))
    return {
        'books': [book_path.name for book_path in book_paths]
    }

@expylliarmus.post('/books/{book_id}/analyze-spells')
def analyze_book(book_id: str):
    spells_by_line = analyze_book_spells(book_id, EXP_BOOKS_PATH)
    return {'spells_by_line': spells_by_line}
