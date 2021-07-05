import sqlite3
from typing import Optional

import config as cf
from utils import make_code


class Database:
    def __init__(self):
        self._conn = sqlite3.connect(cf.Database.location)
        self.setup()

    def __del__(self):
        self._conn.close()

    def setup(self):
        with self._conn:
            self._conn.execute('''
                CREATE TABLE IF NOT EXISTS URLs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    code TEXT NOT NULL UNIQUE,
                    url TEXT NOT NULL UNIQUE,
                    date TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL,
                    uses INTEGER DEFAULT 0 NOT NULL 
                )
            ''')

    def _get_urls_count(self) -> int:
        with self._conn:
            result = self._conn.execute('''
                SELECT COUNT(*) 
                FROM URLs
            ''').fetchone()
        return result[0]

    def _get_code_by_url(self, url: str) -> Optional[str]:
        with self._conn:
            result = self._conn.execute(f'''
                SELECT code
                FROM URLs
                WHERE url = '{url}'
            ''').fetchone()
        return result[0] if result else None

    def add_url(self, url: str) -> str:
        with self._conn:
            if code := self._get_code_by_url(url):
                pass
            else:
                code = make_code(self._get_urls_count() + 1)
                with self._conn:
                    self._conn.execute(f'''
                        INSERT INTO URLs (code, url) 
                        VALUES ('{code}', '{url}')
                    ''')
        return code

    def get_url_by_code(self, code: str) -> Optional[str]:
        with self._conn:
            result = self._conn.execute(f'''
                SELECT url, uses, date
                FROM URLs
                WHERE code = '{code}'
            ''').fetchone()
        if result:
            with self._conn:
                self._conn.execute(f'''
                    UPDATE URLs
                    SET uses = uses + 1
                    WHERE code = '{code}'
                ''')
            return result
        else:
            return None
