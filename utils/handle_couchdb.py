import couchdb
import uuid
import time
from datetime import datetime

class CouchDBManager:
    def __init__(self, server_url, db_name):
        self.couch = couchdb.Server(server_url)
        self.db = self.couch[db_name]

    def add_document(self, data, parent_doc_id):
        try:
            new_leaf_id = f"a:{uuid.uuid4().hex[:12]}"  # 生成 12 位唯一 ID
            # 创建 leaf 数据
            new_leaf_doc = {
                "_id": new_leaf_id,
                "data": data,
                "type": "leaf"
            }
            # 尝试保存新 leaf
            self.db[new_leaf_id] = new_leaf_doc

            # 更新 "待办事项.md" 的 children
            if parent_doc_id in self.db:
                todo_doc = self.db[parent_doc_id]
                if "children" not in todo_doc:
                    todo_doc["children"] = []  # 确保 children 存在
                todo_doc["children"].append(new_leaf_id)  # 添加新的 leaf ID
                todo_doc["mtime"] = int(time.time() * 1000)  # 更新修改时间（毫秒级时间戳）
                self.db[parent_doc_id] = todo_doc  # 保存更新

            return True  # 成功写入返回 True
        except couchdb.http.ResourceConflict:
            print("❌ 写入失败: 资源冲突 (可能是 _rev 过期)")
        except Exception as e:
            print(f"❌ 写入失败: {e}")

        return False  # 发生异常返回 False