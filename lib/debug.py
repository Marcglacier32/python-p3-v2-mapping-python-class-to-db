# lib/debug.py
from __init__ import CONN, CURSOR
from department import Department
import ipdb

Department.drop_table()
Department.create_table()

payroll = Department.create("Payroll", "Building A, 5th Floor")
print(payroll)

hr = Department.create("Human Resources", "Building C, East Wing")
print(hr)

# Update HR department
hr.name = "HR"
hr.location = "Building F, 10th Floor"
hr.update()
print(hr)

# Optional: delete payroll department
payroll.delete()

ipdb.set_trace()
