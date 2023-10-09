## JourniePython

* `python -m venv env`
* `pip install -r requirements.txt`
* `python main.py`

## Notes

O timestamp foi baseado no ano 2001 ????
```sql
select strftime('%s', '2001-01-01');

select z.Z_PK, strftime('%d-%m-%Y', datetime(ZCREATEDATE + 978307200, 'unixepoch')) FROM ZDIARY z;
```

## Reference

* https://stackoverflow.com/questions/36240243/what-timestamp-format-is-this-sqlite-column-using