require "csv"
require_relative "clases.rb"

def escribir_resultados(path, texto)
    File.open(path, "a") {|file| file.write(texto)}
end

def crear_reiniciar_output(path)
    File.open(path, "w") {|file|}
end

def leer_instrucciones(path)
    instrucciones = []
    File.open(path, "r") do |file|
        file.each_line {|line| instrucciones << line.to_s.chomp}
    end
    return instrucciones
end

def leer_paises(carpeta)
    csv = CSV.parse(File.read(File.join(carpeta, "paises.csv")), headers: true)
    dict = {}
    (0...csv.length).each do |i|
        pais = Pais.new(csv[i]["id"], csv[i]["nombre"], csv[i]["hay_infectados"])
        dict[csv[i]["id"].to_i] = pais
    end
    return dict
end

def leer_sectores(carpeta)
    csv = CSV.parse(File.read(File.join(carpeta, "sectores.csv")), headers: true)
    dict = {}
    (0...csv.length).each do |i|
        sector = Sector.new(csv[i]["id"], csv[i]["hay_infectados"])
        dict[csv[i]["id"].to_i] = sector
    end
    return dict
end

def leer_vuelos(carpeta)
    csv = CSV.parse(File.read(File.join(carpeta, "vuelos.csv")), headers: true)
    dict = {}
    (0...csv.length).each do |i|
        vuelo = Vuelo.new(csv[i]["id"], csv[i]["hay_infectados"], csv[i]["dias_desde_vuelo"])
        dict[csv[i]["id"].to_i] = vuelo
    end
    return dict
end

def leer_habitantes(carpeta, dict_sectores)
    csv = CSV.parse(File.read(File.join(carpeta, "habitantes.csv")), headers: true)
    dict = {}
    (0...csv.length).each do |i|
        habitante = Habitante.new(csv[i]["id"], csv[i]["nombre"],
        csv[i]["edad"], dict_sectores[csv[i]["sector"].to_i])
        dict[csv[i]["id"].to_i] = habitante
    end
    return dict
end

def leer_pasajeros(carpeta, dict_vuelos, dict_paises)
    csv = CSV.parse(File.read(File.join(carpeta, "pasajeros.csv")), headers: true)
    dict = {}
    (0...csv.length).each do |i|
        vuelos = csv[i]["vuelos"].split(":")
        paises = csv[i]["paises"].split(":")
        lista_vuelos = []
        lista_paises = []
        vuelos.each {|vuelo| lista_vuelos << dict_vuelos[vuelo.to_i]}
        paises.each {|pais| lista_paises << dict_paises[pais.to_i]}
        pasajero = Pasajero.new(csv[i]["id"], csv[i]["nombre"], csv[i]["edad"],
        lista_vuelos, lista_paises)
        dict[csv[i]["id"].to_i] = pasajero
    end
    return dict
end

def cargar_datos(carpeta)
    dict_sectores = leer_sectores(carpeta)
    dict_paises = leer_paises(carpeta)
    dict_vuelos = leer_vuelos(carpeta)
    dict_habitantes = leer_habitantes(carpeta, dict_sectores)
    dict_pasajeros = leer_pasajeros(carpeta, dict_vuelos, dict_paises)
    return dict_habitantes, dict_pasajeros
end

def pasajeros_en_cuarentena(pasajeros)
    texto = "*** COMIENZO PASAJEROS EN CUARENTENA ***\n"
    pasajeros.each_value do |pasajero|
        texto_pasajero = pasajero.nombre + ": " + pasajero.edad.to_s
        texto_cuarentena = pasajero.cuarentena("todo")
        if texto_cuarentena
            texto += texto_pasajero + ". " + texto_cuarentena + "\n"
        end
    end
    #puts texto + "\n*** FIN PASAJEROS EN CUARENTENA ***\n\n"
    return texto + "*** FIN PASAJEROS EN CUARENTENA ***\n"
end

def habitantes_en_cuarentena(habitantes)
    texto = "*** COMIENZO HABITANTES EN CUARENTENA ***\n"
    habitantes.each_value do |habitante|
        texto_habitante = (habitante.nombre + ": " + habitante.edad.to_s + ". Sector " +
        habitante.sector.id.to_s + "\n")
        cuarentena = habitante.cuarentena
        if cuarentena
            texto += texto_habitante
        end
    end
    #puts texto + "\n*** FIN HABITANTES EN CUARENTENA ***\n\n"
    return texto + "*** FIN HABITANTES EN CUARENTENA ***\n"
end

def personas_en_cuarentena(habitantes, pasajeros)
    texto = "*** COMIENZO PERSONAS EN CUARENTENA ***\n"
    habitantes.each_value do |habitante|
        texto_habitante = habitante.nombre + ": " + habitante.edad.to_s + ". Habitante\n"
        cuarentena = habitante.cuarentena
        if cuarentena
            texto += texto_habitante
        end
    end
    pasajeros.each_value do |pasajero|
        texto_pasajero = pasajero.nombre + ": " + pasajero.edad.to_s + ". Pasajero\n"
        cuarentena = pasajero.cuarentena("todo")
        if cuarentena
            texto += texto_pasajero
        end
    end
    #puts texto + "\n*** FIN PERSONAS EN CUARENTENA ***\n\n"
    return texto + "*** FIN PERSONAS EN CUARENTENA ***\n"
end

def personas_en_edad_de_riesgo(habitantes, pasajeros)
    texto = "*** COMIENZO PERSONAS EN EDAD DE RIESGO ***\n"
    habitantes.each_value do |habitante|
        texto_habitante = habitante.nombre + ": " + habitante.edad.to_s + ". Habitante\n"
        if habitante.edad >= 65
            texto += texto_habitante
        end
    end
    pasajeros.each_value do |pasajero|
        texto_pasajero = pasajero.nombre + ": " + pasajero.edad.to_s + ". Pasajero\n"
        if pasajero.edad >= 65
            texto += texto_pasajero
        end
    end
    #puts texto + "\n*** FIN PERSONAS EN EDAD DE RIESGO ***\n\n"
    return texto + "*** FIN PERSONAS EN EDAD DE RIESGO ***\n"
end

def pasajeros_de_paises_infectados(pasajeros)
    texto = "*** COMIENZO PASAJEROS DE PAISES INFECTADOS ***\n"
    pasajeros.each_value do |pasajero|
        texto_pasajero = pasajero.nombre + ": " + pasajero.edad.to_s
        texto_cuarentena = pasajero.cuarentena("paises")
        if texto_cuarentena
            texto += texto_pasajero + ". " + texto_cuarentena + "\n"
        end
    end
    #puts texto + "\n*** FIN PASAJEROS DE PAISES INFECTADOS ***\n\n"
    return texto + "*** FIN PASAJEROS DE PAISES INFECTADOS ***\n"
end

def pasajeros_de_vuelos_infectados(pasajeros)
    texto = "*** COMIENZO PASAJEROS DE VUELOS INFECTADOS ***\n"
    pasajeros.each_value do |pasajero|
        texto_pasajero = pasajero.nombre + ": " + pasajero.edad.to_s
        texto_cuarentena = pasajero.cuarentena("vuelos")
        if texto_cuarentena
            texto += texto_pasajero + ". " + texto_cuarentena + "\n"
        end
    end
    #puts texto + "\n*** FIN PASAJEROS DE VUELOS INFECTADOS ***\n\n"
    return texto + "*** FIN PASAJEROS DE VUELOS INFECTADOS ***\n"
end