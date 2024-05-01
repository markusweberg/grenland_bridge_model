import os

jobname = "grenland_bridge_2"

os.system("abaqus job=" + jobname + " interactive")
os.system("abaqus viewer database=" + jobname)