require "csv"
require_relative "clases.rb"


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
        vuelos.each do |vuelo|
            lista_vuelos << dict_vuelos[vuelo.to_i]
        end
        paises.each do |pais|
            lista_paises << dict_paises[pais.to_i]
        end
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
    texto = "*** COMIENZO PASAJEROS EN CUARENTENA ***\n\n"
    pasajeros.each_value do |pasajero|
        texto_pasajero = pasajero.nombre + ": " + pasajero.edad.to_s
        texto_cuarentena = pasajero.cuarentena
        if texto_cuarentena
            texto += texto_pasajero + ". " + texto_cuarentena + "\n"
        end
    end
    puts texto + "\n*** FIN PASAJEROS EN CUARENTENA ***\n\n"
end
