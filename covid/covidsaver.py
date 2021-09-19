from covid.api.public import save_jpus, save_korea
from covid.database.db_init import get_db
from threading import Timer

class CovidController:
    def __init__(
        self,
        update_time: float,
    ) -> None:
        self.update_time = update_time
        self.timer = None
        self.db = get_db()
        # self.save_pastdata()

    def save_pastdata(self) -> None:
        for i in range(7):
            save_korea(self.db, i)
            save_jpus(self.db, i)
        
    def save_data(self) -> None:
        save_korea(self.db)
        save_jpus(self.db)
        self.timer = Timer(self.update_time, self.save_data)
        self.timer.start()
    
    def start(self) -> None:
        self.save_data()

    def stop(self) -> None:
        self.timer.cancel()
        self.timer = None
