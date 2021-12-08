#
#
#
#

import argparse
import logging
import sys

def main():
    '''
    Esta es una funcion para ejecutar el script desde otros scripts.
    Cuando se use esta funcion desde otro script se debe de asignar las flags de logging
    :return:
    '''
    logger.info("-" * 50)
    logger.info("          Titulo de Script")
    logger.info("-" * 50)

    # agregar codigo a partir de aqui


if __name__ == '__main__':
    '''
    Esta es lal funcion que se ejecuta directamente de este script con parsing de entradas (input), opciones y logging
    '''
    parser = argparse.ArgumentParser(description='Describe tu codigo aqui')
    parser.add_argument('-v', '--verbosity', type=int, default=0, help='Nivel de informacion impresa a stdout')
    args = parser.parse_args()

    # Sistema de Log
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # manejo de archivo
    log_file = "tu_script.log"
    handler = logging.FileHandler(log_file, mode='w')
    handler.setLevel(logging.DEBUG)

    # Crear formato de Logging
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # crear handle para std
    handler2 = logging.StreamHandler(sys.stdout)
    handler2.setLevel(logging.INFO)
    if (args.verbosity > 9):
        handler2.setLevel(logging.DEBUG)

    formatter2 = logging.Formatter('[-] %(message)s')
    handler2.setFormatter(formatter2)

    # agregar hanldes a logger
    logger.addHandler(handler)
    logger.addHandler(handler2)
    logger.info('Archivo de Log escrito a archivo %s\n' %log_file)
    logger.debug('Corriendo con verbosity nivel: %i' %args.verbosity)


    #llamar al codigo principal
    main()

    logger.info("FIN")