import wmi
import json
import re
import win32api
import win32con
from pyDes import *
import os
import base64

class register:
    def __init__(self):
        self.Des_Key = "DESCRYPT"  # Key
        self.Des_IV = "\x15\1\x2a\3\1\x23\2\0"

    global s
    s = wmi.WMI()

    def get_CPU_info(self):
        cpu = []
        cp = s.Win32_Processor()
        for u in cp:
            cpu.append({"Serial Number": u.ProcessorId,})
        return cpu[0]['Serial Number']

    def get_disk_info(self):
        disk = []
        for pd in s.Win32_DiskDrive():
            disk.append({"Serial": s.Win32_PhysicalMedia()[0].SerialNumber.lstrip().rstrip()})
        return disk[0]['Serial']
        # return disk

    def get_mainboard_info(self):
        mainboard = []
        for board_id in s.Win32_BaseBoard():
            mainboard.append(board_id.SerialNumber.strip().strip('.'))
        return mainboard[0]

    def get_network_info(self):
        network = []
        for nw in s.Win32_NetworkAdapterConfiguration ():  # IPEnabled=0
            if nw.MACAddress != None:
                network.append({"MAC": nw.MACAddress})
    #    print(":::Network info:", json.dumps(network))
        cop = re.compile("[^\u4e00-\u9fa5^a-z^A-Z^0-9]")
        network = cop.sub('', network[0]['MAC'])
        return network

    def get_bios_info(self):
        bios = []
        for bios_id in s.Win32_BIOS():
            bios.append(bios_id.SerialNumber.strip().strip('.'))
        return bios[0]

    def getCombinNumber(self):
        n = 0
        a = self.get_disk_info()
        if len(a) == 0:
            an = a
            n = n + 1
        else:
            an = a[1] + a[3] + a[5] + a[-5] + a[-3] + a[-1]
        b = self.get_mainboard_info()
        # b = str('AD9SA8S6FD8A9G')
        if len(b) == 0:
            bn = b
            n = n + 1
        else:
            bn = b[1]+b[3]+b[5]+b[-5]+b[-3]+b[-1]
        c = self.get_network_info()
        if len(c) == 0:
            cn = c
            n = n + 1
        else:
            cn = c[1]+c[3]+c[5]+c[-5]+c[-3]+c[-1]
        d = self.get_CPU_info()
        dn = d[1] + d[3] + d[5] + d[-5] + d[-3] + d[-1]
        e = self.get_bios_info()
        en = e[1] + e[3] + e[5] + e[-5] + e[-3] + e[-1]
        if n == 3:
            machinecode_str = []
        if n < 3:
            if n > 0:
                machinecode_str = an + bn + cn + dn + en
                machinecode_str = machinecode_str[:12]
            if n == 0:
                a_new = a[0] + a[2] + a[-4] + a[-2]
                b_new = b[0] + b[2] + b[-4] + b[-2]
                c_new = c[0] + c[2] + c[-4] + c[-2]
                machinecode_str = a_new + b_new + c_new
        return machinecode_str, n

    def Encrypted(self, tr):
        k = des(self.Des_Key, CBC, self.Des_IV, pad=None, padmode=PAD_PKCS5)
        EncryptStr = k.encrypt(tr)
        EncryptStr = base64.b64encode(EncryptStr)
        cop = re.compile("[^\u4e00-\u9fa5^a-z^A-Z^0-9]")
        EncryptStr = str.encode(cop.sub('', EncryptStr.decode()))
        return EncryptStr

    def regist(self):
        key = input('请输入注册码: ')
        if key:
            ontent, n = self.getCombinNumber()
            if n == 3:
                print('本机不符合注册要求，请联系售后')
            tent = bytes(ontent, encoding='utf-8')
            content = self.Encrypted(tent)
            key_decrypted = bytes(key, encoding='utf-8')
            if content != 0 and key_decrypted != 0:
                if content != key_decrypted:
                    print("注册码无效，请检查注册码是否正确并再次输入。")
                    self.regist()
                elif content == key_decrypted:
                    print("注册成功。")
                    # TODO:将注册码的ASC码值+5写入注册表，再读取时将从注册表读取
                    # key 的 ASCII码 +5 存入注册文件中
                    key_1 = []
                    key_2 = ''
                    for i in range(len(key)):
                        key_1.append(chr(ord(key[i]) + 5))
                    for item in key_1:
                        key_2 = key_2 + str(item)
                    with open('register.txt', 'w') as f:
                        f.write(str(key_2))
                        f.close()
                    return True
                else:
                    return False
            else:
                return False
        else:
            self.regist()
            return False

    def checkAuthored(self):
        ontent, n = self.getCombinNumber()
        if n == 3:
            print('本机不符合注册要求，请联系售后')
        else:
            tent = bytes(ontent, encoding='utf-8')
            content = self.Encrypted(tent)
            try:
                # TODO：写入注册表
                f = open('register.txt', 'r')
                if f:
                    key_old = f.read()
                    key_1 = []
                    key = ''
                    for i in range(len(key_old)):
                        key_1.append(chr(ord(key_old[i]) - 5))
                    for item in key_1:
                        key = key + str(item)
                    if key:
                        key_decrypted = bytes(key, encoding='utf-8')  # 注册文件中注册码
                        if key_decrypted:
                            if key_decrypted == content:
                                print("欢迎使用。")
                            else:
                                print('未找到注册文件，', '请重新输入注册码，', '或发送', ontent, '至售后', '重新获取注册码')
                                self.regist()
                        else:
                            self.regist()
                            print('未找到注册文件，', '请重新输入注册码，', '或发送', ontent, '至售后', '重新获取注册码')
                    else:
                        self.regist()
                        print('未找到注册文件，', '请重新输入注册码，', '或发送', ontent, '至售后', '重新获取注册码')
                else:
                    self.regist()
            except:
                print('请发送', ontent, '至售后', '获取注册码')
                self.regist()

local_serial  = '029813910F9F'
#local_serial = str(local_serial)
reg = register()
tent = bytes(local_serial, encoding='utf-8')
content = reg.Encrypted(tent)
print(content)