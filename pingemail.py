import os, sys, time

EMAIL_COMMAND = "echo \"Ping went through %d times after %d attempts\" | mail -s \"Ping worked for host %s!\" %s"
PING_COMMAND = "ping -c 1 %s"

def main():
  if not len(sys.argv) == 3:
    print "Expected useage:\n\tpython pingemail.py <ip/hostname> <email>"
    return

  attempts = 0
  goodAttempts = 0
  while True:
    result = os.system(PING_COMMAND % sys.argv[1])
    attempts += 1
    goodAttempts += 1
    if result == 0 and goodAttempts == 3:
      os.system(EMAIL_COMMAND % (goodAttempts, attempts, sys.argv[1], sys.argv[2]))
      return
    elif not result == 0:
      goodAttempts = 0

    time.sleep(3)

if __name__ == "__main__":
  main()
