"""
run unreal bootstrapped with this package's scripts
"""

import os
import subprocess

print(os.path.abspath(__file__))

UE_CONFIG = {
	"APP_PATH":"c:/program files",
	"UE_MAJOR_VER":4,
	"UE_MINOR_VER":26,
	"UE_BIN":"ue4editor.exe",
	"UE_PATH":"{APP_PATH}/epic games/ue_{UE_MAJOR_VER}.{UE_MINOR_VER}/engine/binaries/win64/{UE_BIN}"
	"UE_TOOLS":"{VP_TOOLS_PATH}/unreal_tools"
}

def run_ue(args=[]):

	app = UE_CONFIG['UE_PATH'].format(**UE_CONFIG)
	cmd = [app] + args
	print(app)
	print(os.path.exists(app))
	subprocess.Popen(cmd)

if __name__ == '__main__':
	run_ue()