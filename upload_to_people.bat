SET PYTHONPATH=.
python current_time.py

"C:\Program Files (x86)\WinSCP\WinSCP.exe" klahnakoski@people.mozilla.com /script="upload_to_people.script" /log=upload_to_people.log
type upload_to_people.log
