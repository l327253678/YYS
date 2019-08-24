import os
import re
import sys
import time
from Crack_Onmyoji.crack_service import CrackService
from Crack_Onmyoji.log_recorder import LogRecorder


def main():
    run_time = time.strftime("%Y %m %d %H:%M:%S", time.localtime())
    sys.stdout = LogRecorder('./logs/' + '_'.join(re.split(r'[\\ |:]', run_time)) + '_log.txt')
    c0 = CrackService(0, [['accept_invite', 'tz']])
    c1 = CrackService(1, [['accept_invite', 'tz']])
    c0.accept_invite('tz', change_champion=True)
    # c0.solo_mode("mitama", "original_fire", 100)
    # c0.mitama_or_awake_invite("mitama", "10", [('cross', 'tz')], 100, True)
    # c1 = CrackService(1,
    #                   [['mitama_or_awake_invite', 'mitama', '11', [('cross', 'xgrcey')], 200]])
    # c0.start()
    # c1.start()
    # c2.start()
    # c2.join()
    # c2 = CrackService(2,
    #                   [['mitama_or_awake_invite', 'awake', 'wind', [('cross', 'ybymq'), ('cross', 'xgrcey')], 1
    #                     ]])
    # c2.start()
    # c2.join()
    # c1.personal_break_through()
    # c0.group_break_through()
    # c0.open_close_buff('mitama', True)
    # c1 = CrackService(0, [['accept_invite']])
    # c2 = CrackService(3,
    #                   [['mitama_or_awake_invite', 'mitama', '11', [('cross', 'xgrcey')]]])
    # c1.start()
    # c2.start()
    # os.system('shutdown -s -t 10')
    # c0.accept_invite(timer=60 * 60 * 5)
    # c0.accept_invite(timer=60 * 60 * 3)
    # os.system('shutdown -s -t 60')
    # c0.hundred_ghosts(100)
    # while True:
    #     c0.hundred_ghosts(100)
    #     CrackController.random_sleep(100, 200)
    # c1 = CrackService(0, [['accept_invite', 'tz']])
    # c2 = CrackService(3,
    #                   [['mitama_or_awake_invite', 'mitama', '11', [('cross', 'xgrcey')], 400]])
    # c1.setDaemon(True)
    # c1.start()
    # c2.start()
    # c2.join()
    # os.system('shutdown -s -t 60')


if __name__ == '__main__':
    main()
