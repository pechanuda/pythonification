"""Lesson 02 exercises: slicing, unpacking, membership, and truthiness."""

filenames = [
    "invoice_001.pdf",
    "invoice_002.pdf",
    "notes.txt",
    "archive.tar.gz",
    "report_final.docx",
]

queue = ["parse", "validate", "transform", "write"]

pairs = [
    ("alice", "admin"),
    ("bob", "editor"),
    ("carol", "viewer"),
]


def split_name_and_extension(filename: str) -> tuple[str, str]:
    """Return the base filename and extension for a simple filename."""
    # TODO: implement for names like "notes.txt"
    return "", ""


def main() -> None:
    print("Lesson 02: slicing, unpacking, membership, and truthiness")

    print("\nSection 1: slicing")
    # TODO:
    # - print the first two filenames
    # - print the last two filenames
    # - print the last three characters of each filename

    print("\nSection 2: unpacking")
    # TODO:
    # - unpack the first two queue items into named variables and print them
    # - unpack one filename into base name and extension using split_name_and_extension
    # - loop through pairs and unpack each tuple into user and role

    print("\nSection 3: membership and truthiness")
    # TODO:
    # - print filenames that contain "invoice"
    # - print whether "transform" is in queue
    # - print a message if queue is not empty
    # - print a message if an empty list has no items


if __name__ == "__main__":
    main()
