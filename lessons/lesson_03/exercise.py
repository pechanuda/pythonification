"""Lesson 03 exercises: comprehensions and transformation patterns."""

files = [
    "invoice_001.pdf",
    "invoice_002.pdf",
    "notes.txt",
    "report.pdf",
    "draft.docx",
    "todo.txt",
]

documents = [
    {"name": "invoice_001.pdf", "pages": 3, "processed": True},
    {"name": "notes.txt", "pages": 1, "processed": False},
    {"name": "report.pdf", "pages": 12, "processed": True},
    {"name": "draft.docx", "pages": 5, "processed": False},
]


def main() -> None:
    print("Lesson 03: comprehensions and transformation patterns")

    print("\nSection 1: lists")
    # TODO:
    # - build a list of PDF filenames
    # - build a list of filenames without extensions
    # - build a list of processed document names

    print("\nSection 2: sets")
    # TODO:
    # - build a set of unique file extensions
    # - build a set of page counts greater than 2

    print("\nSection 3: dicts")
    # TODO:
    # - build a mapping of filename -> extension
    # - build a mapping of document name -> processed status
    # - build a mapping of document name -> page count for documents with more than 2 pages

    print("\nSection 4: judgment")
    # TODO:
    # - solve one small task twice:
    #   once with a loop
    #   once with a comprehension
    # - add a short comment saying which version you think is clearer


if __name__ == "__main__":
    main()
