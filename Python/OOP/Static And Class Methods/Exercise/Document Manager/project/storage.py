from sre_parse import CATEGORIES
from project.category import Category
from project.topic import Topic
from project.document import Document

class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        for k in range(0, len(self.categories)):
            if self.categories[k].id == category.id:
                return -1
        
        self.categories.append(category)

    def add_topic(self, topic: Topic):
        for k in range(0, len(self.topics)):
            if self.topics[k].id == topic.id:
                return -1

        self.topics.append(topic)

    def add_document(self, document: Document):
        for k in range(0, len(self.documents)):
            if self.documents[k].id == document.id:
                return -1

        self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        for k in range(0, len(self.categories)):
            if category_id == self.categories[k].id:
                self.categories[k].name = new_name

    def edit_topic(self, topic_id: int, new_name: str, new_storage_folder: str):
        for k in range(0, len(self.topics)):
            if topic_id == self.topics[k].id:
                self.topics[k].topic = new_name
                self.topics[k].storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        for k in range(0, len(self.documents)):
            if document_id == self.documents[k].id:
                self.documents[k].file_name = new_file_name
    
    def delete_category(self, category_id):
        for k in range(0, len(self.categories)):
            if self.categories[k].id == category_id:
                del self.categories[k]
                break
    
    def delete_topic(self, topic_id):
        for k in range(0, len(self.topics)):
            if self.topics[k].id == topic_id:
                del self.topics[k]
                break

    def delete_document(self, document_id):
        for k in range(0, len(self.documents)):
            if self.documents[k].id == document_id:
                del self.documents[k]
                break

    def get_document(self, document_id):
        for k in range(0, len(self.documents)):
            if self.documents[k].id == document_id:
                return self.documents[k]

    def __repr__(self):
        output = ""

        for k in range(0, len(self.documents)):
            output += f"{self.documents[k].__repr__()}"
            if k != len(self.documents) - 1:
                output += "\n"

        return output