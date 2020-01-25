import time
import json




import json

def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError as e:
    return False
  return True




def tail(f, window=1):
    """
    Returns the last `window` lines of file `f` as a list of bytes.
    """
    if window == 0:
        return b''
    BUFSIZE = 1024
    f.seek(0, 2)
    end = f.tell()
    nlines = window + 1
    data = []
    while nlines > 0 and end > 0:
        i = max(0, end - BUFSIZE)
        nread = min(end, BUFSIZE)

        f.seek(i)
        chunk = f.read(nread)
        data.append(chunk)
        nlines -= chunk.count(b'\n')
        end -= nread
    return b'\n'.join(b''.join(reversed(data)).splitlines()[-window:])

if __name__ == "__main__":
    check2 = " "
    while(1):

        with open("/Users/majdsalaheddin/Desktop/test_final", 'rb') as f:
            last_lines = tail(f, 1).decode('utf-8')
            checker = last_lines
            if checker != check2:
                check2 = checker
                if is_json(check2) :
                    d = json.loads(check2)
                    print(d)



        time.sleep(0.2)
