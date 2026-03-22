"""Lesson 01 exercises: core collections and Pythonic transformations.

Suggested flow:
1. Solve each section with normal loops first.
2. Rewrite at least part of each section using comprehensions.
3. Keep the code simple. No classes for this lesson.
"""

files = [
    "invoice_001.pdf",
    "invoice_002.pdf",
    "notes.txt",
    "report_final.docx",
    "image.png",
    "invoice_003.pdf",
    "todo.txt",
]

words = ["doc", "scan", "doc", "report", "scan", "pdf", "report", "report"]

documents = [
    {"name": "invoice_001.pdf", "pages": 3, "processed": True},
    {"name": "notes.txt", "pages": 1, "processed": False},
    {"name": "report.pdf", "pages": 12, "processed": True},
    {"name": "draft.docx", "pages": 5, "processed": False},
]


def summarize_extensions(files: list[str]) -> dict[str, int]:
    """Return counts by file extension."""
    # TODO: implement this during the lesson.
    return {}


def main() -> None:
    print("Lesson 01: core collections")

    print("\nSection 1: filenames")
    # TODO:
    # - print all PDF files
    # - print filenames without extension
    # - print unique extensions
    # - print filename -> extension mapping

    print("\nSection 2: word counting")
    # TODO:
    # - build a set of unique words
    # - build a dictionary of word counts
    # - call summarize_extensions(files)

    print("\nSection 3: document records")
    # TODO:
    # - names of processed documents
    # - names of documents with more than 2 pages
    # - total number of pages
    # - document name -> page count mapping

    print("\nSandbox part")
    print(files[1])
    print(files[0])
    print(files[-2])

    test_dict = { "a": "ej", "b": "by", "c": "sy"}
    print(test_dict["b"])
    test_tuple = ("age","34")
    print(test_tuple)
    print(test_tuple[-1])


if __name__ == "__main__":
    main()
