require_relative "funciones.rb"

def main(carpeta)
    habitantes, pasajeros = cargar_datos(carpeta)
    pasajeros_en_cuarentena(pasajeros)
end

main(ARGV[0])
