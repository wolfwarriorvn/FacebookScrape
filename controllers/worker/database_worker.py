from PySide6.QtCore import QRunnable
from PySide6.QtCore import QObject
from PySide6.QtCore import Signal, Slot
from model.db_model import DatabaseModel
import uuid
class OpSignal(QObject):
    result = Signal(object, object)

class DatabaseWorker(QRunnable):
    def __init__(self, operation, request):
        super().__init__()
        self.operation = operation
        self.request = request
        self.signal = OpSignal()
        self.connectionName = str(uuid.uuid4())  # Unique connection name

    def run(self):
        try:
            self.db_model = DatabaseModel(self.connectionName)

            operation_method = getattr(self.db_model, self.operation, None)
            if not operation_method:
                raise ValueError(f"Unhandled operation type: {self.operation}")
            
            result = operation_method(self.request)
            self.signal.result.emit(result, None)

        except Exception as e:
            self.signal.result.emit(None, str(e))

        finally:
            self.db_model.close_database()
