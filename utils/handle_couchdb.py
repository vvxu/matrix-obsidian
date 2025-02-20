import couchdb

class CouchDBManager:
    def __init__(self, server_url, db_name):
        self.couch = couchdb.Server(server_url)
        self.db = self.couch[db_name]

    def add_document(self, data, parent_doc_id):
        # 创建新文档
        new_doc = {
            'data': data,
            'type': 'leaf'
        }
        
        try:
            new_doc_id, new_doc_rev = self.db.save(new_doc)
        except Exception as e:
            print(f"新文档保存失败: {e}")
            return False

        # 获取父文档
        try:
            parent_doc = self.db[parent_doc_id]
        except Exception as e:
            print(f"获取父文档失败: {e}")
            return False

        # 确保父文档有 children 列表
        if 'children' not in parent_doc:
            parent_doc['children'] = []

        # 将新文档的 ID 添加到父文档的 children 列表中
        print(new_doc_id)
        parent_doc['children'].append(new_doc_id)

        # 保存更新后的父文档
        try:
            self.db.save(parent_doc)
            return True
        except Exception as e:
            return False

