from document import Document

# Creating a document containing a list of two lists
ORIGINAL_DOCUMENT = Document("Original", [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
print(ORIGINAL_DOCUMENT)
print()

DOCUMENT_COPY_1 = ORIGINAL_DOCUMENT.clone(mode=1)  # shallow copy
DOCUMENT_COPY_1.name = "Copy 1"
DOCUMENT_COPY_1.list[1][4] = 100
print(DOCUMENT_COPY_1)
print(ORIGINAL_DOCUMENT)
print()

DOCUMENT_COPY_2 = ORIGINAL_DOCUMENT.clone(2)  # 2 level shallow copy
DOCUMENT_COPY_2.name = "Copy 2"
DOCUMENT_COPY_2.list[0] = [11, 10, 11, 12]
print(DOCUMENT_COPY_2)
print(ORIGINAL_DOCUMENT)
print()

DOCUMENT_COPY_3 = ORIGINAL_DOCUMENT.clone(2)  # 2 level shallow copy
DOCUMENT_COPY_3.name = "Copy 3"
DOCUMENT_COPY_3.list[1][0] = "1234"
print(DOCUMENT_COPY_3)
print(ORIGINAL_DOCUMENT)
print()

DOCUMENT_COPY_4 = ORIGINAL_DOCUMENT.clone(3)  # deep copy (recursive)
DOCUMENT_COPY_4.name = "Copy 4"
DOCUMENT_COPY_4.list[1][0] = "5678"
print(DOCUMENT_COPY_4)
print(ORIGINAL_DOCUMENT)
print()
