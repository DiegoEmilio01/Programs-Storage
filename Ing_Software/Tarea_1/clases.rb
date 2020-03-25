def true?(str)
    if str == "true" then true else false end
end

class Persona
    attr_reader :id, :nombre, :edad

    def initialize(id, nombre, edad)
        @id = id.to_i
        @nombre = nombre
        @edad = edad.to_i
    end
end

class Habitante < Persona
    attr_reader :sector

    def initialize(id, nombre, edad, sector)
        super(id, nombre, edad)
        @sector = sector
    end
end

class Pasajero < Persona
    attr_reader :vuelos, :paises

    def initialize(id, nombre, edad, vuelos, paises)
        super(id, nombre, edad)
        @vuelos = vuelos
        @paises = paises
    end

    def cuarentena
        infectado = false
        if @edad >= 65
            infectado = true
        end
        nombre_paises = []
        @paises.each do |pais|
            nombre_paises << pais.nombre
            if pais.hay_infectados
                infectado = true
            end
        end
        @vuelos.each do |vuelo|
            if (vuelo.hay_infectados) or (vuelo.dias_desde_vuelo <= 14)
                infectado = true
            end
        end
        if infectado
            texto_paises = nombre_paises.join(" - ")
            cantidad_vuelos = @vuelos.length.to_s
            return texto_paises + ". " + cantidad_vuelos
        else
            return infectado
        end
    end
end

class Sector
    attr_reader :id, :hay_infectados

    def initialize(id, hay_infectados)
        @id = id.to_i
        @hay_infectados = true? hay_infectados
    end
end

class Vuelo
    attr_reader :id, :hay_infectados, :dias_desde_vuelo

    def initialize(id, hay_infectados, dias_desde_vuelo)
        @id = id.to_i
        @hay_infectados = true? hay_infectados
        @dias_desde_vuelo = dias_desde_vuelo.to_i
    end
end

class Pais
    attr_reader :id, :nombre, :hay_infectados

    def initialize(id, nombre, hay_infectados)
        @id = id.to_i
        @nombre = nombre
        @hay_infectados = true? hay_infectados
    end
end
