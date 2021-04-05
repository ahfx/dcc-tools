"""
run unreal bootstrapped with unreal_tools
"""

import os
import subprocess

import dcc_tools.log as log
import dcc_tools.paths as paths

print(os.path.abspath(__file__))

UE_CONFIG = {
	"APPS_PATH":"{APPS_PATH}".format(APPS_PATH=os.environ['APPS_PATH']),
	"UE_MAJOR_VER":4,
	"UE_MINOR_VER":26,
	"UE_BIN":"ue4editor.exe",
	"UE_PATH":"{APPS_PATH}/epic games/ue_{UE_MAJOR_VER}.{UE_MINOR_VER}/engine/binaries/win64/{UE_BIN}",
	"UE_TOOLS_PATH":"{VP_TOOLS_PATH}/unreal-tools".format(
		VP_TOOLS_PATH=paths.norm_path(os.environ['VP_TOOLS_PATH'])),
	"UE_SITE_PATH":"{VP_TOOLS_PATH}/unreal-tools/{VP_TOOLS_SITE_SUFFIX}".format(
		VP_TOOLS_PATH=paths.norm_path(os.environ['VP_TOOLS_PATH']), 
		VP_TOOLS_SITE_SUFFIX=os.environ['VP_TOOLS_SITE_SUFFIX'])
}

def run(args=[]):
	"""
	Run UnrealEngine4 in a subprocess
	
	Args:
	    args (list, optional): Description
	"""
	log.info(UE_CONFIG)

	app = UE_CONFIG['UE_PATH'].format(**UE_CONFIG)
	cmd = [app] + args

	log.info(app)
	log.info(os.path.exists(app))

	pythonpath = ';'.join([x for x in [os.environ.get('PYTHONPATH', ''), 
		UE_CONFIG['UE_TOOLS_PATH'], UE_CONFIG['UE_SITE_PATH']] if x])

	log.info(pythonpath)

	env = os.environ.copy()
	env['PYTHONPATH'] = pythonpath
	subprocess.Popen(cmd, env=env)
	log.info('Loading Unreal ... ')

if __name__ == '__main__':
	run_ue()
