import sqlite3

DATABASE_PATH = 'data.db'

class Data:
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.JOB_FIELD_ORDER = ('id', 'title', 'company', 'description', 'salary')

    def add_job(self, **job):
        order = self.JOB_FIELD_ORDER[1:] # Exclude 'id' since it will be generated automatically.
        vals = []
        for next_field in order:
            vals.append(job[next_field])
        self.cursor.execute(
            f'INSERT INTO jobs {order} VALUES(?, ?, ?, ?)',
            tuple(vals)
        )

    def get_job(self, job_id):
        self.cursor.execute(f'SELECT * FROM jobs WHERE id = {job_id}')
        tuple_form = self.cursor.fetchone()
        return dict(zip(self.JOB_FIELD_ORDER, tuple_form))

    def filter(self, **filters):
        sql_command = 'SELECT * FROM jobs WHERE '
        last_field_name = list(filters.keys())[-1]
        for field_name, val in filters.items():
            sql_command += f'{field_name} LIKE \'%{val}%\''
            if field_name != last_field_name:
                sql_command += ' AND '
        self.cursor.execute(sql_command)
        res_list = self.cursor.fetchall()
        for i in range(len(res_list)):
            res_list[i] = dict(zip(self.JOB_FIELD_ORDER, res_list[i]))
        return res_list

    def commit(self):
        self.conn.commit()

    def __del__(self):
        self.conn.commit()
        self.conn.close()
