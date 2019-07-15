# you will need to type a few things in terminal to create the db
sqlite3 todo.db << EOF
.tables
.quit
EOF
python << EOF
from app import db
db.create_all()
exit()
EOF
sqlite3 users.db << EOF
.tables
.quit
EOF
python << EOF
from app import db
db.create_all()
exit()
EOF
#Then you will be ready to run the app.
