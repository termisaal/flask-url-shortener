import sqlite3
from typing import Optional

import config as cf
from utils import make_code


class Database:
    def __init__(self):
        self.setup()

    @staticmethod
    def setup():
        with sqlite3.connect(cf.Database.location) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS URLs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    code TEXT NOT NULL UNIQUE,
                    url TEXT NOT NULL UNIQUE,
                    date TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL,
                    uses INTEGER DEFAULT 0 NOT NULL 
                )
            ''')

    @staticmethod
    def _get_urls_count() -> int:
        with sqlite3.connect(cf.Database.location) as conn:
            result = conn.execute('''
                SELECT COUNT(*) 
                FROM URLs
            ''').fetchone()
        return result[0]

    @staticmethod
    def _get_code_by_url(url: str) -> Optional[str]:
        with sqlite3.connect(cf.Database.location) as conn:
            result = conn.execute(f'''
                SELECT code
                FROM URLs
                WHERE url = '{url}'
            ''').fetchone()
        return result[0] if result else None

    def add_url(self, url: str) -> str:
        with sqlite3.connect(cf.Database.location) as conn:
            if code := self._get_code_by_url(url):
                pass
            else:
                code = make_code(self._get_urls_count() + 1)
                conn.execute(f'''
                    INSERT INTO URLs (code, url) 
                    VALUES ('{code}', '{url}')
                ''')
        return code

    @staticmethod
    def get_url_by_code(code: str) -> Optional[str]:
        with sqlite3.connect(cf.Database.location) as conn:
            result = conn.execute(f'''
                SELECT url, uses, date
                FROM URLs
                WHERE code = '{code}'
            ''').fetchone()
        if result:
            conn.execute(f'''
                UPDATE URLs
                SET uses = uses + 1
                WHERE code = '{code}'
            ''')
            return result
        else:
            return None
