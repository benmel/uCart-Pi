from bluetooth import *
import logging

logging.basicConfig(filename="rfcomm.log", level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

try:
  while True:                   
    logger.info("Waiting for connection on RFCOMM channel %d", port)
    client_sock, client_info = server_sock.accept()
    logger.info("Accepted connection from %s", client_info)

    try:
      while True:
        try:
          text = raw_input()
          text_strip = text.strip()
          if text_strip:
            logger.info("Sending text: %s", text_strip)
            text_strip += '\n'
            client_sock.send(text_strip)
        except IOError:
          logger.error("IOError")
          pass
    except KeyboardInterrupt:    
      logger.info("Disconnected")
      client_sock.close()
      server_sock.close()
      break

except KeyboardInterrupt:
  pass

logger.info("Exiting")
