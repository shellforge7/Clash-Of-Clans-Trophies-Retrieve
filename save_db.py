from database import Session
from models import Trophy

def save_trophies_logs(trophies):
     session = Session()
     try:
          trophy_log = Trophy(trophies=trophies)
          session.add(trophy_log)
          session.commit()
          print(f"Trophy log saved: {trophy_log.trophies}")

     except Exception as e:
          print(f"An error occurred while saving trophy logs: {e}")
          session.rollback()

     finally:
          session.close()