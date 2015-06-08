from bluetooth import *
import logging

logging.basicConfig(filename="rfcomm.log", level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service( server_sock, "uCartPi",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ],
#                   protocols = [ OBEX_UUID ] 
                    )

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
          break
    except KeyboardInterrupt:    
      logger.info("Disconnected")
      client_sock.close()
      server_sock.close()
      break

except KeyboardInterrupt:
  pass

logger.info("Exiting")
