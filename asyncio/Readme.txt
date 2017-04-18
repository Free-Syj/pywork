import asyncio
@asyncio.coroutine
def wget(host):
  print('wget %s...' % host)
  connect = asyncio.open_connection(host, 80)
  reader, writer = yield from connect
  header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
  writer.write(header.encode('utf-8'))
  yield from writer.drain()
  while True:
       line = yield from reader.readline()
       if line == b'\r\n':
            break
       print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
  # Ignore the body, close the socket
  writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

Ϊ�˼򻯲����õر�ʶ�첽IO����Python 3.5��ʼ�������µ��﷨async��await��������coroutine�Ĵ��������׶���
1 - ��@asyncio.coroutine�滻Ϊasync��
2 - ��yield from�滻Ϊawait��
async def wget(host):
       await write.drain()
