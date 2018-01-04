#!C:\python27
#-*-coding:utf8-*-

#http://blog.csdn.net/sogouauto/article/details/44622099
#HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon

#import win32api
import _winreg
import os



username="James-win7"
password="james123"

def SetAutoLoginWin(username,password):  
    """ 
    设置window自动登录 
    """  
    key = None
    syswow = os.getenv("windir")+"\\SysWOW64"
    for i in range(2):
        try:
            if os.path.exists(syswow):
                key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows NT\CurrentVersion\Winlogon", 0, _winreg.KEY_ALL_ACCESS|win32con.KEY_WOW64_64KEY)
            else:
                key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows NT\CurrentVersion\Winlogon", 0, _winreg.KEY_ALL_ACCESS)
        except :
            pass
            
        if key:
            break
        else:
            _winreg.CreateKey(_winreg.HKEY_LOCAL_MACHINE,r"Software\Microsoft\Windows NT\CurrentVersion\Winlogon")
  
    try:
        _winreg.SetValueEx(key,"DefaultUserName",0,_winreg.REG_SZ,username)
        _winreg.SetValueEx(key,"DefaultPassword",0,_winreg.REG_SZ,password)
        _winreg.SetValueEx(key,"AutoAdminLogon",0,_winreg.REG_SZ,"1")
        _winreg.SetValueEx(key,"ForceAutoLogon",0,_winreg.REG_SZ,"1")
    except:
        return False
    return True

def DelAutoLoginWin():
    """
    清除window自动登录 
    """
    items=("DefaultUserName","DefaultPassword","AutoAdminLogon","ForceAutoLogon")
    for item in items:
        DeleteRegValue(r"HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon",item)

SetAutoLoginWin(username,password)