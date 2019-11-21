REFRESH_TIME = 61
#OS = "Windows"
OS = 'Linux'

ADDRS_DICT = {'Херсон': "10.65.1.1",
              'Херсон-2': "192.168.1.2",
              'Берислав': "10.65.11.1",
              'В.Лепетиха': "10.65.12.1",
              'Геническ': "10.65.16.1",
              'Гопры': "10.65.17.1",
              'Каховка': "10.65.21.1",
              'Н.Каховка': "10.65.23.1",
              'Скадовск': "10.65.26.1",
              'Чаплынка': "10.65.28.1",
              'Цюрупинск': "10.65.35.1",
              'Новотроицк': "10.65.40.1",
              'KS_inet': "213.179.245.34",
              'GOOGLE': '8.8.8.8'}

if OS.lower() == 'windows':
    SYSTEM_PING_COMMAND = ["ping", "-n", "1"]
else:
    SYSTEM_PING_COMMAND = ["ping", "-c", "1"]