"""Lesson 04 exercises: consolidation for Week 1."""

documents = [
    {"name": "invoice_001.pdf", "pages": 3, "processed": True, "owner": "alice"},
    {"name": "invoice_002.pdf", "pages": 2, "processed": False, "owner": "bob"},
    {"name": "report_q1.pdf", "pages": 12, "processed": True, "owner": "alice"},
    {"name": "notes.txt", "pages": 1, "processed": False, "owner": "carol"},
    {"name": "draft.docx", "pages": 5, "processed": False, "owner": "bob"},
]


def main() -> None:
    print("Lesson 04: Week 1 consolidation")

    print("\nSection 1: filtering and extraction")
    # TODO:
    # - print the names of all processed documents
    # - print the names of all PDF documents
    # - print the names of documents owned by "bob"

    print("\nSection 2: counting and grouping-style thinking")
    # TODO:
    # - count how many documents each owner has
    # - count how many documents are processed vs not processed
    # - build a set of unique owners

    print("\nSection 3: mappings and summaries")
    # TODO:
    # - build a mapping of document name -> pages
    # - build a mapping of document name -> owner
    # - calculate total pages across all documents
    # - calculate total pages for processed documents only

    print("\nSection 4: refactor pass")
    # TODO:
    # - choose two loop-based solutions
    # - rewrite them using comprehensions if the result is clearer
    # - keep at least one loop if that version reads better


if __name__ == "__main__":
    main()
