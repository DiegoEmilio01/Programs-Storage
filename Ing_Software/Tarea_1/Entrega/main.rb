require_relative "funciones.rb"

def main(path_datos, path_instrucciones, path_resultados)
    habitantes, pasajeros = cargar_datos(path_datos)
    instrucciones = leer_instrucciones(path_instrucciones)
    crear_reiniciar_output(path_resultados)
    instrucciones.each do |instruccion|
        if instruccion == "pasajeros_en_cuarentena"
            texto = pasajeros_en_cuarentena(pasajeros)
            escribir_resultados(path_resultados, texto)
        elsif instruccion == "habitantes_en_cuarentena"
            texto = habitantes_en_cuarentena(habitantes)
            escribir_resultados(path_resultados, texto)
        elsif instruccion == "personas_en_cuarentena"
            texto = personas_en_cuarentena(habitantes, pasajeros)
            escribir_resultados(path_resultados, texto)
        elsif instruccion == "personas_en_edad_de_riesgo"
            texto = personas_en_edad_de_riesgo(habitantes, pasajeros)
            escribir_resultados(path_resultados, texto)
        elsif instruccion == "pasajeros_de_paises_infectados"
            texto = pasajeros_de_paises_infectados(pasajeros)
            escribir_resultados(path_resultados, texto)
        elsif instruccion == "pasajeros_de_vuelos_infectados"
            texto = pasajeros_de_vuelos_infectados(pasajeros)
            escribir_resultados(path_resultados, texto)
        end
    end
end

main(ARGV[0], ARGV[1], ARGV[2])



