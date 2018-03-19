#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import time
import datetime
import os
import sys
# third party libs
from daemon import runner

from excel_oper_demo import UpdateExcel

reload(sys)
sys.setdefaultencoding('utf8')


class Updater():
    CMD_SVN = {
        "svn_checkout": "svn checkout ",
        "svn_info": "svn info ",
        "svn_lock": "svn lock --force ",
        "svn_unlock": "svn unlock ",
        "svn_update": "svn update ",
        "svn_commit": "svn commit -m 'commit by auto merge' "
    }

    def __init__(self, version=None, svn_path=None, source_files=None, desti_file=None, sheet_name=None,):
        self.stdin_path = '/dev/stdin'
        self.stdout_path = '/dev/stdout'
        self.stderr_path = '/dev/stderr'
        self.pidfile_path = '/tmp/testdaemon.pid'
        self.pidfile_timeout = 5
        self.files_version = {}
        self.is_first = True
        self.version = version
        self.svn_path = svn_path
        self.source_files = source_files
        self.desti_file = desti_file
        self.sheet_name = sheet_name
        self.excel_oper_client = None
        self.this_weekly_sheet_name = None
        self.last_weekly_sheet_name = None
	self.new_sheet_name = None

    def get_svn_file_lock(self, file=None, lock=0):
        while True:
            count = 0
            file_info = os.popen(self.CMD_SVN['svn_info'] + " '%s' " % file).readlines()
            logger.info('get svn file info %s' % file_info)
            for info in file_info:
                if 'Lock Owner' in info:
                    lock = 1
                    break
            if lock == 1:
                if count < 5:
                    time.sleep(10)
                    count = count + 1
                    logger.info('the file(%s) is locked by other, wait %s' % (file, count))
                    continue
                else:
                    lock_info = os.popen(self.CMD_SVN['svn_lock'] + " '%s' " % file + '--force').readlines()
                    logger.info('the file(%s) is forced to locked by auto-sprint, %s' % (file, lock_info))
            else:
                lock_info = os.popen(self.CMD_SVN['svn_lock'] + " '%s' " % file).readlines()
                logger.info('the file(%s) is locked by auto-sprint, %s' % (file, lock_info))
                break

    def relase_svn_file_lock(self, file=None):
        unlock_info = os.popen(self.CMD_SVN['svn_unlock'] + " '%s' " % file).readlines()
        logger.info('the file(%s) is unlocked by auto-sprint, %s' % (file, unlock_info))

    def get_svn_file_version(self, file=None):
        file_info = os.popen(self.CMD_SVN['svn_info'] + " '%s' " % file).readlines()
        for info in file_info:
            if 'Last Changed Rev' in info:
                version = filter(str.isdigit, info)
                logger.info("get this file(%s) svn version(%s)" % (file, version))
        return version

    def update_svn_file(self, file=None):
        update_info = os.popen(self.CMD_SVN['svn_update'] + " '%s' " % file).readlines()
        logger.info('update svn file(%s), %s' % (file, update_info))

    def get_source_files(self):
        files = os.popen('ls').readlines()
        source_files = []
        for file in files:
            if u'测试SprintBacklog - ' in file:
                source_files.append(file.strip())
        self.source_files = source_files
        return source_files

    def get_desti_file(self):
        files = os.popen('ls').readlines()
        desti_file = None
        for file in files:
            if u'测试SprintBacklog.xls' in file:
                desti_file = file.strip()
        self.desti_file = desti_file
        return desti_file

    def commit_svn_file(self, file=None):
        logger.info('commit %s' % file)
        return os.popen(self.CMD_SVN['svn_commit'] + " '%s' " % file).readlines()

    def excel_oper(self, desti_file, is_style):
        self.set_sheet_name()
        source_files = self.get_source_files()
        self.excel_oper_client = UpdateExcel(desti_file=desti_file)
	print self.new_sheet_name
	print self.sheet_name
	self.excel_oper_client.update_excel(source_files, desti_file, self.new_sheet_name[1], self.sheet_name[1],
                                             is_style)
        self.excel_oper_client.update_excel(source_files, desti_file, self.new_sheet_name[0], self.sheet_name[0],
                                            is_style)
        if self.commit_svn_file(desti_file) == []:
            self.relase_svn_file_lock(desti_file)
    
    def get_weekly_range(self, this_or_last_week=None):
	if this_or_last_week not in ["this", "last"]:
	    raise ValueError("The this_or_last_week must be 'this' or 'last'")
        now_day = datetime.datetime.now()
        weekday = datetime.datetime.now().weekday()
	if this_or_last_week == "this":
	    day_delta = {0: (0, 4), 1: (-1, 3), 2: (-2, 2), 3: (-3, 1), 4: (-4, 0), 5: (-5, -1), 6: (-6, -2)}
	else:
	    day_delta = {0: (-7, -3), 1: (-8, -4), 2: (-9, -5), 3: (-10, -6), 4: (-11, -7), 5: (-12, -8), 6: (-13, -9)}
	to_one_delta = datetime.timedelta(days=day_delta.get(weekday)[0])
	to_five_delta = datetime.timedelta(days=day_delta.get(weekday)[1])
	to_one = now_day + to_one_delta
	to_five = now_day + to_five_delta
	return to_one.strftime('%m.%d') + '-' + to_five.strftime('%m.%d')
	
    def get_this_weekly_range(self):
	return self.get_weekly_range(this_or_last_week="this")

    def get_last_weekly_range(self):
	return self.get_weekly_range(this_or_last_week="last")

    def set_sheet_name(self):
        weekday = datetime.datetime.now().weekday()
        this_weekly_range = self.get_this_weekly_range()
        self.this_weekly_sheet_name = this_weekly_range
        last_weekly_range = self.get_last_weekly_range()
        self.last_weekly_sheet_name = last_weekly_range
	start_day = datetime.datetime.strptime('2018-02-26', '%Y-%m-%d')
	today = datetime.datetime.now()
	weeks = (today - start_day).days / 7 + 1
	this_weekly_new_sheet_name = u'sprint' + str(weeks) + u'(' + this_weekly_range + u')'
	last_weekly_new_sheet_name = u'sprint' + str(weeks-1) + u'(' + last_weekly_range + u')'
        self.new_sheet_name = [this_weekly_new_sheet_name, last_weekly_new_sheet_name]
	self.sheet_name = [self.this_weekly_sheet_name, self.last_weekly_sheet_name]
	#self.new_sheet_name = [u'sprint17（02.26~03.02）']
	#self.sheet_name = [u'02.26~03.02']

    def monitor_svn_files(self):
        if self.is_first is True:
            os.system('mkdir -p /sf/sprint/%s' % self.version)
            logger.info('mkdir -p /sf/sprint/%s' % self.version)
            os.chdir('/sf/sprint/%s' % self.version)
            logger.info('cd /sf/sprint/%s' % self.version)
            checkout = os.popen(self.CMD_SVN['svn_checkout'] + " '%s' " % self.svn_path).readlines()
            logger.info("checkout svn file: %s" % checkout)
            svn_src = os.popen("ls").readlines()[0].rstrip()
            os.chdir(svn_src)
            logger.info('cd %s' % svn_src)
            desti_file = self.get_desti_file()
            self.update_svn_file(desti_file)
            self.get_svn_file_lock(desti_file)
            self.excel_oper(desti_file, False)
            self.excel_oper(desti_file, True)
            for s_file in self.source_files:
                svn_version = self.get_svn_file_version(s_file)
                self.files_version[s_file] = svn_version
            self.is_first = False
        else:
            merge_excel_flag = False
            for file in self.source_files:
                self.update_svn_file(file)
                version = self.get_svn_file_version(file)
                if version != self.files_version[file]:
                    self.files_version[file] = version
                    merge_excel_flag = True

            if merge_excel_flag is True:
                desti_file = self.get_desti_file()
                self.update_svn_file(desti_file)
                self.get_svn_file_lock(desti_file)
                self.excel_oper(desti_file, False)
                self.excel_oper(desti_file, True)

    def run(self):
        while True:
            self.monitor_svn_files()
            time.sleep(120)


if __name__ == "__main__":
    # version = raw_input("Please input the version of your project, such as aCloud5.8.5")
    # svn_path = raw_input("Please input the sprint svn path of your project")
    version = u'EDR3.2.2'
    svn_path = u'https://200.200.0.8/svn/test/测试部文件服务器/测试工程/EDR版本/EDR3.2.2/01-项目管理/02-计划类/sprint'
    app = Updater(version=version, svn_path=svn_path)

    logger = logging.getLogger("DaemonLog")
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler = logging.FileHandler("/tmp/testdaemon.log")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    daemon_runner = runner.DaemonRunner(app)
    # This ensures that the logger file handle does not get closed during daemonization
    daemon_runner.daemon_context.files_preserve = [handler.stream]
    daemon_runner.do_action()
